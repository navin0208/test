import requests
import json

url = 'http://127.0.0.1:5000/send_data'  # Make sure to use the correct endpoint

data = {
    'pi_id': 'Pi-1',
    'product_count': 50,
    'not_ok_count': 2,
    'shift': 'Shift 1'
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Data sent successfully:", response.json())
else:
    print("Error sending data:", response.status_code, response.text)
