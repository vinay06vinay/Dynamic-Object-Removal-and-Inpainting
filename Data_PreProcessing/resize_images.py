from PIL import Image
import os

def resize_images(input_folder, output_folder, target_size):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            # Open the image
            image_path = os.path.join(input_folder, filename)
            img = Image.open(image_path)

            # Resize the image using LANCZOS resampling filter
            resized_img = img.resize(target_size, Image.LANCZOS)

            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, filename)
            resized_img.save(output_path)

if __name__ == "__main__":
    # Set your input and output folders
    input_folder = "customgtf/"
    output_folder = "customgtf1/"

    # Set the target size (width, height)
    # target_size = (432,240)
    target_size = (240,432)

    # Resize images
    resize_images(input_folder, output_folder, target_size)
