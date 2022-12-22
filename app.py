from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from PIL import Image
from PIL import ImageFilter
import requests

app = FastAPI(title="FashionGEN Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def send_request(prompt: str):
    url = 'http://localhost:5000/send_generated_img'
    data = {'prompt': prompt}
    r = requests.post(url, params=data)
    return r

@app.post("/get_generated_img")
async def get_img(img: UploadFile = File(...)):
    original_image = Image.open(img.file)
    generated_image = BytesIO()
    original_image.save(generated_image, "JPEG")
    generated_image.seek(0)
    print("works")
    return StreamingResponse(generated_image, media_type="image/jpeg")
    

@app.post("/generate")
def generate_img(prompt: str):
    res= send_request(prompt)
    print(f"app = {res}")
    return 
