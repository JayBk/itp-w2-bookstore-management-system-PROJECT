def create_bookstore(name):
    return {
        'name': name,
        'last_author_id': 0,
        'last_book_id': 0,
        'books': [],
        'authors': []
    }


def add_author(bookstore, name, nationality):
    bookstore['last_author_id'] += 1
    author = {
        'name': name,
        'nationality': nationality,
        'id': bookstore['last_author_id']
    }
    bookstore['authors'].append(author)

    return author


def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if author['name'] == name:
            return author


def get_author_by_id(bookstore, author_id):
    for author in bookstore['authors']:
        if author['id'] == author_id:
            return author


def add_book(bookstore, title, isbn, author_id):
    bookstore['last_book_id'] += 1
    book = {
        'title': title,
        'isbn': isbn,
        'author_id': author_id,
        'id': bookstore['last_book_id']
    }
    bookstore['books'].append(book)

    return book


def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book['title'] == title:
            return book


def get_book_by_id(bookstore, book_id):
    for book in bookstore['books']:
        if book['id'] == book_id:
            return book


def get_books_by_author(bookstore, author_id):
    books = []
    for book in bookstore['books']:
        if book['author_id'] == author_id:
            books.append(book)

    return books
