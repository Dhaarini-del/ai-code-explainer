# Stage 1: Build the React Frontend
FROM node:20-alpine AS frontend-build
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Setup the Backend and Final Image
FROM node:20-alpine
WORKDIR /app

# Install backend dependencies
COPY package*.json ./
RUN npm install --production

# Copy all files (respecting .dockerignore)
COPY . .

# Copy the optimized frontend build from Stage 1
COPY --from=frontend-build /app/frontend/build ./frontend/build

# Set environment variables
ENV NODE_ENV=production
ENV PORT=5000

# Use a non-root user for security
RUN chown -R node:node /app
USER node

EXPOSE 5000

# Add a basic healthcheck
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -qO- http://localhost:5000/ || exit 1

# Start the application. 
# IMPORTANT: If your entry point is not server.js (e.g., index.js), 
# change the filename below.
CMD ["node", "server.js"]