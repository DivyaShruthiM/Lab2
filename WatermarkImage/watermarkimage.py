from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, output_image_path, watermark_text):
    image = Image.open(input_image_path)
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", 50)
    text_width = draw.textlength(watermark_text, font)
    width, height = image.size
    x = (width - text_width) // 2
    y = (height - 50) // 2

    #add watermark to the image
    draw.text((x, y), watermark_text,font=font, stroke_fill='red',fill=255)

    image.save(output_image_path)

input_image_path = "C:\\Users\\divya\\OneDrive\\Documents\\Cloud Development and Operations\\2nd sem\\Serverless Applications\\grayscale_image.jpg"
output_image_path = "C:\\Users\\divya\\OneDrive\\Documents\\Cloud Development and Operations\\2nd sem\\Serverless Applications\\output_image_with_watermark.jpg"
watermark_text = "Watermark"
add_watermark(input_image_path, output_image_path, watermark_text)
