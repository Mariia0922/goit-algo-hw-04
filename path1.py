# Імпортуємо список cats з модуля cats_info
from cats_info import cats

def get_cats_info(path):
    # Параметр 'path' не використовується, оскільки дані вже завантажені в пам'ять
    return cats

cats_info = get_cats_info('шлях/до/файлу/не/використовується')
for cat in cats_info:
    print(cat)
