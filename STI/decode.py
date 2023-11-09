import cv2
import numpy as np
import argparse
import os


tok2img = {
    "0" : 0.0,
    "1" : 25.5,
    "2" : 51.0,
    "3" : 76.5,
    "4" : 102.0,
    "5" : 127.5,
    "6" : 153.0,
    "7" : 178.5,
    "8" : 204.0,
    "9" : 229.5,
    "x" : 255.0
}


def convert_tok2img(img_str, img_path):
    w = int(len(img_str)/32)
    img1 = np.zeros([3, 32, w])
    for i in range(32):
        for j in range(w):
            img1[0, i, j] = tok2img[img_str[32*j+i]]
            img1[1, i, j] = tok2img[img_str[32*j+i]]
            img1[2, i, j] = tok2img[img_str[32*j+i]]
    cv2.imwrite(img_path, img1.transpose(1, 2, 0))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--stringpath", type=str, required=True
    )
    parser.add_argument(
        "--imgpath", type=str, required=True
    )

    args = parser.parse_args()
    string_path = args.stringpath
    img_path = args.imgpath
    
    if not os.path.exists(img_path):
        os.mkdir(img_path)
    
    f = open(string_path, "r", encoding="utf-8")
    if not os.path.exists(img_path):
        os.mkdir(img_path)
    cnt = 0

    for l in f:
        s = l.strip().replace(" ", "").replace("@@", "")
        img = os.path.join(img_path, str(cnt) + ".png")
        convert_tok2img(s, img)
        cnt += 1
