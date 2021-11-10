import numpy as np
import pandas as pd
import os

'''
method definition: 本方法用于统计作业提交情况
------------------------------
:param Assignment_num[str]      此次Assignment编号
:param Assignment_root[str]     作业所在的文件夹
:param checklist_path[str]      作业checklist所在
'''
def check(Assignment_num: str, Assignment_root: str, checkList_path: str):
    ## part 1
    df_checkList : pd.DataFrame = pd.read_excel(checkList_path)
    # print(df_checkList['学号'])

    ## part 2
    Assignment = 'Assignment {}'.format(Assignment_num)
    Assignment_path = os.path.join(Assignment_root, Assignment)
    student_checked = []
    for root, dirs, files in os.walk(Assignment_path):
        student_checked = files
    for index in range(len(student_checked)):
        student_checked[index] = str(student_checked[index]).split('-')[0].split('_')[0].split(' ')[0]

    for index, row in df_checkList.iterrows():
        if str(row['学号']) in student_checked:
            # df_checkList[Assignment][index] = '√'
            df_checkList.loc[index,Assignment] = '√'
    df_checkList.to_excel(checkList_path)
    # print(df_checkList)
    # print("---------------")
    # print(student_checked)

    return


if __name__ == '__main__':
    Assibnment_num = '1'
    Assignment_root = r'C:\Users\Lenovo\Desktop\助教-机器学习\作业'
    checkList_path = r'data/checkList.xlsx'
    check(Assibnment_num, Assignment_root, checkList_path)
    print("FINISH")
