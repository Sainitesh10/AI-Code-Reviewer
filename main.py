import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv

# Load env variables
load_dotenv()

from core.reviewer import CodeReviewer

app = FastAPI(title="AI Code Review API")

# Setup CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all for demo purposes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize reviewer
try:
    reviewer = CodeReviewer()
except Exception as e:
    print(f"Warning: Failed to initialize reviewer. Missing API Key? {str(e)}")
    reviewer = None

# Request Model
class ReviewRequest(BaseModel):
    code: str
    language: str

@app.post("/api/review")
async def process_review(request: ReviewRequest):
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty.")
    
    if not reviewer:
        raise HTTPException(status_code=500, detail="AI Reviewer failed to initialize. Check GOOGLE_API_KEY in .env")

    try:
        # Call the existing LangChain logic
        result = reviewer.review_code(request.code, request.language)
        return {"review": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Serve the entire frontend directory as static files (handles index.html automatically)
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
