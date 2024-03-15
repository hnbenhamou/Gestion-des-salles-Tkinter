from PIL import Image, ImageDraw, ImageFont

# Open the image
im = Image.open('screen.jpg')

# Create an ImageDraw object
draw = ImageDraw.Draw(im)

# Choose a font and font size
font = ImageFont.truetype('arial.ttf', 36)

# Get the size of the watermark text
text_width, text_height = draw.textsize('Watermark', font=font)

# Calculate the x and y position of the watermark text
x = (im.width - text_width) / 2
y = (im.height - text_height) / 2

# Set the text color to white
text_color = (255, 255, 255)

# Add the watermark text to the image
draw.text((x, y), 'Watermark', fill=text_color, font=font)

# Save the watermarked image
im.save('watermarked.jpg')