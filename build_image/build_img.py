import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import argparse
import os

pos = (0, 0)
color = (0, 0, 0)
textSize = 20

parser = argparse.ArgumentParser()
parser.add_argument(
    "--prefix", type=str, required=True, help="store image data, token data"
)
parser.add_argument(
    "--font_path", type=str, required=True, help="font for text"
)
parser.add_argument(
    "--total_corpus_path", type=str, required=True, help="total plain parallel corpus"
)
parser.add_argument(
    "--l", type=str, required=True, help="src"
)

args = parser.parse_args()
font = args.font_path
prefix_path = args.prefix
total_corpus_path = args.total_corpus_path

def img_generate(l1):
    l1_file = open(total_corpus_path, "r", encoding="utf-8")
    l1_plain_file = open(prefix_path+"/plain."+l1, "w", encoding="utf-8")
    cnt = 0
    rows = 10
    while True:
        l1_text = l1_file.readline()
        if l1_text:
            l1_plain_file.write(l1_text)
            l = len(l1_text)
            imgBGR = np.zeros((32, rows*l), dtype='uint8')
            imgBGR.fill(255)
            if (isinstance(imgBGR, np.ndarray)):  # OpenCV img type
                imgPIL = Image.fromarray(cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB))
            drawPIL = ImageDraw.Draw(imgPIL)
            fontText = ImageFont.truetype(font, textSize, encoding="utf-8")
            drawPIL.text(pos, l1_text, color, font=fontText)
            imgPutText = cv2.cvtColor(np.asarray(imgPIL), cv2.COLOR_RGB2BGR)
            cv2.imwrite(prefix_path+"/image/"+l1+"/"+str(cnt)+"."+l1+".png", imgPutText)
        else:
            break
        cnt += 1
    print(prefix_path+" "+l1+" count: ", cnt)


if __name__ == "__main__":
    l1 = args.l
    if not os.path.exists(prefix_path):
        os.mkdir(prefix_path)
    if not os.path.exists(prefix_path+"/image"):
        os.mkdir(prefix_path+"/image")
    if not os.path.exists(prefix_path+"/image/"+l1):
        os.mkdir(prefix_path+"/image/"+l1)
    img_generate(l1)
