## Pillow Library

---
The Pillow library in Python is a powerful and easy-to-use tool for image 
processing. It’s a fork of the original PIL (Python Imaging Library) and is 
widely used for tasks like resizing, cropping, filtering, drawing on images,
converting formats, and more.

### Installing Pillow
```
pip install Pillow
```

### Basic Usage Example
```
from PIL import Image

# Open an image
img = Image.open("example.jpg")

# Show the image
img.show()

# Save to a new file
img.save("new_image.png")
```

### Common Features of Pillow

#### 1. Opening and Saving Images
```
img = Image.open("input.jpg")
img.save("output.png")  # Convert format
```

#### 2. Resizing
```
resized = img.resize((200, 200))
resized.show()
```

#### 3. Cropping
```
cropped = img.crop((left, top, right, bottom))
cropped.show()
```

#### 4. Rotating and Flipping
```
rotated = img.rotate(90)         # Rotate 90 degrees
flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
```

#### 5. Convert to Grayscale
```
gray = img.convert("L")
gray.show()
```

#### 6. Draw on Images
```
from PIL import ImageDraw

draw = ImageDraw.Draw(img)
draw.text((10, 10), "Hello", fill="white")

img.show()
```

#### 7. Image Filters (e.g., blur)
```
from PIL import ImageFilter

blurred = img.filter(ImageFilter.BLUR)
blurred.show()
```

#### 8. Getting Image Info
```
print(img.format)  # e.g. JPEG, PNG
print(img.size)    # (width, height)
print(img.mode)    # e.g. RGB, L
```

### Summary
| Feature    | Code Sample                         |
|------------|-------------------------------------|
| Open image | `Image.open("file.jpg")`            |
| Resize     | `.resize((w, h))`                   |
| Convert    | `.convert("L")`                     |
| Crop       | `.crop((left, top, right, bottom))` |
| Filter     | `.filter(ImageFilter.BLUR)`         |
| Draw text  | `ImageDraw.Draw(img).text()`        |

