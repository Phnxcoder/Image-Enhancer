from PIL import Image , ImageFilter

img = Image.open('images/pikachu.jpg')

filtered_img = img.filter(ImageFilter.SHARPEN)

filtered_img.save('sharpened.png','png')