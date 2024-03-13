from PIL import Image


def reduce_resolution(image_path, block_size):

    img = Image.open(image_path) # Load the image
    img_gray = img.convert('L') # Convert the image to grayscale
    width, height = img_gray.size # Get image dimensions
    img_result = img_gray.copy() # Create a copy of the image to modify

    # Iterate over non-overlapping blocks
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            block = img_gray.crop((x, y, x + block_size, y + block_size)) # Get pixels in the current block
            average_pixel = int(sum(block.getdata()) / block_size ** 2) # Calculate the average pixel value
            img_result.paste(Image.new('L', (block_size, block_size), average_pixel), (x, y)) # Replace pixels in the
                                                                                                            # original image with the average value

    img_gray.show(title='Original Image') # Display the original and reduced resolution images
    img_result.show(title=f'Reduced Resolution ({block_size}x{block_size} blocks)')


#usage:
reduce_resolution("images/image1.jpg", block_size=3)
reduce_resolution("images/image1.jpg", block_size=5)
reduce_resolution("images/image1.jpg", block_size=7)
