from PIL import Image


def rotate_image(image_path, degrees):
    img = Image.open(image_path)  # Load the image
    img_rotated = img.rotate(degrees)  # Rotate the image
    img.show(title='Original Image')  # Display the original and rotated images
    img_rotated.show(title=f'Rotated {degrees} degrees')


# Usage:
rotate_image("images/image1.jpg", degrees=45)
rotate_image("images/image1.jpg", degrees=90)
