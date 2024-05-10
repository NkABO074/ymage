from PIL import Image
import numpy as np

def load_image(file_path):
    """
    Load an image from the specified file path using Pillow (PIL) library.
    
    Parameters:
        file_path (str): The file path of the image to load.
        
    Returns:
        PIL.Image.Image: The loaded image.
    """
    try:
        image = Image.open(file_path)
        return image
    except Exception as e:
        print(f"Error loading image from {file_path}: {e}")
        return None

def save_image(image, file_path):
    """
    Save an image to the specified file path using Pillow (PIL) library.
    Parameters:
        image (numpy.ndarray): The image to save as a NumPy array.
        file_path (str): The file path where the image will be saved.
    Returns:
        bool: True if the image was saved successfully, False otherwise.
    """
    try:
        # Convert the NumPy array to a PIL Image object
        pil_image = Image.fromarray(image.astype(np.uint8))
        pil_image.save(file_path)
        return True
    except Exception as e:
        print(f"Error saving image to {file_path}: {e}")
        return False


