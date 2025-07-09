# StudentConnect Deployment Guide

This guide will help you deploy the StudentConnect application to Vercel (both frontend and backend).

## Backend Deployment (Vercel)

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Navigate to the backend directory:
```bash
cd backend
```

3. Log in to Vercel:
```bash
vercel login
```

4. Deploy to Vercel:
```bash
vercel --prod
```

5. During deployment:
   - Set up environment variables in the Vercel dashboard
   - Connect to your GitHub repository (optional)
   - Verify the deployment settings match your vercel.json file

## Frontend Deployment (Vercel)

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Build the frontend:
```bash
npm run build
```

3. Deploy to Vercel:
```bash
vercel --prod
```

4. When prompted:
   - Specify the `build` directory as the deploy path
   - Set up environment variables in the Vercel dashboard
   - Ensure the REACT_APP_API_URL points to your Vercel backend API

## Environment Variables

### Backend (.env)
```
SECRET_KEY=your-secret-key
MONGODB_URL=your-mongodb-connection-string
DATABASE_NAME=studentconnect_db
CLOUDINARY_CLOUD_NAME=your-cloudinary-name
CLOUDINARY_API_KEY=your-cloudinary-key
CLOUDINARY_API_SECRET=your-cloudinary-secret
GMAIL_USER=your-gmail-address
GMAIL_APP_PASSWORD=your-gmail-app-password
```

### Frontend (Vercel Environment Variables)
```
REACT_APP_API_URL=https://your-backend-vercel-app-name.vercel.app
```

## Verifying the Deployment

1. Test the backend API at: `https://your-backend-vercel-app-name.vercel.app/`
2. Test the frontend at: `https://your-frontend-vercel-app-name.vercel.app/`
3. Ensure CORS settings in the backend allow requests from your frontend domain

## Troubleshooting

- Check Vercel logs for both frontend and backend errors
- Test API endpoints using tools like Postman
- Verify environment variables are set correctly in the Vercel dashboard
- Check CORS configuration if experiencing API connection issues
- For the frontend, ensure that the build process completes successfully before deployment
