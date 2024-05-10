from image_processing import bicubic_interpolation
from file_processing import load_image, save_image

# Load the original image
original_image = load_image("input.jpg")

# Define the scaling factor
scaling_factor = 2

# Perform bicubic interpolation for upscaling
upscaled_image = bicubic_interpolation(original_image, scaling_factor)

# Save or display the upscaled image
save_image(upscaled_image, "output.jpg")