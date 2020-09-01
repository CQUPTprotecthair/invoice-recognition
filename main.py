# encoding: utf-8
import cv2
import numpy as np
import roi_merge as roi_
import util_funs as util
from get_rects import *
import pytesseract
from PIL import Image


def main(img):
    region = get_rects(img)
    roi_solve = roi_.Roi_solve(region)
    roi_solve.rm_inside()
    roi_solve.rm_overlop()
    region = roi_solve.merge_roi()
    region = util.sort_region(region)
    region = util.get_targetRoi(region)
    for i in range(2):
        rect2 = region[i]
        w1, w2 = rect2[0], rect2[0] + rect2[2]
        h1, h2 = rect2[1], rect2[1] + rect2[3]
        box = [[w1, h2], [w1, h1], [w2, h1], [w2, h2]]
        cv2.drawContours(img, np.array([box]), 0, (0, 255, 0), 1)
        if i == 0:
            # cv2.imwrite('Code.jpg', img[h1:h2, w1:w2])
            code = img[h1:h2, w1:w2]
            code_str = pytesseract.image_to_string(code, lang='chi_sim')
            print("发票代码:", code_str)
        else:
            # cv2.imwrite('Num.jpg', img[h1:h2, w1:w2])
            num = img[h1:h2, w1:w2]
            num_str = pytesseract.image_to_string(num, lang='chi_sim')
            print("发票号码:", num_str)
    cv2.imshow('img', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    img = cv2.imread("5.jpg")
    main(img)
