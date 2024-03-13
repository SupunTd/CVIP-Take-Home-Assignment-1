from PIL import Image, ImageFilter


def spatial_average(image_path, neighborhood_size):
    img = Image.open(image_path)  # Load the image
    img_gray = img.convert('L')  # Convert the image to grayscale
    img_avg = img_gray.filter(ImageFilter.BoxBlur(neighborhood_size))  # Apply a simple spatial average filter
    img_gray.show(title='Original Image')  # Display the original and averaged images
    img_avg.show(title=f'Averaged {neighborhood_size}x{neighborhood_size}')


# Usage:
spatial_average("images/image1.jpg", neighborhood_size=3)
spatial_average("images/image1.jpg", neighborhood_size=10)
spatial_average("images/image1.jpg", neighborhood_size=20)
