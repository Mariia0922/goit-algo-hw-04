from cats_info import cats

def get_cats_info(path):
    return cats

cats_info = get_cats_info('шлях/до/файлу/не/використовується')
for cat in cats_info:
    print(cat)
