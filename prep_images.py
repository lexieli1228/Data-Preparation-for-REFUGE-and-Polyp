import os
from os import listdir
from os.path import isdir, join
import re
import torch
import numpy as np
from glob import glob
from PIL import Image
import cv2
from torch.utils.data import Dataset
import itertools
from torch.utils.data.sampler import Sampler
import json
import imgaug as ia
import imgaug.augmenters as iaa
from imgaug.augmentables.segmaps import SegmentationMapsOnImage
import warnings
import pdb

def read_list():
    list_file_path = "path of the list of images"
    with open(list_file_path, 'r') as f:
        reference_image_list = f.readlines()
        for i in range(len(reference_image_list)):
            temp = reference_image_list[i]
            reference_image_list[i] = temp.replace('\n', '')

        get_details_list = reference_image_list
        print(get_details_list)
        for i in range(len(get_details_list)):
            print(i)
            get_details_list[i] = reference_image_list[i].replace(',', '_')
            img_idx, img_size, crop_pos_1, crop_pos_2 = get_details_list[i].split("_")
            crop_pos_3 = crop_pos_2.replace('.', '_')
            crop_y, back_lace = crop_pos_3.split("_")
            crop_x = crop_pos_1
            original_path = 'original path' + img_idx
            print(img_idx)
            original_path = original_path + '.jpg'
            reference_image_0 = cv2.imread(original_path, 1)
            file_x, img_number = img_idx.split("/")
            # 现在已经打开了目标图片
            # 准备crop图片
            new_x = int(crop_x) + int(img_size)
            new_y = int(crop_y) + int(img_size)
            crop_result = reference_image_0[int(crop_x):int(new_x), int(crop_y):int(new_y)]
            str_0 = 'path that store the modified results'
            str1 = str_0 + img_number
            str2 = str1 + '_'
            str3 = str2 + img_size
            str4 = str3 + '_'
            str5 = str4 + crop_x
            str6 = str5 + ','
            str7 = str6 + crop_y
            str8 = str7 + '.png'
            print(str8)
            cv2.imwrite(str8, crop_result)

if __name__ == '__main__':
    read_list()

