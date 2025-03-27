import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#8210-8219
PORT=8212

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

rooms = {
    101: {"room No.": 101, "type": "single", "status": "available"},
    102: {"room No.": 102, "type": "double", "status": "occupied"},
    103: {"room No.": 103, "type": "single", "status": "available"},
    104: {"room No.": 104, "type": "single", "status": "available"},
    105: {"room No.": 105, "type": "double", "status": "occupied"},
    106: {"room No.": 106, "type": "single", "status": "available"},
    107: {"room No.": 107, "type": "single", "status": "available"},
    208: {"room No.": 208, "type": "double", "status": "occupied"},
    209: {"room No.": 209, "type": "single", "status": "available"},
    210: {"room No.": 210, "type": "single", "status": "available"},
    211: {"room No.": 211, "type": "double", "status": "occupied"},
    301: {"room No.": 301, "type": "suite", "status": "available"},
    303: {"room No.": 303, "type": "suite", "status": "available"},
    305: {"room No.": 305, "type": "suite", "status": "available"},
    307: {"room No.": 307, "type": "suite", "status": "available"},
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