import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#8210-8219
PORT=8212

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

rooms = {
    101: {"type": "single", "status": "available"},
    102: {"type": "double", "status": "occupied"},
    103: {"type": "single", "status": "available"},
    104: {"type": "single", "status": "available"},
    105: {"type": "double", "status": "occupied"},
    106: {"type": "single", "status": "available"},
    107: {"type": "single", "status": "available"},
    208: {"type": "double", "status": "occupied"},
    209: {"type": "single", "status": "available"},
    210: {"type": "single", "status": "available"},
    211: {"type": "double", "status": "occupied"},
    301: {"type": "suite", "status": "available"},
    303: {"type": "suite", "status": "available"},
    305: {"type": "suite", "status": "available"},
    307: {"type": "suite", "status": "available"},
}

@app.get("/rooms")
def read_root():
    return {"rooms": rooms}

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=PORT,
        ssl_keyfile="/etc/letsencrypt/privkey.pem",
        ssl_certfile="/etc/letsencrypt/fullchain.pem",
    )