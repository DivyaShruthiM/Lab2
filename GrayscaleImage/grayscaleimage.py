from PIL import Image

def convert_to_grayscale(input_image_path, output_image_path):
    image = Image.open(input_image_path)
    
    # Converting the image to grayscale
    grayscale_image = image.convert('L')
    
    grayscale_image.save(output_image_path)

input_image_path = "C:\\Users\\divya\\OneDrive\\Documents\\Cloud Development and Operations\\2nd sem\\Serverless Applications\\resized_image.jpg"
output_image_path = "C:\\Users\\divya\\OneDrive\\Documents\\Cloud Development and Operations\\2nd sem\\Serverless Applications\\grayscale_image.jpg"
convert_to_grayscale(input_image_path, output_image_path)