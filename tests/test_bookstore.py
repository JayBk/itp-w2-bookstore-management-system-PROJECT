import unittest

from bookstore import *


class BookstoreTestCase(unittest.TestCase):
    def test_create_bookstore(self):
        store = create_bookstore("rmotr's bookstore")
        self.assertEqual(store['name'], "rmotr's bookstore")

    def test_add_get_authors(self):
        store = create_bookstore("rmotr's bookstore")

        poe = add_author(store, 'Edgar Alan Poe', 'US')
        borges = add_author(store, 'Jorge Luis Borges', 'AR')
        joyce = add_author(store, 'James Joyce', 'UK')

        self.assertEqual(poe['name'], 'Edgar Alan Poe')
        self.assertIsNotNone(poe['id'])
        self.assertEqual(poe['nationality'], 'US')

        self.assertEqual(borges['name'], 'Jorge Luis Borges')
        self.assertIsNotNone(borges['id'])
        self.assertEqual(borges['nationality'], 'AR')

        self.assertEqual(joyce['name'], 'James Joyce')
        self.assertIsNotNone(joyce['id'])
        self.assertEqual(joyce['nationality'], 'UK')

        author = get_author_by_name(store, 'James Joyce')
        self.assertEqual(author['id'], joyce['id'])
        self.assertEqual(author['name'], joyce['name'])
        self.assertEqual(author['nationality'], joyce['nationality'])

        author = get_author_by_id(store, poe['id'])
        self.assertEqual(author['id'], poe['id'])
        self.assertEqual(author['name'], poe['name'])
        self.assertEqual(author['nationality'], poe['nationality'])

    def test_add_get_books(self):
        store = create_bookstore("rmotr's bookstore")

        poe = add_author(store, 'Edgar Alan Poe', 'US')
        borges = add_author(store, 'Jorge Luis Borges', 'AR')
        joyce = add_author(store, 'James Joyce', 'UK')

        raven = add_book(store, 'The Raven', 'XXX-1', poe['id'])
        ulysses = add_book(store, 'Ulysses', 'XXX-2', joyce['id'])
        ficciones = add_book(store, 'Ficciones', 'XXX-3', borges['id'])
        aleph = add_book(store, 'El Aleph', 'XXX-4', borges['id'])

        book = get_book_by_title(store, 'The Raven')
        self.assertEqual(book['title'], 'The Raven')
        self.assertEqual(book['isbn'], 'XXX-1')
        self.assertEqual(book['author_id'], poe['id'])

        book = get_book_by_id(store, ulysses['id'])

        self.assertEqual(book['title'], 'Ulysses')
        self.assertEqual(book['isbn'], 'XXX-2')
        self.assertEqual(book['author_id'], joyce['id'])

        books = get_books_by_author(store, borges['id'])
        self.assertEqual(len(books), 2)

        book1 = books[0]
        self.assertEqual(book1['title'], 'Ficciones')
        self.assertEqual(book1['isbn'], 'XXX-3')
        self.assertEqual(book1['author_id'], borges['id'])

        book2 = books[1]
        self.assertEqual(book2['title'], 'El Aleph')
        self.assertEqual(book2['isbn'], 'XXX-4')
        self.assertEqual(book1['author_id'], borges['id'])
