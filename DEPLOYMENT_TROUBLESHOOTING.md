# Deployment Troubleshooting Guide

## Common Issues and Solutions

### 1. "Build Failed" Error

**For Railway/Render:**
- Check if all dependencies are in `requirements-deploy.txt`
- Verify Python version compatibility
- Look at build logs for specific error messages

**Solution:**
```bash
# Test locally first
pip install -r requirements-deploy.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 2. "Application Failed to Start"

**Common Causes:**
- Missing environment variables
- Database connection issues
- Port binding problems

**Solutions:**
- Verify all environment variables are set
- Test MongoDB connection string
- Check if app starts locally

### 3. CORS Issues

**Symptoms:**
- Frontend can't connect to backend
- "CORS policy" errors in browser

**Solution:**
Update `main.py` CORS settings with your deployed frontend URL.

### 4. Import Errors

**Symptoms:**
- "ModuleNotFoundError"
- Routes not loading

**Solution:**
- Ensure all files are committed to GitHub
- Check file paths and imports
- Verify requirements.txt includes all dependencies

### 5. Database Connection Issues

**Symptoms:**
- "Connection refused"
- "Authentication failed"

**Solutions:**
- Verify MONGODB_URL is correct
- Check MongoDB Atlas IP whitelist (set to 0.0.0.0/0 for all IPs)
- Ensure database user has proper permissions

## Step-by-Step Debugging

### 1. Test Locally First
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
Visit `http://localhost:8000` - should see "StudentConnect Backend is running!"

### 2. Check Environment Variables
Create `.env` file in backend folder:
```
SECRET_KEY=your-secret-key
MONGODB_URL=your-mongodb-url
DATABASE_NAME=your-db-name
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

### 3. Test API Endpoints
- Visit `http://localhost:8000/docs` for API documentation
- Test basic endpoints first

### 4. Deployment Checklist

Before deploying:
- [ ] App runs locally without errors
- [ ] All environment variables ready
- [ ] Database accessible from internet
- [ ] All files committed to GitHub
- [ ] Requirements.txt up to date

## Platform-Specific Tips

### Railway.app
- Build logs are very detailed
- Environment variables are easy to set
- Usually "just works" with Python apps

### Render.com
- Free tier has some limitations
- May need to simplify build process
- Check service logs for errors

### Vercel
- Works better for simple APIs
- Database connections can be tricky
- Consider serverless limitations

## Getting Help

If you're still stuck:
1. Check the specific platform's documentation
2. Look at build/deployment logs
3. Test each component (database, API, frontend) separately
4. Share specific error messages for better help
