import file_handler

# 1. lista létrehozása a kulcsoknak 
# 2. iterálás az eredeti kulcsokon 
# 3. csak a Sales stringet tartalmazó kulcsok összegyűjtése 
# 4. az új lista felhasználásával a fájlból beolvasott listában lévő értékek módosítása 
# 5. egy új módosított lista létrehozása 

def get_sales_keys(list_of_dicts):
    tuple_of_keys = tuple(list_of_dicts[0].keys())
    sales_keys = []
    for key in tuple_of_keys:
        if 'Sales' in key:
            sales_keys.append(key)
    return sales_keys


def modify_sales_numbers(list_of_dicts):
    sales_keys = get_sales_keys(list_of_dicts)
    modified_list = []
    for data_dict in list_of_dicts:
        for key in sales_keys:
            data_dict[key] = float(data_dict[key])
        modified_list.append(data_dict)
    return tuple(modified_list)


video_game_sales = modify_sales_numbers(file_handler.get_dicts_from_csv('vg_sales.csv'))
sales_keys = get_sales_keys(video_game_sales)