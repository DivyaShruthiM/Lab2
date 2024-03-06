from PIL import Image

def resize_image(input_image_path, output_image_path, new_size=(1024, 768)):
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize(new_size, Image.Resampling.LANCZOS)
    resized_image.save(output_image_path)

# Example usage
#Provide the path to your input image
input_image_path = "C:\\Users\\divya\\Downloads\\input_image.jpg"
output_image_path = "C:\\Users\\divya\\OneDrive\\Documents\\Cloud Development and Operations\\2nd sem\\Serverless Applications\\resized_image.jpg"# Provide the desired path for the resized image
resize_image(input_image_path, output_image_path)