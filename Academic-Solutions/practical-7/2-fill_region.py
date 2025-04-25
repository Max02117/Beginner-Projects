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
axis_x = [(-8, 0), (8, 0)] 
pixel_points = [to_pixel(x, y) for x, y in axis_x]
draw.line(pixel_points, fill, width=3)

axis_y = [(0, 8), (0, -8)]
pixel_points = [to_pixel(x, y) for x, y in axis_y]
draw.line(pixel_points, fill, width=3)

# Многоугольник с заливкой
polygon = [(0, 4), (0, 6), (6, 0), (6, 0), (2, 0)]
pixel_points = [to_pixel(x, y) for x, y in polygon]
draw.polygon(pixel_points, (0,0,0,100), outline=fill, width=4)

img.save('graph2.png')