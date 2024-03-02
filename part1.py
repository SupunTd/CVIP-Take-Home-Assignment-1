from PIL import Image
import numpy as np


def reduce_intensity_levels(image_path, desired_levels):
    # Open the image
    img = Image.open(image_path)

    # Convert image to grayscale
    img_gray = img.convert('L')

    # Convert the image to a NumPy array
    img_array = np.array(img_gray)

    # Calculate the factor to reduce intensity levels
    factor = 256 // desired_levels

    # Apply intensity reduction
    img_reduced = (img_array // factor) * factor

    # Create a new image from the modified array
    img_result = Image.fromarray(img_reduced)

    # Save or display the result
    img_result.show()


# Example usage:
reduce_intensity_levels("images/image1.jpg", desired_levels=2)
