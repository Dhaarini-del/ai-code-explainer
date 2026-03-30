from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
from database import init_db, save_to_history
from ai_engine import get_ai_explanation

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

# Enable CORS to allow requests from your React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (change this to ["http://localhost:3000"] for stricter security)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    language: str
    code: str

@app.post("/explain")
def explain_code(request: CodeRequest):
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty")

    # Call the AI Engine to get the real explanation
    explanation = get_ai_explanation(request.language, request.code)

    # Save to history database
    try:
        save_to_history(request.language, request.code, explanation)
    except Exception as e:
        print(f"Database error: {e}")

    return {"explanation": explanation}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000))

# Enable CORS to allow requests from your React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (change this to ["http://localhost:3000"] for stricter security)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    language: str
    code: str

@app.post("/explain")
def explain_code(request: CodeRequest):
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty")

    # Call the AI Engine to get the real explanation
    explanation = get_ai_explanation(request.language, request.code)

    # Save to history database
    try:
        save_to_history(request.language, request.code, explanation)
    except Exception as e:
        print(f"Database error: {e}")

    return {"explanation": explanation}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
