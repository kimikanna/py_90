# Дан диаметр окружности d. Найти ее длину {{L = π·d, π = 3.14}}

def get_circle_length(diameter):
    pi = 3.14
    return(pi * diameter)


diameter = float(input("Введите диаметр: "))
print("Длина окружности:", round(get_circle_length(diameter), 2))