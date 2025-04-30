# 🚀 FastAPI + MongoDB Example

This is a simple FastAPI project that connects to MongoDB using the async `motor` driver. It provides basic CRUD endpoints for managing users.

---

## 📦 Requirements

- Python 3.7+
- MongoDB (local or remote)
- pip

---

## 🔧 Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/fastapi-mongo-example.git
cd fastapi-mongo-example
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows (PowerShell)
# source venv/bin/activate  # On Linux/macOS
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file**

```
MONGO_URL=mongodb://localhost:27017
```

5. **Run the server**

```bash
uvicorn app:app --reload
```

---

## 📂 Project Structure

```
.
├── app.py           # FastAPI app
├── models.py         # Pydantic models
├── db.py             # MongoDB connection
├── .env              # MongoDB URL
├── .gitignore
└── README.md
```

---

## 🔌 API Endpoints

- `GET /users/` – List all users
- `GET /users/{user_id}` – Get user by ID
- `POST /users/` – Create a new user

---

## 📚 Auto-generated Docs

- Swagger: http://localhost:8000/docs  
- ReDoc: http://localhost:8000/redoc

---


