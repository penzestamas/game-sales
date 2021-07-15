
# Set létrehozása a platformoknak
# Iterálás a beolvasott listán és a különböző platformok összegyűjtése
# Lista létrehozása, amely a platformokat, és a hozzájuk tartozó listákat fogja tartalmazni, ennek a neve legyen: all_platform_sales
# Set felhasználásával iterálás még egyszer a beolvasott listán
# Lista létrehozása egy platformnak az eladásairól
# Eladások hozzáadása a listához, amelyek az adott platformhoz tartoznak
# Platform neve, és a hozzá tartozó eladások lementése egy dictionarybe
# Dictionary hozzáadása az all_platform_sales-hez

def get_all_platforms(list_of_dicts):
    platforms = set()

    for data_dict in list_of_dicts:
        platforms.add(data_dict['Platform'])

    return platforms
    

def get_gamesales_by_platforms(list_of_dicts):
    platforms = get_all_platforms(list_of_dicts)
    all_platform_sales = []

    for platform in platforms:
        
        platform_sales = []

        for data_dict in list_of_dicts:
            if data_dict['Platform'] == platform:
                platform_sales.append(data_dict)

        all_platform_sales.append({platform: platform_sales})

    return tuple(all_platform_sales)


# Egy nulla értékű változó létrehozása.
# Iterálás az eladásokon, majd az egy területhez tartozó eladások összeadása.
# A létrejött összeg kerekítése két tizedesjegyre.
# Egy dictionary létrehozása az új értékek tárolására.
# Iterálás a platformhoz tartozó eladás listán.
# Iterálás az eladás kulcsokon, majd az egyes területi eladások összegének mentése.

def sum_gamesales_by_territory(sales, territory):
    sum_of_sales = 0

    for game in sales:
        sum_of_sales += game[territory]

    return round(sum_of_sales,2)

def sum_platform_sales(platform_sale_items, sales_keys):
    sum_sales_by_platform = {}

    for platform, sales in platform_sale_items:
        sum_sales_by_platform['Platform'] = platform

        for key in sales_keys:
            sum_sales_by_platform[key] = sum_gamesales_by_territory(sales, key)

    return sum_sales_by_platform

# Egy üres lista létrehozása
# Iterálás a get_gamesales_by_platforms() által kapott listán.
# Új dictionary létrehozása egy platform eladásainak az összegéről.
# A kész dictionary hozzáadása a listához.

def create_platform_sales(platform_sales, sales_keys):
    sum_platform_sales_list = []

    for platform_sale in platform_sales:
        sum_sales_by_platform = sum_platform_sales(platform_sale.items(), sales_keys)
        sum_platform_sales_list.append(sum_sales_by_platform)

    return sum_platform_sales_list