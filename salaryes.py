# Дані про заробітну плату розробників
salaries_data = """
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
"""

# Функція для отримання даних у вигляді списку рядків
def get_salaries():
    return salaries_data.strip().split('\n')
