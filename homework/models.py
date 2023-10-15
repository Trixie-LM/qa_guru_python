from dataclasses import dataclass


@dataclass
class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        if self.quantity >= quantity:
            return True
        else:
            return False

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity = self.quantity - quantity
        else:
            raise ValueError(f"Недостаточное количество продукта '{self.name}' для покупки")

    def __hash__(self):
        return hash(self.name + self.description)


@dataclass
class Cart:

    def __init__(self):
        # По-умолчанию корзина пустая
        self.grocery_basket = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.grocery_basket:
            self.grocery_basket[product] = self.grocery_basket[product] + buy_count
        else:
            self.grocery_basket[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product in self.grocery_basket:
            if remove_count is None or self.grocery_basket[product] <= remove_count:
                self.grocery_basket.pop(product)
            else:
                self.grocery_basket[product] = self.grocery_basket[product] - remove_count
        else:
            raise KeyError(f"Продукта '{product.name}' нет в корзине")

    def clear(self):
        self.grocery_basket.clear()

    def get_total_price(self) -> float:
        total_price = 0
        for product, quantity in self.grocery_basket.items():
            total_price = total_price + quantity * product.price
        return total_price

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for product, quantity in self.grocery_basket.items():
            product.buy(quantity)
        self.grocery_basket.clear()
