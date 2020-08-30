import fitz

def my_fitz(pdfPath, imagePath):
    """
    :param pdfPath: pdf的路径
    :param imagePath: 图片文件夹的路径，不是图片路径
    :return:
    """
    # 打开pdf文件
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为2，生成的图像的分辨率会提高，参数也可以自由设置，没有硬性要求
        zoom_x = 2
        zoom_y = 2
        # 这个函数可以理解为，把zoom_x，zoom_y这两个参数保存起来
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        rect = page.rect  # 页面大小
        # mp为截取矩形的左上角坐标
        mp=rect.tr-(500/zoom_x,0)
        # tem为截取矩形的右下角坐标
        tem=rect.tr+(0,200/zoom_y)
        # clip为截取的矩形
        clip = fitz.Rect(mp, tem)
        # 进行图片的截取
        pix = page.getPixmap(matrix=mat, alpha=False,clip=clip)
        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建
        new_img_path = imagePath + '/' + '0.png'
        pix.writePNG(new_img_path)  # 将图片写入指定的文件夹内

        return new_img_path