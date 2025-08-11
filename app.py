from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory database
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"}
]

# 1. GET all books
@app.route("/api/v1/books", methods=["GET"])
def get_books():
    return jsonify(books), 200

# 2. GET book by ID
@app.route("/api/v1/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

# 3. POST - create new book
@app.route("/api/v1/books", methods=["POST"])
def add_book():
    data = request.get_json()
    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"]
    }
    books.append(new_book)
    return jsonify(new_book), 201

# 4. PUT - replace entire book
@app.route("/api/v1/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    for book in books:
        if book["id"] == book_id:
            book["title"] = data["title"]
            book["author"] = data["author"]
            return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

# 5. PATCH - update part of a book
@app.route("/api/v1/books/<int:book_id>", methods=["PATCH"])
def patch_book(book_id):
    data = request.get_json()
    for book in books:
        if book["id"] == book_id:
            book.update({k: v for k, v in data.items() if k in book})
            return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

# 6. DELETE - remove a book
@app.route("/api/v1/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
