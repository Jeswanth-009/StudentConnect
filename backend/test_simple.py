from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="StudentConnect Test API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TestUser(BaseModel):
    name: str
    email: str
    username: str
    password: str
    bio: str = None

@app.get("/")
def read_root():
    return {"message": "Test Backend is running!", "status": "ok"}

@app.post("/api/auth/signup")
def test_signup(user: TestUser):
    return {
        "message": "Test signup successful!",
        "user": {
            "id": "test-123",
            "name": user.name,
            "email": user.email,
            "username": user.username
        }
    }

@app.get("/api/test")
def test_endpoint():
    return {"message": "Test endpoint working", "timestamp": "2025-07-09"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
