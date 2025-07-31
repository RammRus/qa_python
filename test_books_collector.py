import pytest
from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_one_amount_book_added(self):
        books_collector = BooksCollector()
        book_name = 'Преступление и наказание'
        assert book_name not in books_collector.get_books_genre()
        books_collector.add_new_book(book_name)
        assert book_name in books_collector.get_books_genre()
#тест на успешное добавление книги в словарь


    def test_set_book_genre_one_book_book_added(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Внутри убийцы')
        books_collector.set_book_genre('Внутри убийцы', 'Детективы')
        assert books_collector.get_books_genre()['Внутри убийцы'] == 'Детективы'
#тест на успешное присвоение жанра новой книги


    def test_get_book_genre_with_valid_genre(self):
        books_collector = BooksCollector()
        book1 = 'Книга_Фантастика_1'
        book2 = 'Книга_Фантастика_2'
    
        for name in [book1, book2]:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, "Фантастика")
    
        result = list(books_collector.get_books_with_specific_genre("Фантастика"))
    
        assert set(result) == {book1, book2}
#тест на вывод книг с определенным жанром


    def test_get_book_genre_for_existing_book(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Идеальный муж')
        books_collector.set_book_genre('Идеальный муж', 'Комедии')
        assert books_collector.get_book_genre('Идеальный муж') == 'Комедии'
#тест на вывод жанра книги по ее имени


    def test_get_books_genre_returns_dictionary(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Кладбище домашних животных')
        books_collector.set_book_genre('Кладбище домашних животных', 'Ужасы')
        books_dictionary = books_collector.get_books_genre()
        assert books_dictionary == {
            'Кладбище домашних животных': 'Ужасы'
        }
#тест на вывод текущего словаря


    def test_get_books_for_children_only(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Король лев')
        books_collector.set_book_genre('Король лев', 'Мультфильмы')
        result = list(books_collector.get_books_for_children())
        assert set(result) == {'Король лев'}
#тест на возвращение детских книг


    def test_add_book_in_favorites_book_added(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Какая-то книга')
        books_collector.add_book_in_favorites('Какая-то книга')
        favorites_books = list(books_collector.get_list_of_favorites_books())
        assert 'Какая-то книга' in favorites_books
#тест на добавление книги в избранное


    def test_get_list_of_favorites_books_empty(self):
        books_collector = BooksCollector()
        favorites_book = list(books_collector.get_list_of_favorites_books())
        assert favorites_book == []
#тест на вывод списка избранных книг