from PIL import Image, ImageDraw

width = 700
height = 700
fill = 'black'

img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Функция для преобразования математических координат в пиксельные
def to_pixel(x, y):
    scale_x = width / 20 
    scale_y = height / 20 
    return ((x + 10) * scale_x, height - (y + 10) * scale_y)

# Оси
axis_x = [(-10, 0), (10, 0)]
pixel_points = [to_pixel(x, y) for x, y in axis_x]
draw.line(pixel_points, fill, width=3)

axis_y = [(0, 8), (0, -8)]
pixel_points = [to_pixel(x, y) for x, y in axis_y]
draw.line(pixel_points, fill, width=3)


# Линии 
line1 = [(-9,1), (-6,-7), (-1,2), (2,3), (7.2,3)]
pixel_points = [to_pixel(x, y) for x, y in line1]
draw.line(pixel_points, fill, width=5)

line2 = [(7.4, 3.5), (8,3), (8.6,3.5)]
pixel_points = [to_pixel(x, y) for x, y in line2]
draw.line(pixel_points, fill, width=5)

# Полукруг
x, y = 8, 3  # Центр полукруга
radius = 1

# Преобразование в пиксельные координаты
px_center = to_pixel(x, y)
px_radius_x = (width - 100) / 20 * radius  # Радиус по X
px_radius_y = (height - 100) / 20 * radius  # Радиус по Y

# Ограничивающий прямоугольник для дуги
bbox = (
    px_center[0] - px_radius_x,  # Левая
    px_center[1] - px_radius_y,  # Верхняя
    px_center[0] + px_radius_x,  # Правая
    px_center[1] + px_radius_y   # Нижняя
)

# Верхняя половина круга
draw.arc(bbox, start=180, end=0, fill=fill, width=5)

img.save('graph.png')