"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def book():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def toy():
    return Product('toy', 300.00, 'Пони-плюшки', 10)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, book):
        # TODO напишите проверки на метод check_quantity
        assert book.check_quantity(999)
        assert book.check_quantity(1000)
        assert not book.check_quantity(1001)

    def test_product_buy_more_than_available(self, book):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            book.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, cart, book):
        cart.add_product(book)
        assert len(cart.grocery_basket) == 1

    def test_add_2_products(self, cart, book, toy):
        cart.add_product(book)
        cart.add_product(toy)
        assert len(cart.grocery_basket) == 2

    def test_add_5_books(self, cart, book):
        cart.add_product(book, 5)
        assert cart.grocery_basket[book] == 5

    def test_remove_one_item(self, cart, book):
        cart.add_product(book, 15)
        cart.remove_product(book, 1)
        assert cart.grocery_basket[book] == 14

    def test_remove_one_product(self, cart, book):
        cart.add_product(book, 15)
        cart.remove_product(book)
        assert len(cart.grocery_basket) == 0

    def test_remove_more_product_than_have(self, cart, book):
        cart.add_product(book, 15)
        cart.remove_product(book, 16)
        assert len(cart.grocery_basket) == 0

    def test_remove_missing_product(self, cart, book):
        with pytest.raises(KeyError):
            cart.remove_product(book)

    def test_clear(self, cart, book, toy):
        cart.add_product(book, 15)
        cart.add_product(toy)
        cart.clear()
        assert len(cart.grocery_basket) == 0

    def test_total_price(self, cart, book, toy):
        cart.add_product(book, 15)
        cart.add_product(toy)
        assert cart.get_total_price() == 1800.0

    def test_buy(self, cart, book, toy):
        cart.add_product(book, 15)
        cart.add_product(toy)
        cart.buy()
        assert len(cart.grocery_basket) == 0
        assert book.quantity == 985
        assert toy.quantity == 9

    def test_buy_more_than_available(self, cart, book):
        cart.add_product(book, 1001)
        with pytest.raises(ValueError):
            cart.buy()
