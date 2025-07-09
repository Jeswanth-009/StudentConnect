import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from .env file in the same directory as main.py
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

app = FastAPI(title="StudentConnect API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Local development
        "https://studentconnect.vercel.app",  # Vercel frontend URL
        "https://studentconnect-frontend.vercel.app",  # Alternative Vercel frontend URL
        "*"  # Allow all for now - restrict in production
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "StudentConnect Backend is running!"}

# Import routes after app creation to avoid circular imports
try:
    # Use relative imports for better Vercel compatibility
    from .routes import auth, posts, comments
    
    # Include routers
    app.include_router(auth.router, prefix="/api")
    app.include_router(posts.router, prefix="/api")
    app.include_router(comments.router, prefix="/api")
except ImportError as e:
    print(f"Warning: Trying absolute imports due to: {e}")
    try:
        # Fallback to absolute imports
        from routes import auth, posts, comments
        
        # Include routers
        app.include_router(auth.router, prefix="/api")
        app.include_router(posts.router, prefix="/api")
        app.include_router(comments.router, prefix="/api")
    except ImportError as e2:
        print(f"Warning: Could not import routes: {e2}")
        
        @app.get("/api/test")
        def test_fallback():
            return {"message": "Routes not loaded, but API is working", "error": str(e2)}

# Export app for Vercel
handler = app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
