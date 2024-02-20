from asciiartist import asciiartist, display_edges
from PIL import Image

img = Image.open("/home/maxtretikov/Pictures/methuselah.jpeg")

art, edges = asciiartist(
    img, # The image!
    30,  # Number of lines of the output ascii art
    noise_reduction=2,  # Level of noise reduction (optional)
    line_weight=1,      # Weight of the lines to draw (optional)
    text_ratio=2.2      # Height/width ratio of each character (optional)
)

print(art) # `art` is a string u can just print

# v Display the result of edge detection. 
#   Good for finetuning params.
display_edges(edges)
