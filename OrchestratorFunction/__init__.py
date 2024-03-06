# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

from azure.durable_functions import DurableOrchestrationContext, orchestrator
import azure.functions as func
from PIL import Image, ImageDraw, ImageFont



# ResizeImage activity function
def ResizeImage(image_path: str) -> str:
    # Perform image resizing
    output_image_path="C:\\Users\\divya\\OneDrive\\Documents\\Cloud Development and Operations\\2nd sem\\Serverless Applications\\resized_image.jpg"
    original_image = Image.open(image_path)
    new_size=(1024, 768)
    resized_image = original_image.resize(new_size, Image.Resampling.LANCZOS)
    resized_image.save(output_image_path)
    return output_image_path

# GrayscaleImage activity function
def GrayscaleImage(resized_image_path: str) -> str:
    grayscale_image_path="C:\\Users\\divya\\OneDrive\\Documents\\Cloud Development and Operations\\2nd sem\\Serverless Applications\\grayscale_image.jpg"
    image = Image.open(resized_image_path)
    # Converting the image to grayscale
    grayscale_image = image.convert('L')
    grayscale_image.save(grayscale_image_path)
    return grayscale_image_path

# WatermarkImage activity function
def WatermarkImage(grayscale_image_path: str) -> str:
    watermark_text="Watermark"
    watermarked_image_path = "C:\\Users\\divya\\OneDrive\\Documents\\Cloud Development and Operations\\2nd sem\\Serverless Applications\\output_image_with_watermark.jpg"
    image = Image.open(grayscale_image_path)
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", 50)
    text_width = draw.textlength(watermark_text, font)

    width, height = image.size
    x = (width - text_width) // 2
    y = (height - 50) // 2

    #add watermark to the image
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

    image.save(watermarked_image_path)
    return watermarked_image_path

# Orchestrator function
@orchestrator
def orchestrator_function(context: str):
    input_path = "C:\\Users\\divya\\Downloads\\input_image.jpg"

    resized_image = yield context.call_activity('ResizeImage', input_path)

    grayscale_image = yield context.call_activity('GrayscaleImage', resized_image)

    watermarked_image = yield context.call_activity('WatermarkImage', grayscale_image)

    return watermarked_image



main = orchestrator.create(orchestrator_function)