# EcoMarket - Eco-Friendly Marketplace

## Overview
EcoMarket is an e-commerce platform specialized in eco-friendly and sustainable products. Built with Django, it provides an easy and convenient shopping experience for environmentally conscious users with complete user authentication system.

## Features
- 🛒 Display eco-friendly products
- 👤 User authentication system (Login/Register/Logout)
- 🔐 Secure user accounts with password protection
- 📱 Responsive design supporting all devices
- 🌍 English interface
- 🎨 Modern and attractive design with black, white, and gray color scheme
- 📧 Customer contact form
- 💰 Price display in USD
- ✨ Beautiful login and registration pages

## Technologies Used
- **Backend**: Django 5.2.6
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite
- **Styling**: CSS Grid, Flexbox
- **Fonts**: Google Fonts (Poppins)

## Installation and Setup

### Requirements
- Python 3.12+
- pipenv

### Installation Steps

1. **Clone the project**
```bash
git clone <repository-url>
cd Project_EcoMarket
```

2. **Activate virtual environment**
```bash
cd EcoMarcket/ecomarcket
```

3. **Install requirements**
```bash
pipenv install
```

4. **Run database migrations**
```bash
python manage.py migrate
```

5. **Create a superuser** (optional)
```bash
python manage.py createsuperuser
```

6. **Run the application**
```bash
python manage.py runserver
```

7. **Create sample products** (optional)
```bash
python manage.py create_sample_products
```

## Project Structure
```
Project_EcoMarket/
├── EcoMarcket/
│   ├── ecomarcket/          # Django main settings
│   │   ├── settings.py      # Project settings
│   │   ├── urls.py         # Main URLs
│   │   └── wsgi.py         # WSGI configuration
│   ├── ecomarckets/        # Store application
│   │   ├── models.py       # Data models
│   │   ├── views.py        # Request handlers (home, login, register, logout)
│   │   ├── forms.py        # Django forms (LoginForm, RegisterForm)
│   │   ├── urls.py         # App URLs
│   │   ├── templates/      # HTML templates
│   │   │   ├── home.html   # Home page with authentication
│   │   │   ├── login.html  # Login page
│   │   │   └── register.html # Registration page
│   │   └── management/     # Management commands
│   ├── static/             # Static files
│   │   ├── style/          # CSS files
│   │   ├── js/             # JavaScript files
│   │   └── images/         # Images
│   └── media/              # User files
├── Pipfile                 # Dependency management
└── README.md              # This file
```

## Models

### Product
- `name`: Product name
- `description`: Product description
- `price`: Product price
- `image`: Product image
- `created_at`: Creation date

## Available Pages
- **Home Page** (`/`): Product display and welcome with user authentication
- **Login Page** (`/login/`): User login with secure authentication
- **Register Page** (`/register/`): Create new user accounts
- **Logout** (`/logout/`): Secure user logout
- **Products Section**: Display all eco-friendly products
- **Contact Form**: For customer communication

## User Authentication System

### Login Features
- Secure username and password authentication
- Beautiful login form with modern design
- Error handling for invalid credentials
- Success messages for successful login
- Automatic redirect to home page after login

### Registration Features
- Complete user registration form
- Username, first name, last name, and email fields
- Password confirmation with validation
- Email uniqueness checking
- Automatic redirect to login page after registration
- Form validation with clear error messages

### Security Features
- CSRF protection on all forms
- Password hashing and secure storage
- User session management
- Protected routes with login requirements

## Usage Guide

### For Users
1. **Register**: Visit `/register/` to create a new account
2. **Login**: Visit `/login/` to access your account
3. **Browse Products**: View eco-friendly products on the home page
4. **Logout**: Click logout to securely end your session

### For Administrators
1. **Access Admin**: Visit `/admin/` with superuser credentials
2. **Manage Products**: Add, edit, or delete products
3. **User Management**: View and manage user accounts

## Customization

### Adding New Products
New products can be added through:
1. Django Admin Panel
2. Custom management commands
3. Direct programming

### Design Customization
All CSS files are located in `static/style/style.css` and can be customized as needed. The current design features:
- Black, white, and gray color scheme
- Modern gradient backgrounds
- Responsive design for all devices
- Beautiful form styling for login/register pages

### Authentication Customization
- Modify `forms.py` to add custom validation rules
- Update `views.py` to customize authentication logic
- Edit templates in `templates/ecomarckets/` for UI changes

## Support and Contributing
We welcome contributions to improve the project. Please open an Issue or Pull Request.

## License
This project is open source and available for personal and commercial use.

## Recent Updates

### Version 2.0 - Authentication System
- ✅ Complete user authentication system
- ✅ Beautiful login and registration pages
- ✅ Secure password handling
- ✅ User session management
- ✅ Modern black, white, and gray design
- ✅ Responsive authentication forms
- ✅ Form validation and error handling

---

Developed with ❤️ for environmental sustainability
