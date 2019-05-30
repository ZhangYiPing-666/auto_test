# excel文件转化成csv
import pandas as pd

file = r'C:\Users\zhangyp\Desktop\增值税纸质发票Excel批量开票模板.xls'
outfile = r'C:\Users\zhangyp\Desktop\test.csv'


def xlsx_to_csv_pd():
    data_xls = pd.read_excel(file, index_col=0)

    data_xls.to_csv(outfile, sep="~", encoding='gbk')


if __name__ == '__main__':
    xlsx_to_csv_pd()
    print("\n转化完成！！！\nCSV文件所处位置：" + str(outfile))
