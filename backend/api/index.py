import sys
import os
from pathlib import Path

# Add the parent directory to the Python path
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

# Load environment variables
from dotenv import load_dotenv
load_dotenv(dotenv_path=parent_dir / '.env')

try:
    # Import the app from main.py
    from main import app
    
    # This is the handler for Vercel
    handler = app
    
    print("✅ Successfully imported app from main.py")
except Exception as e:
    print(f"❌ Import error: {e}")
    # Create a simple fallback app
    from fastapi import FastAPI
    app = FastAPI()
    
    @app.get("/")
    def read_root():
        return {"message": "Fallback app - Error occurred during import", "error": str(e)}
    
    # Set the handler for Vercel
    handler = app

# Export the app for Vercel
# Vercel expects the app to be available at the module level
