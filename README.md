# T-Shop API

A Django REST API service for managing customers and orders with SMS notifications.

## Features

- Customer management
- Order processing
- SMS notifications via Africa's Talking
- Authentication via Auth0
- API documentation (Swagger & ReDoc)
- Automated testing and CI/CD
- Vercel deployment support

## Prerequisites

- Python 3.9+
- PostgreSQL
- Auth0 account
- Africa's Talking account

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/t-shop.git
cd t-shop
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file based on `.env.example` and fill in your credentials.

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Auth0 Integration

1. Create an Auth0 account at https://auth0.com

2. Create a new application:
   - Go to Applications > Create Application
   - Choose "Regular Web Application"
   - Note down the Domain, Client ID, and Client Secret

3. Configure Auth0 Application:
   - Allowed Callback URLs: `http://localhost:8000/auth/complete/auth0`
   - Allowed Logout URLs: `http://localhost:8000`

4. Update your `.env` file with Auth0 credentials:
```
AUTH0_DOMAIN=your-domain.auth0.com
AUTH0_CLIENT_ID=your-client-id
AUTH0_CLIENT_SECRET=your-client-secret
```

## Africa's Talking Integration

1