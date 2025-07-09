# Railway.app Deployment Guide - Step by Step

## IMPORTANT: Fix for "cd backend && pip install" Error

**Updated Fix - Exit Code 127:**
1. The backend files have been copied to the root directory
2. Railway now installs from `requirements.txt` in root
3. The start command runs `uvicorn main:app` directly from root

If you get an error about Railway detecting Node.js instead of Python:
1. The empty `package.json` file has been removed
2. A `nixpacks.toml` file has been created to force Python detection
3. The `railway.json` file has been moved to the root directory

## Step 1: Prepare Your Backend

1. Make sure all your environment variables are ready:
   - `SECRET_KEY` (any random string)
   - `MONGODB_URL` (your MongoDB connection string)
   - `DATABASE_NAME` (your database name)
   - `CLOUDINARY_CLOUD_NAME`
   - `CLOUDINARY_API_KEY`
   - `CLOUDINARY_API_SECRET`
   - `GMAIL_USER` (optional, for emails)
   - `GMAIL_APP_PASSWORD` (optional, for emails)

## Step 2: Deploy to Railway

1. Go to https://railway.app
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Railway will auto-detect it's a Python app
6. Wait for it to build (this might take a few minutes)

## Step 3: Add Environment Variables

1. In Railway dashboard, go to your project
2. Click on "Variables" tab
3. Add all the environment variables listed above
4. Click "Deploy" to redeploy with new variables

## Step 4: Get Your URL

Railway will give you a URL like: `https://your-app-name.railway.app`

## Step 5: Update Frontend

Update your frontend's API URL to point to the new Railway URL.

## Common Issues and Solutions

### "cd backend && pip install" fails with exit code 127
**Cause:** Railway can't find the backend directory or has path issues
**Solution:** 
- Copied all backend files to root directory
- Updated nixpacks.toml to install from root requirements.txt
- Simplified start command to run from root

### "Nixpacks build failed - No start command could be found"
**Cause:** Railway detected Node.js instead of Python due to package.json file
**Solution:** 
- Removed empty package.json file
- Added nixpacks.toml to force Python detection
- Moved railway.json to root directory

### Build Failing?
- Check the logs in Railway dashboard
- Make sure all dependencies are in requirements.txt
- Ensure Python version compatibility

### App Not Starting?
- Verify the start command is correct
- Check environment variables are set
- Look at the application logs

### Connection Issues?
- Verify MongoDB URL is correct
- Check CORS settings in main.py
- Ensure all environment variables are properly set
