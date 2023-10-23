import cloudinary
from cloudinary import uploader
import os
from dotenv import load_dotenv
import PIL
from PIL import Image
import io
import uuid  # Import the uuid module for generating unique filenames

load_dotenv()


class Methods:
    def image_upload(self, image):
        cloudinary.config(
            cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
            api_key=os.getenv("CLOUDINARY_API_KEY"),
            api_secret=os.getenv("CLOUDINARY_API_SECRET"),
            secure=True
        )
        
        img = Image.open(image)

        # Convert the image to RGB mode if it's in RGBA mode
        if img.mode == 'RGBA':
            img = img.convert('RGB')

        # Set the maximum target file size in bytes (5MB)
        max_size_bytes = 5 * 1024 * 1024

        # Create a byte stream to hold the compressed image
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format='JPEG')

        # Rewind the byte stream to the beginning
        img_byte_array.seek(0)

        # Check if the compressed image is below the target size
        if img_byte_array.tell() <= max_size_bytes:
            # Upload the compressed image to Cloudinary
            try:
                upload_result = uploader.upload(img_byte_array, folder='my_pics', public_id=str(uuid.uuid4()),  # Use a unique filename
                    transformation=[
                        {"width": 400, "height": 600, "crop": "fill"}
                    ]
                )
                return upload_result['secure_url']
            except Exception as cloudinary_error:
                print(f"Cloudinary upload failed: {str(cloudinary_error)}")

        # If Cloudinary upload fails or the image size exceeds the limit, save to local storage with a unique filename
        unique_filename = str(uuid.uuid4()) + '.jpg'  # Unique filename
        local_path = f"uploads/my_pics/{unique_filename}"
        img.save(local_path, format='JPEG')
        return local_path  # Return the local path as the image URL
