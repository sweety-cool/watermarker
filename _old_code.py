# Import required Image library
from PIL import Image, ImageDraw, ImageFont

# Create an Image Object from an Image
im = Image.open('image.jpg')
width, height = im.size

draw = ImageDraw.Draw(im)
text = "© Sweety"

fontSize = round(min(width, height) * 0.1)
font = ImageFont.truetype('font.ttf', fontSize)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 20
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)

# Save watermarked image
im.save('watermark.jpg')
