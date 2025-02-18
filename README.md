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
 Use this example: 

 ```
   SECRET_KEY="django-insecure-hiuvhd5-)#3o1_d=2-z&^+ymvp*u-6kmy8s9^aryovrr0v3$wn"
   DATABASE_URL=postgresql://fredricomosh:Ooy5SuRcn6UQ@ep-crimson-poetry-07648100.us-east-2.aws.neon.tech/tshop?sslmode=require
   DEBUG=True
   AUTH0_DOMAIN=dev-s8xuus8i1y70ysrp.us.auth0.com
   AUTH0_CLIENT_ID=QH9YySC1lNUWfkqu32ztVlPefXJECaCf
   AUTH0_CLIENT_SECRET=L2KADcNXMf6BtTXC2f0hniJoRYWCrnMaJsbJLo0z9LuO5uS1X9Oqfu0IKrMalXuB

   AT_USERNAME=sandbox
   AT_API_KEY=atsk_62851277f7cc8af2c60ebfb36b569763738cb31f164352fbedfa097c6fb921afa0bd1acc
   AT_SENDER_ID=your-sender-id

   API_URL=https://tshop.vercel.app
 ```

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
