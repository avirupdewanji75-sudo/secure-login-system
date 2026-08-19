# 🔐 Secure Login System

A secure **Python Flask web application** for user registration and authentication. The system uses **bcrypt password hashing**, input validation, parameterized SQL queries, and session management to protect user accounts from common security threats.

## 🚀 Features

* User registration
* Secure login authentication
* Password hashing using **bcrypt**
* Input validation
* SQL injection protection
* Session-based authentication
* Secure logout functionality
* Protected dashboard
* SQLite database
* Optional 2FA support can be added

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **SQLite**
* **Flask-Bcrypt**
* **HTML/CSS**

## 📁 Project Structure

```text
Secure-Login-System/
│
├── app.py
├── users.db
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Secure-Login-System.git
cd Secure-Login-System
```

### 2. Install dependencies

```bash
pip install flask flask-bcrypt
```

Or:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 🔑 How It Works

### Registration

1. User enters a username and password.
2. Input is validated.
3. Password is hashed using bcrypt.
4. Only the hashed password is stored in the database.

### Login

1. User enters their credentials.
2. The application retrieves the stored password hash.
3. bcrypt verifies the password.
4. A secure session is created after successful authentication.

### Logout

The user's session is cleared when they log out, preventing further access to protected pages.

## 🛡️ Security Features

| Security Feature      | Purpose                              |
| --------------------- | ------------------------------------ |
| bcrypt hashing        | Protects stored passwords            |
| Input validation      | Prevents invalid input               |
| Parameterized SQL     | Helps prevent SQL injection          |
| Session management    | Protects authenticated pages         |
| Password verification | Prevents plain-text password storage |
| Logout                | Clears authenticated sessions        |

## 📸 Application Flow

```text
Register
   ↓
Validate Input
   ↓
Hash Password
   ↓
Store in Database
   ↓
Login
   ↓
Verify Password
   ↓
Create Session
   ↓
Protected Dashboard
   ↓
Logout
```

## 🔮 Future Improvements

* Add Two-Factor Authentication (2FA)
* Add CSRF protection
* Add login rate limiting
* Implement password reset functionality
* Add email verification
* Use secure cookies
* Add HTTPS support
* Improve password strength requirements

## ⚠️ Disclaimer

This project is intended for **educational purposes** and demonstrates basic secure authentication practices. Additional security controls should be implemented before using it in a production environment.

## 👨‍💻 Author

**Avirup Dewanji**

If you find this project useful, consider giving the repository a ⭐ on GitHub.
