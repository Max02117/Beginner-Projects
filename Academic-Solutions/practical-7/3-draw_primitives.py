from PIL import Image, ImageDraw

width = 700
height = 700
fill = 'black' 

img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

def to_pixel(x, y):
	scale_x = width / 20
	scale_y = height / 20
	return ((x + 10) * scale_x, height - (y + 10) * scale_y)

star = [(-9, 2), (-3, 3), (0, 8), (3, 3), (9, 2), (5, -3), (6, -9), (0, -7), (-6, -9), (-5, -3), (-9, 2)]
pixel_points = [to_pixel(x, y) for x, y in star]
draw.polygon(pixel_points, fill, outline=fill)

img.save('star.png')