from app.methods import Methods

methods = Methods()

image_url = methods.image_upload('girl.png')
print(image_url)