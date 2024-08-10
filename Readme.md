# Online Restaurant Application

This is a simple Django-based online restaurant application that allows users to browse the menu, place orders, and manage restaurant operations.

## Technologies Used

- **Backend**: Django
- **Database**: SQLite (default)

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtualenv (recommended)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Firdous19/Online_Restuarant.git

cd online-restaurant
```

### 2. Create and Activate a Virtual Environment

```bash
py -m venv myvenv
source myvenv/Scripts/activate  # On Windows, use `.myvenv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Set Up the Database

Run the following command to apply migrations and set up the SQLite database:

```bash
python manage.py migrate
```

### 5. Create a Superuser

Create an admin account to manage the application:

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000` to see the application running.

Thanks ❤️