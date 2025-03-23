from random import choice

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
    product_price = input("Cena produktu:")
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

def max_product():
    max_price = int(products[0]['price'])
    max_products = []

    for product in products:
        price = int(product['price'])

        if price > max_price:
            max_price = price
            max_products = [product]
        elif price == max_price:
            max_products.append(product)

    print("Nejražší produkty jsou: ")
    for product in max_products:
        print(f"{product['name']}, s cenou: {product['price']}Kč")

def price_average():
    total = 0
    for product in products:
        total += int(product['price'])
    average_price = total / len(products)
    print(f"Průměrná cena všech prouktů je {average_price:.2f} Kč")

def product_numbers():
    print("\nSeznam prouktů")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product['name']} s cenou {product['price']} Kč")

def edit_product():
    product_numbers()

    try:
        choice = int(input("\nZadej číslo produktu k upravení: ")) -1

        if 0 <= choice < len(products):
            new_name = input("Zadej nové jméno produktu: ")
            new_price = int(input("Zadej novou cenu produktu: "))

            products[choice]['name'] = new_name
            products[choice]['price'] = int(new_price)

            print("\nProdukt byl nahrazen!")
        else:
            print("Chyba: Špatně zadané číslo")

    except ValueError:
        print("Zadej Prosím platné číslo produktu a cenu!")

def remove_product():
    product_numbers()

    if not products:
        print("Není zde co smazat.")
        return
    try:
        choice = int(input("\nZadej číslo produktu k smazání: ")) - 1

        if 0 <= choice < len(products):
            removed_product = products.pop(choice)
            print(f"Produkt {removed_product['name']} byl nahrazen!")
        else:
            print("Chyba: Špatně zadané číslo")

    except ValueError:
        print("Zadej prosím platné číslo")





def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Vyhledání položky")
    print("4. Celková cena všech položek")
    print("5. Zobrazení nejlevnějších položek")
    print("6. Zobrazení nejražších položek")
    print("7. Zobrazení průměrné ceny všech položek")
    print("8. Úprava produktů")
    print("9. Smazání produktu\n")


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

    elif choice == 6:
        print("Vyhledání nejdražších produktů:")
        max_product()
        print("")
        menu()

    elif choice == 7:
        print("Vyhledání průměru cen: ")
        price_average()
        print("")
        menu()

    elif choice == 8:
        print("Úprava výrobku na skladě:")
        edit_product()
        print("")
        menu()

    elif choice == 9:
        print("Smazání produktu:")
        remove_product()
        print("")
        menu()


    else:
        print("Zadal jsi špatně!\n")
        menu()



menu()
