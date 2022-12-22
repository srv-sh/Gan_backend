# client.py
import requests
url = 'http://localhost:5000/send_generated_img'
files = {'img': open('face.jpg', 'rb')}
res  = requests.post(url, files=files)
print(res)