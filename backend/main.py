from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # per ora accettiamo tutto
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modello per /chat
class ChatRequest(BaseModel):
    message: str

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/chat")
def chat(req: ChatRequest):
    return {"reply": f"Hai detto: {req.message}"}


