import cloudinary
from cloudinary import uploader
import os
from dotenv import load_dotenv
import PIL
from PIL import Image
import io
import uuid
import logging

load_dotenv()


class Methods:
    """Save an image to cloudinary after compressing its size in bytes"""
    def image_upload(self, image):
        cloudinary.config(
            cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
            api_key=os.getenv("CLOUDINARY_API_KEY"),
            api_secret=os.getenv("CLOUDINARY_API_SECRET"),
            secure=True
        )

        img = Image.open(image)

        if img.mode == 'RGBA':
            img = img.convert('RGB')

        max_size_bytes = 5 * 1024 * 1024

        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format='JPEG')
        img_byte_array.seek(0)

        try:
            if img_byte_array.tell() <= max_size_bytes:
                upload_result = uploader.upload(
                    img_byte_array,
                    folder='my_pics',
                    public_id=str(uuid.uuid4()),
                    transformation=[
                        {"width": 400, "height": 600, "crop": "fill"}
                    ]
                )
                return upload_result['secure_url']
            else:
                unique_filename = str(uuid.uuid4()) + '.jpg'
                local_path = f"uploads/my_pics/{unique_filename}"
                img.save(local_path, format='JPEG')
                return local_path
        except Exception as e:
            # Log the error
            logging.error(f"Image upload failed: {str(e)}")
            return "Image upload failed. Please try again."

    """"Get the total value of items on favorite carts"""
    def total_price(self, purchase_items, changed_item=None, purchase_item=None):
        if purchase_items:
            total_price = 0
            for item in purchase_items:
                if changed_item == item or (purchase_item and item == purchase_item):
                    continue
                total_price += float(item.artwork.price) * int(item.quantity)
            return total_price
        return 0


