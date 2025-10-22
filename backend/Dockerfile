# Use Node.js 18 Alpine image
FROM node:18-alpine

# Install pnpm
RUN npm install -g pnpm

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json pnpm-lock.yaml ./

# Install dependencies
RUN pnpm install

# Copy source code
COPY . .

# Expose port
EXPOSE 3000

# Start the application
CMD ["pnpm", "run", "dev"]
