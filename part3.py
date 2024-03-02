from PIL import Image


def rotate_image(image_path, degrees):
    # Load the image
    img = Image.open(image_path)

    # Rotate the image
    img_rotated = img.rotate(degrees)

    # Display the original and rotated images
    img.show(title='Original Image')
    img_rotated.show(title=f'Rotated {degrees} degrees')


# Example usage:
rotate_image("images/image1.jpg", degrees=45)
rotate_image("images/image1.jpg", degrees=90)
