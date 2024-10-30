from email.policy import default
from fastapi import FastAPI, Body

app = FastAPI()

books: list[dict[str, str | int]] = [
    {"id": 1, "title": "Great Expectations", "author": "Charles Dickens"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen"},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"id": 6, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 7, "title": "Moby Dick", "author": "Herman Melville"},
    {"id": 8, "title": "War and Peace", "author": "Leo Tolstoy"},
    {"id": 9, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky"},
    {"id": 10, "title": "The Odyssey", "author": "Homer"},
    {"id": 11, "title": "Brave New World", "author": "Aldous Huxley"},
    {"id": 12, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
    {"id": 13, "title": "Jane Eyre", "author": "Charlotte Brontë"},
    {"id": 14, "title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky"},
    {"id": 15, "title": "Wuthering Heights", "author": "Emily Brontë"},
    {"id": 16, "title": "Animal Farm", "author": "George Orwell"},
    {"id": 17, "title": "Les Misérables", "author": "Victor Hugo"},
    {"id": 18, "title": "The Iliad", "author": "Homer"},
    {"id": 19, "title": "Frankenstein", "author": "Mary Shelley"},
    {"id": 20, "title": "The Picture of Dorian Gray", "author": "Oscar Wilde"},
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/books")
async def get_books():
    return books

@app.get("/books/{id}")
async def get_book_by_id(id: int) -> dict[str, str | int]:
    for book in books:
        if book["id"] == id:
            return book

@app.get("/author/{author}")
async def get_books_by_author(author: str) -> list[dict[str, str | int]]:
    fetched_books = []
    for book in books:
        if book["author"].lower() == author.lower():
            fetched_books.append(book)
    return fetched_books
@app.post("/books")
async def create_book(new_book=Body()) -> dict[str, str | int]:
    books.append(new_book)
    return new_book

@app.put("/books/update")
async def update_book(updated_book=Body(())) -> dict[str, str | int]:
    for book in books:
        if book["id"] == updated_book["id"]:
            book["title"] = updated_book["title"]
            book["author"] = updated_book["author"]
            return book


@app.delete("/books/{id}")
async def delete_book_by_id(id: int) -> None:
    for book in books:
        if book["id"] == id:
            books.remove(book)