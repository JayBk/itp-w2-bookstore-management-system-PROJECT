#
def create_bookstore(name):
    return {'name':name, 'author_id':0, 'authlist':[], 'lebook_id':0, 'booklist':[], 'dabook':[]}

def add_author(bookstore, name, nationality):
    bookstore['author_id']+=1
    author={'name':name, 'nationality':nationality, 'id':bookstore['author_id']}
    bookstore['authlist'].append(author)
    return author


def get_author_by_name(bookstore, name):
    for author in bookstore['authlist']:
        if name==author['name']:
            return author


def get_author_by_id(bookstore, author_id):
    for author in bookstore['authlist']:
        if author_id==author['id']:
            return author


def add_book(bookstore, title, isbn, author_id):
    bookstore['lebook_id']+=1
    books={'title':title, 'isbn':isbn, 'author_id':author_id, 'id':bookstore['lebook_id']}
    bookstore['booklist'].append(books)
    return books

def get_book_by_title(bookstore, title):
    for books in bookstore['booklist']:
        if title==books['title']:
            return books


def get_book_by_id(bookstore, book_id):
    for books in bookstore['booklist']:
        if book_id==books['id']:
            return books


def get_books_by_author(bookstore, author_id):
    for books in bookstore['booklist']:
        if author_id==books['author_id']:
            bookstore['dabook'].append(books)
    return bookstore['dabook']
