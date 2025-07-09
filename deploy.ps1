# Deployment script for StudentConnect project
# Run this script from the root directory

# Check for required tools
Write-Host "Checking for required tools..." -ForegroundColor Cyan
try {
    npm --version
} catch {
    Write-Host "npm is required. Please install it." -ForegroundColor Red
    exit 1
}

try {
    node --version
} catch {
    Write-Host "Node.js is required. Please install it." -ForegroundColor Red
    exit 1
}

# Deploy backend to Vercel
Write-Host "Preparing backend for Vercel deployment..." -ForegroundColor Cyan
Push-Location -Path "backend"

# Install Vercel CLI if not present
if (-not (Get-Command "vercel" -ErrorAction SilentlyContinue)) {
    Write-Host "Installing Vercel CLI..." -ForegroundColor Yellow
    npm install -g vercel
}

# Deploy to Vercel
Write-Host "Deploying backend to Vercel..." -ForegroundColor Green
Write-Host "Please follow the prompts to complete deployment" -ForegroundColor Yellow
vercel --prod

# Return to root directory
Pop-Location

# Build and deploy frontend
Write-Host "Preparing frontend for deployment..." -ForegroundColor Cyan
Push-Location -Path "frontend"

# Install dependencies if needed
if (-not (Test-Path -Path "node_modules")) {
    Write-Host "Installing frontend dependencies..." -ForegroundColor Yellow
    npm install
}

# Build the project
Write-Host "Building frontend..." -ForegroundColor Green
npm run build

# Vercel CLI should already be installed from backend deployment
if (-not (Get-Command "vercel" -ErrorAction SilentlyContinue)) {
    Write-Host "Installing Vercel CLI..." -ForegroundColor Yellow
    npm install -g vercel
}

# Deploy to Vercel
Write-Host "Deploying frontend to Vercel..." -ForegroundColor Green
Write-Host "Please follow the prompts to complete deployment" -ForegroundColor Yellow
vercel --prod

Write-Host "Deployment complete! Check the DEPLOYMENT.md file for verification steps." -ForegroundColor Cyan
