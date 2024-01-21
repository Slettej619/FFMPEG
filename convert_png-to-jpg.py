import os
from PIL import Image

def convert_png_to_jpg(source_dir, target_dir):
    """
    Converts all PNG files in the specified directory to JPG format, with a specific naming convention.

    Args:
    source_dir (str): The directory containing PNG files.
    target_dir (str): The directory where converted JPG files will be saved.

    Returns:
    None
    """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    png_files = [f for f in os.listdir(source_dir) if f.endswith('.png')]
    for i, file_name in enumerate(png_files, start=1):
        with Image.open(os.path.join(source_dir, file_name)) as img:
            rgb_im = img.convert('RGB')
            rgb_im.save(os.path.join(target_dir, f'frame_{i}.jpg'), 'JPEG')

# Example usage
source_directory = 'D:/xxx/xxx/xxx_video_buffer'  # Source directory containing PNG files
target_directory = 'D:/xxx/xxx/new_xxx_video_buffer'  # Target directory for JPG files

convert_png_to_jpg(source_directory, target_directory)
