"""
These are my data analysis functions used to download and process some temperature time series from berkely earth.
"""
import numpy as np
import requests

def generate_url(location):
    url = f'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/{(location.lower())}-TAVG-Trend.txt'
    return url
	
def download_data(location):
    url = generate_url(location)
    # Download the content of the URL
    response = requests.get(url)
    
    data = np.loadtxt(response.iter_lines(), comments="%")
    
    return data
	
def moving_average(data,width):
	"""
	Computes the moving average
	
	:param data: Input data array
	:param width: Width in samples
	"""
    moving_avg = np.full(data.size, np.nan)
    for i in range(width, moving_avg.size - width):
        moving_avg[i] = np.mean(data[i - width:i + width])
    return moving_avg
	
def test_moving_avg():
    avg = moving_average(np.ones(10000),2)
    assert np.all(np.isnan(avg[0:2]))
    assert np.all(np.isnan(avg[-2:]))
    assert np.allclose(avg[2:-2], 1)