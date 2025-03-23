products = [
    {
        "name": "Audi",
        "price": 50
    },
    {
        "name": "BMW",
        "price": 30,
    }
]


def print_products():
    for product in products:
        print(f"Název produktu2: {product['name']}, cena: {product['price']}Kč")


def add_product():
    product_name = input("Název produktu:")
    product_price = input("Cena prouktu:")
    product2 = {
        'name': product_name,
        'price': product_price
    }

    products.append(product2)

def product_search():
    key = input("Hledaný výrobek: ")

    if len(key) == 0:
        print("Na skladě není žádný výrobek")
        menu()

    query = []
    for product in products:
        if len(key) > len(product['name']):
            continue
        elif key.lower() == product['name'][0:len(key)].lower():
            query.append(product)

    print("Výsledek hledání: ")
    for item in query:
        print(f"{item['name']} - {item['price']} Kč")

def price_sum():
    total = 0
    for product in products:
        total += product['price']
    print(f"Celková cena všeho na skladu je {total} Kč")

def min_prouct():
    min_price = int(products[0]['price'])
    min_products = []

    for product in products:
        price = int(product['price'])

        if price < min_price:
            min_price = price
            min_products = [product]
        elif price == min_price:
            min_products.append(product)

    print("Nejlevnější produkty jsou: ")
    for product in min_products:
        print(f"{product['name']}, s cenou: {product['price']}Kč")


def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Vyhledání položky")
    print("4. Celková cena všech položek")
    print("5. Zobrazení nejlevnějších položek\n")


    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání položky:")
        add_product()
        print("")
        menu()

    elif choice == 3:
        print("Vyhledávání položky:")
        product_search()
        print("")
        menu()

    elif choice == 4:
        print("Celková cena:")
        price_sum()
        print("")
        menu()

    elif choice == 5:
        print("Vyhledání nejlevnějších produktů:")
        min_prouct()
        print("")
        menu()


    else:
        print("Zadal jsi špatně!\n")
        menu()





menu()
