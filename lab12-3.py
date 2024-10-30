import math
def cone_volume(radius, height):
    """Обчислює об'єм прямого конуса."""
    return (1/3) * math.pi * radius**2 * height
def cone_surface_area(radius, height):
    """Обчислює площу поверхні прямого конуса."""
    slant_height = math.sqrt(radius**2 + height**2)
    return math.pi * radius * (radius + slant_height)
radius = float(input("Введіть радіус основи конуса: "))
height = float(input("Введіть висоту конуса: "))
volume = cone_volume(radius, height)
print(f"Об'єм конуса: {volume}")
surface_area = cone_surface_area(radius, height)
print(f"Площа поверхні конуса: {surface_area}")