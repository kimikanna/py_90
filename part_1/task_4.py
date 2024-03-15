# Дан диаметр окружности d. Найти ее длину {{L = π·d, π = 3.14}}

def get_circle_length(diameter):
    pi = 3.14
    circle_length = pi * diameter
    return(round(circle_length, 2))


diameter = float(input("Введите диаметр: "))
print("Длина окружности:", get_circle_length(diameter))