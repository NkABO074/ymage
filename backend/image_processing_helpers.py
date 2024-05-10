from PIL import Image
import numpy as np

def get_neighboring_pixels(image, x, y):
    """
    Extract a 4x4 pixel neighborhood centered around the specified position in the image.
    
    Parameters:
        image (PIL.Image.Image): The input image.
        x (float): The x-coordinate of the target pixel.
        y (float): The y-coordinate of the target pixel.
        
    Returns:
        list: A list of neighboring pixels (as tuples containing RGB values).
    """
    # Calculate the integer coordinates of the top-left corner of the 4x4 neighborhood
    x0 = int(x) - 1
    y0 = int(y) - 1
    
    # Extract the 4x4 pixel neighborhood
    neighborhood = []
    for j in range(4):
        for i in range(4):
            # Handle boundary cases by clamping coordinates to image boundaries
            px = max(0, min(image.width - 1, x0 + i))
            py = max(0, min(image.height - 1, y0 + j))
            neighborhood.append(image.getpixel((px, py)))
    
    return neighborhood


def calculate_interpolation_weights(x, y):
    """
    Calculate interpolation weights for bicubic interpolation.
    
    Parameters:
        x (float): The x-coordinate of the target pixel.
        y (float): The y-coordinate of the target pixel.
        
    Returns:
        numpy.ndarray: A 4x4 matrix of interpolation weights.
    """
    # Cubic spline coefficients
    a = -0.5
    
    # Distance weights
    dx = [((1.5 - abs(x - i)) ** 3) if abs(x - i) <= 1.5 else 0 for i in range(int(x) - 1, int(x) + 3)]
    dy = [((1.5 - abs(y - i)) ** 3) if abs(y - i) <= 1.5 else 0 for i in range(int(y) - 1, int(y) + 3)]
    
    # Calculate interpolation weights
    weights = np.outer(dx, dy)
    
    return weights


def compute_weighted_average(neighborhood, weights):
    """
    Compute the weighted average of neighboring pixels using interpolation weights.
    
    Parameters:
        neighborhood (list): A list of neighboring pixels (as tuples containing RGB values).
        weights (numpy.ndarray): A 4x4 matrix of interpolation weights.
        
    Returns:
        tuple: The weighted average pixel value (as a tuple containing RGB values).
    """
    # Convert the neighborhood list to a NumPy array for element-wise multiplication
    neighborhood_array = np.array(neighborhood)

    # Reshape the weights array to match the shape of the neighborhood array
    weights_reshaped = weights.reshape(-1, 1)

    # Compute the weighted sum of neighboring pixels
    weighted_sum = np.sum(neighborhood_array * weights_reshaped, axis=0)

    # Normalize the sum by dividing by the total weight
    total_weight = np.sum(weights)
    weighted_average = weighted_sum / total_weight

    # Ensure that the pixel values are within the valid range [0, 255]
    weighted_average = np.clip(weighted_average, 0, 255)

    # Round the pixel values to integers
    weighted_average = np.round(weighted_average).astype(np.uint8)

    return tuple(weighted_average)