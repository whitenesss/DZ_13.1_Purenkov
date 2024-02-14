import json


def file_json():
    '''
    Получаем данные с json файла
    '''
    with open('products.json', encoding='UTF-8') as file:
        data = json.load(file)
        return data
