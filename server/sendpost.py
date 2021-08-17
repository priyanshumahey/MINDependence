import requests

white = 'LightCoral'
x = str(white)


url = 'http://127.0.0.1:5000/setState'
state_info = {'state': x}
x = requests.post(url, params=state_info)

