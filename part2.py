from PIL import Image, ImageFilter


def spatial_average(image_path, neighborhood_size):
    # Load the image
    img = Image.open(image_path)

    # Convert the image to grayscale
    img_gray = img.convert('L')

    # Apply a simple spatial average filter
    img_avg = img_gray.filter(ImageFilter.BoxBlur(neighborhood_size))

    # Display the original and averaged images
    img_gray.show(title='Original Image')
    img_avg.show(title=f'Averaged {neighborhood_size}x{neighborhood_size}')


# Example usage:
spatial_average("images/image1.jpg", neighborhood_size=3)
spatial_average("images/image1.jpg", neighborhood_size=10)
spatial_average("images/image1.jpg", neighborhood_size=20)
