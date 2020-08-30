import cv2
import numpy as np


def xyhw(li):
    n = 10
    tem_li = []
    while n < 30:
        for i in range(len(li)):
            tem_li = [li[i]]
            for k in range(i + 1, len(li)):
                if abs(li[i][1] - li[k][1]) + abs(li[i][2] - li[k][2]) + abs(li[i][3] - li[k][3]) < n:
                    tem_li.append(li[k])
            if len(tem_li) >= 8:
                return tem_li
        n += 1
    else:
        return tem_li


# 将img的高度调整为28，先后对图像进行如下操作：直方图均衡化，形态学，阈值分割
def pre_treat(img):
    height_ = 28
    ratio_ = float(img.shape[1]) / float(img.shape[0])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (int(ratio_ * height_), height_))
    gray = cv2.equalizeHist(gray)
    _, binary = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)
    img_ = 255 - binary  # 反转：文字置为白色，背景置为黑色
    return img_


def get_roi(contours):
    rect_list = []
    for i in range(len(contours)):
        rect = cv2.boundingRect(contours[i])
        if rect[3] > 10:
            rect_list.append(rect)
    return rect_list


def get_rect(img):
    _, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
    rect_list = get_roi(contours)
    rect_list.sort(key=lambda x: x[0], reverse=True)
    rect_list = xyhw(rect_list)

    return rect_list


def change_(img):
    length = 28
    h, w = img.shape
    H = np.float32([[1, 0, (length - w) / 2], [0, 1, (length - h) / 2]])
    img = cv2.warpAffine(img, H, (length, length))
    M = cv2.getRotationMatrix2D((length / 2, length / 2), 0, 26 / float(img.shape[0]))
    return cv2.warpAffine(img, M, (length, length))


def fenge(img_path):
    cont = 0
    img = cv2.imread(img_path)
    img = pre_treat(img)
    contours = get_rect(img)
    folder_path = r"C:\Users\86173\Desktop\jetbrains2019.2\new\tem"
    file_list = []
    # img=cv2.drawContours(img,contours,2,(0, 0, 255),3)
    print("*********************%s*************" % contours)
    for i in range(len(contours)):
        y0 = contours[i][1]
        y1 = contours[i][1] + contours[i][3]
        x0 = contours[i][0]
        x1 = contours[i][0] + contours[i][2]
        print(y0, y1, x0, x1)
        cropImg = img[y0:y1, x0:x1]
        cropImg = change_(cropImg)
        fenge_img = rf"{folder_path}\{cont}.png"
        cv2.imwrite(fenge_img, cropImg)
        cont += 1
        file_list.append(fenge_img)
    return file_list