# 📚 Library Management API

A simple **Library Management REST API** built using **FastAPI** and **Pydantic** to perform CRUD operations on books.

## 🚀 Features

* ➕ Create a book
* 📖 Get all books
* 🔍 Get a book by ID
* ✏️ Update a book
* 🗑️ Delete a book
* 📑 Swagger API documentation

## 🛠️ Technologies

* Python
* FastAPI
* Pydantic
* Uvicorn

## 📁 Project Structure

```text
Library-Management-API/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

## ▶️ Run the API

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## 📖 Swagger UI

Open the following URL to test the API:

```text
http://127.0.0.1:8000/docs
```

## 🔗 API Endpoints

| Method | Endpoint           | Description    |
| ------ | ------------------ | -------------- |
| GET    | `/`                | Home           |
| POST   | `/books`           | Add a book     |
| GET    | `/books`           | Get all books  |
| GET    | `/books/{book_id}` | Get book by ID |
| PUT    | `/books/{book_id}` | Update a book  |
| DELETE | `/books/{book_id}` | Delete a book  |

## 💾 Data Storage

The project uses an **in-memory list** to store book data. Data will reset whenever the application is restarted.

## 👨‍💻 Author

**Vijay N**
