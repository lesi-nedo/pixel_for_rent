# Pixels For Rent

A full-stack application with a Django backend API and Vue.js frontend.

## Project Structure

This project consists of two main components:

- **pixelAPI**: Django backend API
- **pixelsforrent**: Vue.js frontend application

## Setup Instructions

### Backend Setup (pixelAPI)

1. Navigate to the pixelAPI directory:
   ```
   cd pixelAPI
   ```

2. Install dependencies using Pipenv:
   ```
   pipenv install
   pipenv shell
   ```

3. Set up environment variables:
   - Ensure the .env file in configPixel directory is properly configured

4. Run database migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

### Frontend Setup (pixelsforrent)

1. Navigate to the pixelsforrent directory:
   ```
   cd pixelsforrent
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm run serve
   ```

4. For production builds:
   ```
   npm run build
   ```

## Additional Commands

### Backend
- Create superuser: `python manage.py createsuperuser`
- Run tests: `python manage.py test`

### Frontend
- Run unit tests: `npm run test:unit`
- Lint and fix files: `npm run lint`

## Documentation

- Frontend Vue.js configuration: [Configuration Reference](https://cli.vuejs.org/config/)