from PIL import Image, ImageFilter


img = Image.open('./images/bike.jpg')

# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save('./processed_images/BLUR_pika.png', 'png')
#
# print('done')

# filtered_img = img.convert('L')
# filtered_img.save('./processed_images/test_pika.png', 'png')
#
# print('done')
#
# rotated_img = img.rotate(90)
# rotated_img.save('./processed_images/rotated_pika.png', 'png')
#
# print('done')

# resized_img = img.resize((480, 360))
# resized_img.save('./processed_images/resized_pika.png', 'png')
#
# print('done')


# box = (100,100,400,400)
# croped_img = img.crop(box)
# croped_img.save('./processed_images/croped_pika.png', 'png')


# resized_img = img.resize((400, 400))
# resized_img.save('./processed_images/thumbnail_bike.jpg')

#this does not change the aspect ratio
img.thumbnail((400, 400))
img.save('./processed_images/thumbnail_bike.jpg')

print(img.size)