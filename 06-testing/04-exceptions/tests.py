import pytest
from book import Book


@pytest.mark.parametrize("title", [
    "Harry snottter",
    "DrunkenDriving",
    "trojaansehelm"
])
@pytest.mark.parametrize("isbn", [
    '978-1779501127',
    '978-1-77-950112-7',
    '978 1 77 950112 7',
    '9780735611313'
])
def test_valid_creation(title, isbn):
    book = Book(title, isbn)

    assert book.title == title
    assert book.isbn == isbn


@pytest.mark.parametrize("isbn", [
    '978-1779501127',
    '978-1-77-950112-7',
    '978 1 77 950112 7',
    '9780735611313'
])
def test_creation_with_invalid_title(isbn):

    with pytest.raises(RuntimeError):
        Book("", isbn)


@pytest.mark.parametrize("title", [
    "Harry snottter",
    "DrunkenDriving",
    "trojaansehelm"
])
@pytest.mark.parametrize("isbn", [
    '978-177911557',
    '978-1-77-940112-7',
    '016515666515616',
    '97807545945413'
])
def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError):
        Book(title, isbn)
