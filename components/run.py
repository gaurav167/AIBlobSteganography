import argparse
import cv2

from data_embedder import AISteganography
from frame_manager import FrameManager

parser = argparse.ArgumentParser()
parser.add_argument("--image", "-i", action='store_true', help='Image flag; If turned on, media is treated as an image')
parser.add_argument("--video", "-v", action='store_true', help='Video flag; If turned on, media is treated as a video')
parser.add_argument("--source", "-s", type=str, help='Source of media', required=True)
parser.add_argument("--data", "-d", type=str, help='Data to embed', required=True)
args = parser.parse_args()

key = b'ZAQkxVlI1UyVVcVARrBT0x1eYNc6qDE61oTGlaaEcXQ='

if not(args.image ^ args.video):
	raise "Media can be either an image or a vide. See help : python run.py -h"

if args.video:
	video_handler = AISteganography(args.data, args.source, key)
	""" Hide the data in video and generate new video. """
	video_handler.embedData()
	""" Retrieve data from modified video """
	print("Retrieved Data : ", video_handler.extractData())

elif args.image:
	image = cv2.imread(args.source)
	frame_handler = FrameManager(image, key)
	frame_handler.embed(self.data[0])
