from PIL import Image
import argparse

parser = argparse.ArgumentParser(
                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--image', type=str, default='input',
                    help='input image', metavar="image")
parser.add_argument('--resize', type=float, default=1,
                    help='amount to downscalse', metavar="resize")
parser.add_argument('--invert', type=bool, default=False,
                    help='invert colors', metavar="invert")
parser.add_argument('--write', type=bool, default=False,
                    help='write to output.txt')
parser.add_argument('--chars', type=str, default=".'*#░▒▓█",
                    help='input image', metavar="chars")
parser.add_argument('--single', type=bool, default=False,
                    help='print singe characters', metavar="single")

args = parser.parse_args()

im = Image.open(args.image + ".jpg")
width, height = im.size
im = im.resize((round(width/args.resize), round(height/args.resize)), Image.ANTIALIAS) 
im = im.convert('L')
chars = args.chars
if not args.invert:
	chars = chars[::-1]
width, height = im.size
txt = ""



for y in range(height):
	for x in range(width):
		try:

			print(chars[round(im.getpixel((x, y))/(255/len(chars)))], end="")
			if(not args.single):
				print(chars[round(im.getpixel((x, y))/(255/len(chars)))], end="")
				txt += chars[round(im.getpixel((x, y))/(255/len(chars)))]
			txt += chars[round(im.getpixel((x, y))/(255/len(chars)))]
		except:
			print("█", end="")
			txt += "█"
			if(not args.single):
				print("█", end="")
				txt += "█"
	txt += "\n"
	print()
if args.write:
	with open("output.txt", "w+", encoding='utf-8') as f:
		f.write(txt)
