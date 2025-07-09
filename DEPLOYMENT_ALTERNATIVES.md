# Railway.app Deployment Guide

## Quick Railway Deployment

1. Go to [railway.app](https://railway.app)
2. Click "Deploy from GitHub repo"
3. Select your repository
4. Railway will auto-detect it's a Python app
5. Set the following environment variables:
   - `SECRET_KEY`
   - `MONGODB_URL`
   - `DATABASE_NAME`
   - `CLOUDINARY_CLOUD_NAME`
   - `CLOUDINARY_API_KEY`
   - `CLOUDINARY_API_SECRET`
   - `GMAIL_USER`
   - `GMAIL_APP_PASSWORD`
6. Deploy!

Railway usually gives you a URL like: `https://your-app-name.railway.app`

## Alternative: Render.com

1. Go to [render.com](https://render.com)
2. Connect your GitHub repository
3. Select "Web Service"
4. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables
6. Deploy!

## If you switch platforms:

Update `frontend/netlify.toml`:
```toml
[build.environment]
  REACT_APP_API_URL = "https://your-new-backend-url.com"
```
