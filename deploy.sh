# Deployment script for StudentConnect project
# Run this script from the root directory

# Check for required tools
echo "Checking for required tools..."
npm --version || { echo "npm is required. Please install it."; exit 1; }
node --version || { echo "Node.js is required. Please install it."; exit 1; }

# Deploy backend to Vercel
echo "Preparing backend for Vercel deployment..."
cd backend

# Install Vercel CLI if not present
if ! command -v vercel &> /dev/null; then
    echo "Installing Vercel CLI..."
    npm install -g vercel
fi

# Deploy to Vercel
echo "Deploying backend to Vercel..."
echo "Please follow the prompts to complete deployment"
vercel --prod

# Return to root directory
cd ..

# Build and deploy frontend
echo "Preparing frontend for deployment..."
cd frontend

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies..."
    npm install
fi

# Build the project
echo "Building frontend..."
npm run build

# Install Vercel CLI if not already installed (should be from backend deployment)
if ! command -v vercel &> /dev/null; then
    echo "Installing Vercel CLI..."
    npm install -g vercel
fi

# Deploy to Vercel
echo "Deploying frontend to Vercel..."
echo "Please follow the prompts to complete deployment"
vercel --prod

echo "Deployment complete! Check the DEPLOYMENT.md file for verification steps."
