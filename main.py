products = [
    ["audi", 90, 10],
    ["bmw", 30, 5],
    ["tričko", 1, 20],
]


def print_products():
    for index, product in enumerate(products):
        print(f"{index}. Název produktu: {product[0]}, cena: {product[1]}$, skladem: {product[2]} ks")


def add_product():
    product_name = input("Název produktu: ")
    product_price = input("Cena produktu: ")
    product_quantity = input("Počet kusů na skladě: ")
    products.append([product_name, product_price, product_quantity])
    print("Produkt přidán.")


def search_product():
    query = input("Zadejte hledaný produkt: ")
    results = [product for product in products if query in product[0]]
    if results:
        for product in results:
            print(f"Název: {product[0]}, Cena: {product[1]}$, Skladem: {product[2]} ks")
    else:
        print("Žádný produkt nenalezen.")


def total_price():
    total = sum(int(product[1]) for product in products)
    print(f"Celková cena všech produktů: {total}$")


def min_price():
    min_value = min(int(product[1]) for product in products)
    cheapest = [product for product in products if int(product[1]) == min_value]
    print("Nejlevnější produkty:")
    for product in cheapest:
        print(f"{product[0]} - {product[1]}$, Skladem: {product[2]} ks")


def max_price():
    max_value = max(int(product[1]) for product in products)
    expensive = [product for product in products if int(product[1]) == max_value]
    print("Nejdražší produkty:")
    for product in expensive:
        print(f"{product[0]} - {product[1]}$, Skladem: {product[2]} ks")


def avg_price():
    avg = sum(int(product[1]) for product in products) / len(products)
    print(f"Průměrná cena produktů: {avg:.2f}$")


def edit_product():
    print_products()
    try:
        index = int(input("Zadejte číslo produktu k úpravě: "))
        if 0 <= index < len(products):
            new_name = input("Nový název produktu: ")
            new_price = input("Nová cena: ")
            new_quantity = input("Nový počet kusů na skladě: ")
            products[index] = [new_name, new_price, new_quantity]
            print("Produkt upraven.")
        else:
            print("Neplatná volba.")
    except ValueError:
        print("Neplatný vstup.")


def menu():
    while True:
        print("\nVítej ve skladu")
        print("1. Výpis položek")
        print("2. Přidání položky")
        print("3. Vyhledání produktu")
        print("4. Celková cena produktů")
        print("5. Nejlevnější produkt")
        print("6. Nejdražší produkt")
        print("7. Průměrná cena produktů")
        print("8. Úprava produktu")
        print("9. Konec")

        choice = input("Volba: ")
        if choice == "1":
            print_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            search_product()
        elif choice == "4":
            total_price()
        elif choice == "5":
            min_price()
        elif choice == "6":
            max_price()
        elif choice == "7":
            avg_price()
        elif choice == "8":
            edit_product()
        elif choice == "9":
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba, zkuste znovu.")


menu()
