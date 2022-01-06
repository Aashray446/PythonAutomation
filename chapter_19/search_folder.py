import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('E:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not (filename.lower().endswith('.jpg') or filename.lower().endswith('.png')):
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        try:
            im = Image.open(os.path.join(foldername, filename))
            width, height = im.size
        except:
            pass
        # Check if width & height are larger than 500.
        if height > 500 and width > 500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numPhotoFiles>numNonPhotoFiles:
        print(os.path.abspath(foldername))