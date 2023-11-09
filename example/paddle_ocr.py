from paddleocr import PaddleOCR
from argparse import ArgumentParser
import os
import argparse
from tqdm import tqdm

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--img_dir", type=str, required=True
    )
    parser.add_argument(
        "--ocr_result_path", type=str, required=True
    )
    args = parser.parse_args()

    img_dir = args.img_dir
    ocr_result_path = args.ocr_result_path

    len = len(os.listdir(img_dir))
    ocr_result = open(ocr_result_path, "w", encoding="utf-8")
    ocr = PaddleOCR(lang="en")
    for i in tqdm(range(len)):
        img_path = img_dir+"/"+str(i)+".png"
        result = ocr.ocr(img_path, det=False)
        ocr_result.write(result[0][0][0]+"\n")
