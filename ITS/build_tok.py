from PIL import Image
import numpy as np
from torchvision import transforms
import cv2
import argparse
import os
from multiprocessing import Pool


img_transforms = transforms.Compose([
    transforms.Grayscale(),
    transforms.ToTensor()
])

# 0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  x
# 0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0
img2tok = {
    0.0: "0",
    0.1: "1",
    0.2: "2",
    0.3: "3",
    0.4: "4",
    0.5: "5",
    0.6: "6",
    0.7: "7",
    0.8: "8",
    0.9: "9",
    1.0: "x"
}


def convert_img2tok(img_path, tok_file):
    img = Image.open(img_path)
    img = img_transforms(img)

    h, w = img.shape[1], img.shape[2]

    empty_lines = "x" * 320
    img_str = ""
    for i in range(w):
        for j in range(h):
            img_str += str(img2tok[round(img[0, j, i].item(), 1)])
            if empty_lines in img_str:
                tok_file.write(img_str+"\n")
                return 
    tok_file.write(img_str+"\n")

def main(img_list, tok_file_path):
    f = open(tok_file_path, "w", encoding="utf-8")
    for img in img_list:
        convert_img2tok(img, f)
    f.close()

def multi_workers(l, img_folder, tok_file_path, workers):
    total_img_list = os.listdir(img_folder)
    img_count = len(total_img_list) # imgmfolder/cnt.l.png
    
    def divide_list(lst, n):
        # divide img list to workers
        quotient, remainder = divmod(len(lst), n)
        partitions = []
        start = 0
        for i in range(n):
            length = quotient + (i < remainder)
            partitions.append(lst[start:start+length])
            start += length
        return partitions
    img_partitions = divide_list([i for i in range(img_count)], workers)
    for i in range(workers):
        each_len = len(img_partitions[i])
        for j in range(each_len):
            img_partitions[i][j] = os.path.join(img_folder,str(img_partitions[i][j])+"."+l+".png")
    
    pool = Pool(processes=workers)
    for i in range(workers):
        tok_file_path_worker = tok_file_path+str(i)
        pool.apply_async(main, (img_partitions[i], tok_file_path_worker))
    pool.close()
    pool.join()
    # merge the files 
    
    total_file = open(tok_file_path, "w", encoding="utf-8")
    for i in range(workers):
        tok_file_path_worker = tok_file_path+str(i)
        worker_file = open(tok_file_path_worker, "r", encoding="utf-8")
        tokens = worker_file.read()
        total_file.write(tokens)
        worker_file.close()
        os.remove(tok_file_path_worker)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--l", type=str, required=True)
    parser.add_argument("--img_folder", type=str, required=True)
    parser.add_argument("--tok_path", type=str, required=True)
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()
    l = args.l
    img_folder = args.img_folder
    tok_path = args.tok_path
    workers = args.workers
    multi_workers(l, img_folder, tok_path, workers)
