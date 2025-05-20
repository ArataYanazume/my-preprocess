"""
FastAPI Backend
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from functions.gate import xor_gate

app = FastAPI()

origins = [
    "http://localhost:3000",
]

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def func_hello():
    """ Hello World """
    return {"message": "Hello World"}

@app.get("/api/xor_gate")
async def func_xor_gate(a: float, b: float):
    """ XOR回路 """
    return {"result": xor_gate(a, b)}
