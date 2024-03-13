from PIL import Image
import numpy as np


def reduce_intensity_levels(image_path, desired_levels):
    # Open the image , Convert image to grayscale , Convert the image to a NumPy array
    # Calculate the factor to reduce intensity levels
    # Apply intensity reduction ,Create a new image from the modified array

    img = Image.open(image_path)

    img_gray = img.convert('L')
    img_array = np.array(img_gray)
    factor = 256 // desired_levels
    img_reduced = (img_array // factor) * factor
    img_result = Image.fromarray(img_reduced)
    img_result.show()


reduce_intensity_levels("images/image1.jpg", desired_levels=2)
