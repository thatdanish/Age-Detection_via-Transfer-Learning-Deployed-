import requests

url = 'http://127.0.0.1:5000/deploy'
image_path = 'srk.jfif'

image = open(image_path,'rb').read()
payload = {'image':image}

r = requests.post(url,files=payload).json()

if r['success']:
    print(r['prediction'])

else: 
    print("Request Failed!! Restart the server and try again.")