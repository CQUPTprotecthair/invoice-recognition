from PyPDF2 import PdfFileWriter,PdfFileReader

def test1(file_path,folder_path,num,end_page,start_page=0):
    """
    :param file_path: pdf文件路径
    :param folder_path: 存放路径
    :param num: 拆分后的pdf存在几个原pdf页数
    :param end_page: 拆分到的最后一页
    :param start_page: 起始的页数，默认为0
    :return:
    """
    # 打开PDF文件
    pdf_file = PdfFileReader(open(file_path, 'rb'))
    # 获取pdf的页数
    pdf_file_num = pdf_file.getNumPages()
    # 如果输入的end_page页数比pdf文件的页数大或者小于等于0，让停止的页数为pdf最大的页数
    if end_page>pdf_file_num or end_page<=0:
        end_page=pdf_file_num
    # 从起始页到最后一页进行遍历
    for i in range(start_page,end_page,num):
        #创建一个PdfFileWriter的对象
        out_put = PdfFileWriter()
        # 给out_put这个对象传num数的页，项目中每个发票都只占了1页，所以num为1，如果发票占据2页，那么num为2
        for k in range(num):
            out_put.addPage(pdf_file.getPage(i))
        # 设置保存的路径
        out_file = folder_path + "\\" + f"{i}.pdf"
        # 把out_put里面的数据写入到文件中
        out_put.write(open(out_file, 'wb'))