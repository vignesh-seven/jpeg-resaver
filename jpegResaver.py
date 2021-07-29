import sys
import os

def parse_my_args(argv=None):
  PARSER = argparse.ArgumentParser()
  PARSER.add_argument("--path")
  return PARSER.parse_args(argv)

def main(*img_inputs):
  from PIL import Image, ImageFilter
  print("imported PIL")
  
  for img_input in img_inputs:
    # Read image
    im = Image.open( img_input ).convert('RGBA')
      
    # New name for file
    new_name = os.path.splitext("sample.txt")[0]
    
    # make a new background
    background = Image.new('RGBA', im.size, (255,255,255))

    # composite the image on the background
    alpha_composite = Image.alpha_composite(background, im)

    # convert the image back to RGB
    final_image = alpha_composite.convert('RGB')

    # save the composite as a jpg
    final_image.save(img_input + '_resave.jpg', 'JPEG')


if __name__ == "__main__":
   args = parse_my_args()
   main(args.path)
