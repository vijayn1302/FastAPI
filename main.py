from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Library Management API is running"}

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float
    category: str
    available: bool

books = [
    Book(id = 1, title = "Python Programming", author = "John Smith", price = 450.0, category = "Programming", available = True),
    Book(id = 2, title = "Machine Learning Basics", author = "Alice Brown", price = 600.0, category = "AI", available = True),
    Book(id = 3, title = "Database Management", author = "Robert Johnson", price = 500.0, category = "Database", available = False)
]

# Create Book

@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return {"message": "Book added successfully", "book": book}

# Get all the books

@app.get("/books")
def get_books():
    "Get a list of all books in a library."
    return books

# Get book by id

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return {"message": "Book found", "book": book}

        return {"message": "Book not found"}

# Update Book

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = updated_book
            return {"message": "Book updated successfully", "book": updated_book}

    return {"message": "Book not found"}

# Delete Book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            delete_book = books.pop(index)
            return {"message": "Book deleted successfully", "book": delete_book}

    return {"message": "Book not found"}

