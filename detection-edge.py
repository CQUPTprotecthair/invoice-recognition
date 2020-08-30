import cv2

def my_croping(imgpath):
    # 读取图片的路径
    img = cv2.imread(imgpath)
    # 把该图片转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #设置固定级别的阈值应用于矩阵
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # 寻找边缘，返回的contours为边缘数据的集合
    _, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
    # 画出边缘,-1为画出所有的边缘，如果为任意自然数那么为contours的索引,(0,0,255)为颜色，最后的2是线条的粗细，数值越大，线条越粗
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
    # 展示图片
    cv2.imshow("pic", img)
    # 等待，当参数为0时，为无限等待，直到有键盘指令
    cv2.waitKey(0)
