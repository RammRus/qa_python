# qa_python
Внесены изменения:
1. Изменен тест test_get_book_genre_with_valid_genre
2. Изменен тест test_get_list_of_favorites_books_empty

Пыталась внести фикстуру на создание класса, но тесты выдавали ошибку. Вот как я записала фикстуру:
@pytest.fixture
def books_collector():
    return BooksCollector()