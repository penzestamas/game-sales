import file_handler
from platform_sales import platform_sales_list


print(file_handler.write_dicts_to_csv('platform_sales.csv', platform_sales_list))