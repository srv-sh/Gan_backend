from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from PIL import Image
from PIL import ImageFilter
import requests

app = FastAPI(title="FashionGEN Tiger Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
async def send_img(files):    
    url = 'http://localhost:8000/get_generated_img'
    res  = requests.post(url, files=files)
    print(f"tiger{res}")

@app.post("/send_generated_img")
async def get_img(prompt: str):
                            ## DO SOMETHING WITH THE PROMPT ##
    print(prompt)
    files = {'img': open('face.jpg', 'rb')}
    await send_img(files)

    return
    
