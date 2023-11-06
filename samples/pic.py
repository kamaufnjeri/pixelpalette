from PIL import Image
import os

def compress_image(input_path, output_path, target_size_bytes):
    image = Image.open(input_path)

    # Set the desired quality (between 1 and 95).
    quality = 95  # You can adjust this value as needed.

    # Make sure the output file exists before trying to check its size
    if not os.path.exists(output_path):
        image.save(output_path, "JPEG", quality=quality)

    while os.path.getsize(output_path) > target_size_bytes and quality > 1:
        quality -= 5
        image.save(output_path, "JPEG", quality=quality)

if __name__ == "__main__":
    input_image_path = "image.jpg"  # Replace with your input image file path
    output_image_path = "compressed_image.jpg"  # Replace with the desired output file path
    target_file_size = 5 * 1024 * 1024  # 5MB in bytes

    compress_image(input_image_path, output_image_path, target_file_size)
