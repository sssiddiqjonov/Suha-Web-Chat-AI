# ProDeveloper Chatbot

A Django-based chatbot application.

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start the server: `python manage.py runserver`

## Security Note

Never commit `SECRET_KEY` or database files. Use environment variables for sensitive data in production.
