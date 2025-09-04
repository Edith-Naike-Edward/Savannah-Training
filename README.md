# Savannah Training

This is a Django-based web application developed for Savannah Informatics training purposes. It demonstrates basic web development concepts using Django, including models, views, templates, and static files.

## Project Structure
- `savannahtraining/` - Main Django project directory
- `posts/` - Django app for managing posts
- `static/` - Static files (CSS, JS)
- `templates/` - HTML templates
- `db.sqlite3` - SQLite database
- `manage.py` - Django management script

## Setup Instructions
1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   pip install django
   ```
3. **Run migrations**:
   ```bash
   python manage.py migrate
   ```
4. **Start the development server**:
   ```bash
   python manage.py runserver
   ```
5. **Access the app**: Open `http://127.0.0.1:8000/` in your browser.

## Features
- Home and About pages
- Posts app with basic CRUD functionality
- Static files for styling and scripts

## License
This project is for training purposes and does not have a specific license.
