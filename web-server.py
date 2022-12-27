## REQUIRED IMPORTS
import socketio
from fastapi import FastAPI
from decouple import config
import uvicorn
from utils import Fashion_Generator_Handler


## Handler
fashion_gen = Fashion_Generator_Handler()




## DECLARING SOCKET APP
sio = socketio.AsyncServer(async_mode='asgi',ping_timeout=80,cors_allowed_origins='*')
socket_app = socketio.ASGIApp(sio)

## initializing fastapi instance
app = FastAPI(title="FASHION GEN")



## MOUNT APP WITH SOCKET APP
app.mount("/", socket_app)  



## RECEIVING FROM USER(FRONT)
@sio.on("prompt")
async def admin_uttered(sid,resp):
    prompt = resp["prompt"]
    user_id = resp["user_id"]
    url = fashion_gen.generate_img(prompt=prompt)
    data = {"user_id" : user_id,
            "photo" : [url]
    }
    # emitting the generated images
    await sio.emit("generated_img",data)
    


## ON CONNECTION 
@sio.on("connect")
async def connect(sid, environ):
    print('User:', sid, 'connected')


## ON DISCONNECT
@sio.on("disconnect")
async def disconnect(sid):
    print(sid, 'disconnected')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5050)