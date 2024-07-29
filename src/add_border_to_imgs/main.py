from PIL import Image, ImageOps
from pathlib import Path
from add_border_to_imgs.cli import (source_dir, destination_dir,
                                    img_width, img_height,
                                    border_size, border_fill_color)

def run():
    # source_dir, destination_dir, img_width, img_height, border_size, border_fill_color = cli()
    source_files = list(source_dir.iterdir())

    for src_file in source_files:
        if str(src_file.suffix) == ".jpg":
            print('')
            print(f'Processing image: {src_file.name}')

            img = Image.open(src_file)  # open image as an object

            # Image processing
            # ================
            # Returns a resized and padded version of the image, with respect to the given size.
            img = ImageOps.pad(img, (img_width-2*border_size, img_height-2*border_size), color=border_fill_color)
            # Add borders
            img = ImageOps.expand(img, border=border_size, fill=border_fill_color)

            # Save image and delete original 
            # ==============================
            destination_file = destination_dir / src_file.name
            if not destination_file.is_file():
                if destination_dir.is_dir():
                    img.save(destination_file, subsampling=0, quality=100) # Save image with border
                    print(f'succesfully saved image: {destination_file.name}')
                    # src_file.unlink() # Delete original image
                else:
                    print(f'{destination_dir} does not exist')
            else:
                print(f'{src_file.name} already exist')
        else:
            print(f'{src_file.name} is not a .jpg image')

if __name__ == '__main__':
  run()
