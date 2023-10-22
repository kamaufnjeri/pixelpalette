def image_upload(path, image_name):
    try:
        with open(image_name, 'wb') as f:
            f.write(path.read())
        return image_name
    except:
        return "Error"

# Open the image file you want to upload
with open('girl.png', 'rb') as image_file:
    result = image_upload(image_file, 'me.png')

print(result)