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
    product_price = input("Název cenu:")
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


def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Vyhledání položky")
    print("4. Celková cena všech položek\n")


    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání polžky:")
        add_product()
        print("")
        menu()

    elif choice == 3:
        print("Vyhledávání položky")
        product_search()


    else:
        print("Zadal jsi špatně!\n")
        menu()




menu()
