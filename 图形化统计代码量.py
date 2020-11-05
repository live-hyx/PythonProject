# root 表示当前正在访问的文件夹路径
# dirs 表示该文件夹下的子目录名list
# files 表示该文件夹下的文件list
import fnmatch
import os
import sys
import prettytable as pt
import time
from tkinter import *

# 后缀集合
CPP_SUFFIX_SET = {'.h', '.hpp', '.hxx', '.c', '.cpp', '.cc', '.cxx'}#c、c++
PYTHON_SUFFIX_SET = {'.py'}#python
JAVA_SUFFIX_SET = {'.java'}#java
# 全局变量
cpp_lines = 0
python_lines = 0
java_lines = 0

def list_files(path):
    #遍历工程路径path，如果遇到文件则统计其行数，如果遇到目录则进行递归
    filenames = os.listdir(path)
    for f in filenames:
        fpath = os.path.join(path, f)
        if (os.path.isfile(fpath)):
            count_lines(fpath)
        if (os.path.isdir(fpath)):
            list_files(fpath)
def count_lines(fpath):
    #对于文件fpath，计算它的行数，然后根据其后缀将它的行数加到相应的全局变量当中
    global CPP_SUFFIX_SET, PYTHON_SUFFIX_SET, JAVA_SUFFIX_SET
    global cpp_lines, python_lines, java_lines, total_lines
    # 统计行数
    with open(fpath, 'rb') as f:
        cnt = 0
        last_data = '\n'
        while True:
            data = f.read(0x400000)
            if not data:
                break
            cnt += data.count(b'\n')
            last_data = data
        if last_data[-1:] != b'\n':
            cnt += 1
    # 只统计C/C++，Python和Java这三类代码
    suffix = os.path.splitext(fpath)[-1]
    if suffix in CPP_SUFFIX_SET:
        cpp_lines += cnt
    elif suffix in PYTHON_SUFFIX_SET:
        python_lines += cnt
    elif suffix in JAVA_SUFFIX_SET:
        java_lines += cnt
    else:
        pass

def run_c():
     path = str(inp.get())
     list_files(path)
     s=cpp_lines
     txt.insert(END,'\n')
     txt.insert(END,'\n')
     txt.insert(END,"C/C++类代码行数")
     txt.insert(END,'\n')
     txt.insert(END, s)   # 追加显示运算结果
   
def run_p():
     path = str(inp.get())
     list_files(path)
     s=python_lines
     txt.insert(END,'\n')
     txt.insert(END,'\n')
     txt.insert(END,"Python类代码行数")
     txt.insert(END,'\n')
     txt.insert(END, s)   # 追加显示结果
     
def run_j():
     path = str(inp.get())
     list_files(path)
     s=java_lines
     txt.insert(END,'\n')
     txt.insert(END,'\n')
     txt.insert(END,"Java类代码行数")
     txt.insert(END,'\n')
     txt.insert(END, s)   # 追加显示结果

def run_restart():
     txt.delete(1.0, END)
     inp.delete(0, END)  # 清空输入
    
root = Tk()
root.geometry('1000x500')
root.title('代码统计工具')

lb1 = Label(root, text='请输入文件路径')
lb1.place(relx=0.2, rely=0.05, relwidth=0.1, relheight=0.1)
inp = Entry(root)
inp.place(relx=0.2, rely=0.15, relwidth=0.5, relheight=0.1)
lb2 = Label(root, text='请选择代码类型')
lb2.place(relx=0.2, rely=0.25, relwidth=0.1, relheight=0.1)
lb3 = Label(root, text='是否包含空行')
lb3.place(relx=0.2, rely=0.45, relwidth=0.1, relheight=0.1)
lb4 = Label(root, text='是否包含注释')
lb4.place(relx=0.2, rely=0.65, relwidth=0.1, relheight=0.1)

btn_restart = Button(root, text='重置', command=run_restart)
btn_restart.place(relx=0.72, rely=0.15, relwidth=0.1, relheight=0.1)

btn_c = Button(root, text='C/C++', command=run_c)
btn_c.place(relx=0.2, rely=0.35, relwidth=0.1, relheight=0.1)

btn_p = Button(root, text='Python', command=run_p)
btn_p.place(relx=0.4, rely=0.35, relwidth=0.1, relheight=0.1)

btn_j = Button(root, text='Java', command=run_j)
btn_j.place(relx=0.6, rely=0.35, relwidth=0.1, relheight=0.1)

btn_kong = Button(root, text='是', command=run_c)
btn_kong.place(relx=0.2, rely=0.55, relwidth=0.1, relheight=0.1)

btn_kong = Button(root, text='否', command=run_c)
btn_kong.place(relx=0.4, rely=0.55, relwidth=0.1, relheight=0.1)

btn_zhu = Button(root, text='是', command=run_c)
btn_zhu.place(relx=0.2, rely=0.75, relwidth=0.1, relheight=0.1)

btn_zhu = Button(root, text='否', command=run_c)
btn_zhu.place(relx=0.4, rely=0.75, relwidth=0.1, relheight=0.1)
# 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
txt = Text(root)
txt.place(rely=0.5, relx=0.6,relheight=0.35,relwidth=0.22)

root.mainloop()

