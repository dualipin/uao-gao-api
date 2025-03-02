# UAO Backend

## Description

This project is an academic and administrative management system built with Django REST framework. It leverages Django's high-level Python web framework to facilitate rapid development and clean, pragmatic design. The system includes features such as user authentication, course management, student records, and an admin interface, all provided by Django's "batteries-included" philosophy.

## Installation Process

To get the UAO Backend project up and running on your local machine, follow these steps:

1. **Create and activate a virtual environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

2. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Apply the database migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Create a superuser to access the admin interface:**

   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

Now you should have the UAO Backend project running locally.
