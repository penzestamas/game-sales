import file_handler
import data_conversion
import platform_sales

# test_video_game_sales = file_handler.get_dicts_from_csv('vg_sales.csv')[:3]

test_video_game_sales = data_conversion.modify_sales_numbers(file_handler.get_dicts_from_csv('vg_sales.csv')[:3])
# print(platform_sales.get_all_platforms(test_video_game_sales))
# print(platform_sales.get_gamesales_by_platforms(test_video_game_sales))
print(data_conversion.modify_sales_numbers(test_video_game_sales))
print(platform_sales.get_gamesales_by_platforms(test_video_game_sales)[0].items())
print(platform_sales.sum_gamesales_by_territory(test_video_game_sales, 'Global_Sales'))
# print(platform_sales.get_gamesales_by_platforms(test_video_game_sales)[0].items())
# print(data_conversion.get_sales_keys(test_video_game_sales))
# print(data_conversion.modify_sales_numbers(test_video_game_sales))

# print(test_video_game_sales)
# print(file_handler.write_dicts_to_csv('test_sales.csv', test_video_game_sales))

print(platform_sales.sum_platform_sales(platform_sales.get_gamesales_by_platforms(test_video_game_sales)[0].items(), data_conversion.get_sales_keys(test_video_game_sales)))
print(platform_sales.create_platform_sales(platform_sales.get_gamesales_by_platforms(test_video_game_sales), data_conversion.get_sales_keys(test_video_game_sales))