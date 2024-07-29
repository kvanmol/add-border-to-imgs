import argparse
from pathlib import Path

# ToDo: Implement some checking, if source and destination directories exist, or work with errorhandling 

parser = argparse.ArgumentParser(prog="add-border-to-imgs",
                                 description='Will add border to images',
                                 epilog="additional description")

parser.add_argument("source_directory",
                    type=str,
                    help='''Path to the source directory of the images.
                    ''')

parser.add_argument("destination_directory",
                    type=str,
                    help='''Path to the destination directory for the images.
                    ''')

parser.add_argument("-s","--size",
                    nargs=2,
                    type=int,
                    default=[1080, 1350],
                    help='''size (width x height) of the image that will be exported.
                    First argument is the width in pixels, and the second argument is the height in pixels.
                    Default size is 1080x1350px
                    '''
                    )

parser.add_argument("-b","--border-size",
                    type=int,
                    default=15,
                    help='''size of the border around the image in pixels
                    default border size is 15px
                    ''')

parser.add_argument("-bfc","--border-fill-color",
                    type=str,
                    default="#FFFFFF",
                    help='''Color used to fill the border, given as a hexadecimal color specifier "#rrggbb" example: #d9d9d9
                    (hex triplet is a six-digit, three-byte hexadecimal number)
                    default fill color is white (#FFFFFF)
                    ''')

args = parser.parse_args()

source_dir = Path(args.source_directory)
destination_dir = Path(args.destination_directory)
img_width = args.size[0]
img_height = args.size[1]
border_size = args.border_size
border_fill_color = args.border_fill_color