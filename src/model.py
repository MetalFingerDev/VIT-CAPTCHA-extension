# src/model.py


import io
import torch
from transformers import VisionEncoderDecoderModel, TrOCRProcessor
from PIL import Image

# Load model and processor
processor = TrOCRProcessor.from_pretrained("anuashok/ocr-captcha-v3")
model = VisionEncoderDecoderModel.from_pretrained("anuashok/ocr-captcha-v3")

def solve_captcha(image_data):
  
  """
  Solves a CAPTCHA from image data using the pre-trained TrOCR model.

  Args:
    image_data (bytes): The raw image data (e.g., from base64 decoding).

  Returns:
    str: The solved CAPTCHA text.
  """
  
  # Load image
  image_stream = io.BytesIO(image_data)

  # Load and preprocess image for display
  image_display = Image.open(image_stream).convert("RGBA")
  # Create white background
  background = Image.new("RGBA", image_display.size, (255, 255, 255))
  combined = Image.alpha_composite(background, image_display).convert("RGB")


  # Prepare image
  pixel_values = processor(combined, return_tensors="pt").pixel_values

  # Generate text
  generated_ids = model.generate(pixel_values) # type: ignore
  generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
  
  return(generated_text)
