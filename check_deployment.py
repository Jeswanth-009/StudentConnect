# Deployment readiness check script
import os
import sys
from pathlib import Path

def check_backend():
    print("\n=== Checking Backend ===")
    
    # Check for required files
    required_files = [
        "main.py",
        "api/index.py",
        "vercel.json",
        "requirements.txt",
    ]
    
    backend_path = Path("backend")
    for file in required_files:
        file_path = backend_path / file
        if file_path.exists():
            print(f"✅ Found {file}")
        else:
            print(f"❌ Missing {file}")
    
    # Check if .env exists
    if (backend_path / ".env").exists():
        print("✅ .env file exists")
    else:
        print("❌ .env file is missing")
        
    # Check Python version
    print("\nPython version:", sys.version)

def check_frontend():
    print("\n=== Checking Frontend ===")
    
    # Check for required files
    required_files = [
        "package.json",
        "vercel.json",
        "src/App.js",
        "public/index.html"
    ]
    
    frontend_path = Path("frontend")
    for file in required_files:
        file_path = frontend_path / file
        if file_path.exists():
            print(f"✅ Found {file}")
        else:
            print(f"❌ Missing {file}")
    
    # Check if build directory exists
    if (frontend_path / "build").exists():
        print("✅ Build directory exists")
    else:
        print("⚠️ Build directory not found - make sure to run 'npm run build'")
    
    # Check environment files
    if (frontend_path / ".env.production").exists():
        print("✅ Production environment file exists")
    else:
        print("⚠️ Production environment file is missing")

if __name__ == "__main__":
    print("=== STUDENTCONNECT DEPLOYMENT READINESS CHECK ===")
    check_backend()
    check_frontend()
    
    print("\n=== DEPLOYMENT RECOMMENDATIONS ===")
    print("1. Make sure MongoDB credentials are correctly set in Vercel environment")
    print("2. Ensure the frontend REACT_APP_API_URL points to your deployed backend")
    print("3. Update CORS settings in backend to allow requests from your frontend domain")
    print("4. Run 'vercel --prod' in both backend and frontend directories to deploy")
    print("\nRefer to DEPLOYMENT.md for detailed instructions.")
