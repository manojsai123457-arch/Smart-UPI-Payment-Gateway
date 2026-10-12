# 💳 Smart UPI Payment Gateway

A RESTful backend application inspired by the Unified Payments Interface (UPI), built using FastAPI and MySQL. The project provides secure user authentication, wallet management, account management, and money transfer functionality through well-designed REST APIs.

---

## 🚀 Features

- User Registration
- Secure Login using JWT Authentication
- Password Hashing with bcrypt
- Wallet Creation
- Deposit Money into Wallet
- Check Wallet Balance
- Bank Account Creation
- View Account Details
- Transfer Money Between Users
- Transaction History
- Interactive API Documentation using Swagger UI

---

## 🛠 Tech Stack

- Python 3.12
- FastAPI
- MySQL
- SQLAlchemy ORM
- JWT Authentication
- Passlib (bcrypt)
- Uvicorn
- Pydantic

---

## 📂 Project Structure

```
Smart-UPI-Payment-System/
│
├── app/
│   ├── api/
│   ├── auth/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone <repository-url>
cd Smart-UPI-Payment-System
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄 Configure Database

1. Create a MySQL database.
2. Update the database URL in your configuration.
3. Start the application.

---

## ▶️ Run the Project

```bash
uvicorn app.main:app --reload
```

Application:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /register | Register User |
| POST | /login | Login User |
| POST | /wallet/create/{user_id} | Create Wallet |
| POST | /wallet/deposit/{user_id} | Deposit Money |
| GET | /wallet/balance/{user_id} | Check Wallet Balance |
| POST | /account/create/{user_id} | Create Account |
| GET | /account/{user_id} | Get Account Details |
| POST | /transfer | Transfer Money |
| GET | /transactions/{user_id} | Transaction History |

---

## 🗃 Database Tables

- Users
- Wallets
- Accounts
- Transactions

---

## 🔒 Authentication

The project uses JWT (JSON Web Tokens) for secure authentication and bcrypt for password hashing.

---

## 📖 Future Scope

- UPI PIN Verification
- QR Code Payments
- Email Notifications
- Docker Deployment
- Cloud Deployment

---

## 👨‍💻 Author

**Manoj Sai**

B.Tech, Electronics and Communication Engineering

Indian Institute of Technology Bhubaneswar