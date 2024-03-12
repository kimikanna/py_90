# Дана длина ребра куба a. Найти объем куба V = a^3
# и площадь его поверхности S = 6·a^2

def get_volume(side):
    return(pow(side, 3))

def get_surface_area(side):
    return(6 * pow(side, 2))


side = float(input("Введите длину ребра куба: "))
print("\nОбъём:", round(get_volume(side), 2))
print("Площадь поверхности:", round(get_surface_area(side), 2))