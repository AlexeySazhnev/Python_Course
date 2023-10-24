"""
У вас есть список словарей, каждый из которых представляет собой запись о продукте.
Вам нужно написать программу, которая спрашивает пользователя,
в каком порядке сортировать (по возрастанию или убыванию цены), и затем сортирует
список products по цене с использованием lambda-функции и выводит отсортированный список на экран.

"""

products = [
{"name": "Шоколад", "price": [2.5, 5.0], "quantity": 100},
{"name": "Молоко", "price": [1.0, 9.0], "quantity": 50},
{"name": "Кофе", "price": [5.0, 12], "quantity": 30},
{"name": "Чай", "price": [3.0, 15], "quantity": 80},
]


# Функция для сортировки списка словарей по цене
def sort_products(products, ascending: bool):
    return sorted(products, key=lambda x: x["price"][1], reverse=ascending)


def main():
# Ввод пользователя: "asc" для сортировки по возрастанию, "desc" - по убыванию
    sort_order = input("Введите порядок сортировки (asc/desc): ").strip().lower()

    if sort_order == "asc":
        sorted_products = sort_products(products, False)
    elif sort_order == "desc":
        sorted_products = sort_products(products, True)
    else:
        print("Неверный порядок сортировки.")
    return 0

    for product in sorted_products:
        print(product)


main()