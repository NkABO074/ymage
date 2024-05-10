import numpy as np
from image_processing_helpers import get_neighboring_pixels, calculate_interpolation_weights, compute_weighted_average

def bicubic_interpolation(original_image, scaling_factor):
    # Calculate dimensions of the upscaled image
    upscaled_height = original_image.height * scaling_factor
    upscaled_width = original_image.width * scaling_factor
    
    # Create an empty array for the upscaled image
    # upscaled_image = np.zeros((upscaled_height, upscaled_width, original_image.channels))
    upscaled_image = np.zeros((upscaled_height, upscaled_width, 3), dtype=np.uint8)
    
    # Iterate through each pixel in the upscaled image
    for y in range(upscaled_height):
        for x in range(upscaled_width):
            # Calculate the corresponding position in the original image
            original_x = x / scaling_factor
            original_y = y / scaling_factor
            
            # Identify neighboring pixels in the original image
            neighbors = get_neighboring_pixels(original_image, original_x, original_y)
            
            # Calculate interpolation weights
            weights = calculate_interpolation_weights(original_x, original_y)
            
            # Compute weighted average of neighboring pixels
            interpolated_pixel = compute_weighted_average(neighbors, weights)
            
            # Assign the interpolated pixel value to the upscaled image
            upscaled_image[y, x] = interpolated_pixel
    
    return upscaled_image

