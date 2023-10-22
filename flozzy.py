import cloudinary
from cloudinary import uploader
import os

cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
    secure=True
)


def image_upload(path):
    upload_result = uploader.upload(path, folder='my_pics', public_id="web_images",
        transformation=[
            {"width": 200, "height": 300, "crop": "fill"}
        ]
    )
    return upload_result

print(image_upload('girl.png'))
