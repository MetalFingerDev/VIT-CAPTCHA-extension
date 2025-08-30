# test.py


import io
import torch
from PIL import Image
from src.model import solve_captcha


image = Image.open('src/static/image.png')

buffered = io.BytesIO()
image.save(buffered, format="PNG")
image_bytes = buffered.getvalue()

solution = solve_captcha(image_bytes)
print(f"Solution from model: {solution}")

# Solution from model: ZLNQ52
