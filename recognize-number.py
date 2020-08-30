import numpy as np
from os import listdir
from sklearn.neighbors import KNeighborsClassifier as kNN


def np2vector(im):
    returnVect = np.zeros((1, 784))
    for i in range(28):
        # 读一行数据
        lineStr = im[i]
        # 每一行的前28个元素依次添加到returnVect中
        for j in range(28):
            returnVect[0, 28 * i + j] = int(lineStr[j])
    # 返回转换后的1x784向量
    return returnVect


def img2vector(filename):
    # 创建1x784零向量
    returnVect = np.zeros((1, 784))
    # 打开文件
    fr = open(filename)
    # 按行读取
    for i in range(28):
        # 读一行数据
        lineStr = fr.readline()
        # 每一行的前28个元素依次添加到returnVect中
        for j in range(28):
            returnVect[0, 28 * i + j] = int(lineStr[j])
    # 返回转换后的1x784向量
    return returnVect


def handwritingClassTest(im):
    # 测试集的Labels
    hwLabels = []
    # 返回trainingDigits目录下的文件名
    trainingFileList = listdir(r"C:\Users\86173\Desktop\jetbrains2019.2\model_test\txt_folder")
    # 返回文件夹下文件的个数
    m = len(trainingFileList)
    # 初始化训练的Mat矩阵,测试集
    trainingMat = np.zeros((m, 784))
    # 从文件名中解析出训练集的类别
    for i in range(m):
        # 获得文件的名字
        fileNameStr = trainingFileList[i]
        # 获得分类的数字
        classNumber = int(fileNameStr.split('_')[0])
        # 将获得的类别添加到hwLabels中
        hwLabels.append(classNumber)
        trainingMat[i, :] = img2vector(
            r'C:\Users\86173\Desktop\jetbrains2019.2\model_test\txt_folder\%s' % (fileNameStr))
    # 构建kNN分类器
    neigh = kNN(n_neighbors=4, algorithm='auto')
    # 拟合模型, trainingMat为测试矩阵,hwLabels为对应的标签
    neigh.fit(trainingMat, hwLabels)

    vectorUnderTest = np2vector(im)

    classifierResult = neigh.predict(vectorUnderTest)
    return classifierResult