# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 08:54:12 2020

Modified on Mon Oct 19 11:38:49 2020
1.修改数据合并逻辑，解决数据合并时有重叠行问题。


@author: Roy
"""

#用于GUI窗口模块
from tkinter import*
from tkinter.ttk import*
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

#提示任务执行完成
def myMsg():
    messagebox.showinfo('INFO','Finished')


#分割工具打开文件
def openfile():
    #文件路径，文件内容，文本行数
    global filename
    global content
    global count
    filename = askopenfilename()
    if filename == '':
        return
    with open(filename,'r') as fileobj:
        content = fileobj.read()
    count = 0
    for index,line in enumerate(open(filename,'r')):
        pass
        count += 1
    #加入文件路径到entry
    a_entry.delete(0,END)
    a_entry.insert(0,filename)
 
#合并工具打开文件
def openfile2():
    global content2
    global count2
    filename2 = askopenfilename()
    if filename2 == '':
        return
    with open(filename2,'r') as fileobj:
        content2 = fileobj.read()
    count2 = 0
    for index,line in enumerate(open(filename2,'r')):
        pass
        count2 += 1
    e_entry.delete(0,END)
    e_entry.insert(0,filename2)
def openfile3():
    global content3
    global count3
    filename3 = askopenfilename()
    if filename3 == '':
        return
    with open(filename3,'r') as fileobj:
        content3 = fileobj.read()
    count3 = 0
    for index,line in enumerate(open(filename3,'r')):
        pass
        count3 += 1
    e2_entry.delete(0,END)
    e2_entry.insert(0,filename3)

#合并读取出来的两个文件内容
def Merge():
    new_name = e3_entry.get()
    list_content2 = content2.split('\n')
    list_content3 = content3.split('\n')
    new_filename = new_name + 'Merge.txt'
    with open(new_filename,'a') as new_fileobj:
        for i in range(count2):
                # if i != count2-1:
                    new_fileobj.write(list_content2[i])
                    new_fileobj.write('\n')
                # else:
                #     new_fileobj.write(list_content2[i])
        for i in range(count3):
                if i != count3-1:
                    new_fileobj.write(list_content3[i])
                    new_fileobj.write('\n')
                else:
                    new_fileobj.write(list_content3[i])
    myMsg()


#判断是否有头部标注文件，开启分割文件是否用同一个标注
def state_button():
    state2 = var2.get()
    if state2 ==True:
        c_button.config(state = NORMAL)
    else:
        var1.set('False')
        c_button.config(state = DISABLED)
        
        

#数据分割
def Excute():
#读取复选框
    state1 = var1.get()
    state2 = var2.get()
    new_name = b_entry.get()
#取得分割数量
    split_str = c_entry.get()
    split_num = int(split_str)
    #判断是不是有标签页，有标签取得商和余数，有标签行数需要减1
    if state2 ==True:
        split_num_result = divmod(count-1,split_num)
    else:
        split_num_result = divmod(count,split_num)
    if split_num_result[1]==0:
        d2_label_str.set(split_num_result[0])
    else:
        d2_label_str.set(split_num_result[0]+1)
#内容转换列表     
    list_content = content.split('\n')
    label_contet = list_content[0]
    re_list_content = list_content.copy()
    re_list_content.remove(re_list_content[0])
#判断抬头
    if state1 == True:
        for i in range(1,split_num_result[0]+1):
            new_filename = new_name + "split(" + str(i) +').txt'
            with open(new_filename,'a') as new_fileobj:
                new_fileobj.write(label_contet)
                new_fileobj.write('\n')
                for i in range(split_num):
                    if i != split_num-1:
                        new_fileobj.write(re_list_content[i])
                        new_fileobj.write('\n')
                    else:      #如果是最后一行则不写回车行
                        new_fileobj.write(re_list_content[i])
                for i in range(split_num):
                    re_list_content.remove(re_list_content[0])
        if split_num_result[1]!=0:      #如果分割有余数写剩余部分的数据
            new_filename = new_name + "split(" + str(split_num_result[0]+1) +').txt'
            with open(new_filename,'a') as new_fileobj:
                new_fileobj.write(label_contet)
                new_fileobj.write('\n')
                for i in range(split_num_result[1]):
                    if i != split_num_result[1]-1:
                        new_fileobj.write(re_list_content[i])
                        new_fileobj.write('\n')
                    else:
                        new_fileobj.write(re_list_content[i])
                for i in range(split_num_result[1]):
                    re_list_content.remove(re_list_content[0])

            
    else:
        for i in range(1,split_num_result[0]+1):
            new_filename = new_name + "split(" + str(i) +').txt'
            with open(new_filename,'a') as new_fileobj: 
                for i in range(split_num):
                    if i != split_num-1:
                        new_fileobj.write(list_content[i])
                        new_fileobj.write('\n')
                    else:
                        new_fileobj.write(list_content[i])
                for i in range(split_num):
                    list_content.remove(list_content[0])
        if split_num_result[1]!=0:
            new_filename = new_name + "split(" + str(split_num_result[0]+1) +').txt'
            with open(new_filename,'a') as new_fileobj: 
                for i in range(split_num_result[1]):
                    if i != split_num_result[1]-1:
                        new_fileobj.write(list_content[i])
                        new_fileobj.write('\n')
                    else:
                        new_fileobj.write(list_content[i])
                for i in range(split_num_result[1]):
                    list_content.remove(list_content[0])
    myMsg()
        
               


window = Tk()
window.title('Data Processing Tool v1.1')
winWidth = 550
winHeight = 280
# 获取屏幕分辨率
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
 
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
 

# 设置窗口初始位置在屏幕居中
window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))

#a为文件路径，b为储存路径,c为分割数量,d2为分割份数,v2和v1为复选框的值
a_entry_str =StringVar()
b_entry_str =StringVar()
c_entry_str =StringVar()
d2_label_str =StringVar()
var1 =IntVar()
var2 =IntVar()

tabControl = Notebook(window)
tab1 = Frame(tabControl)        # 创建选项卡（tab）分割
tabControl.add(tab1, text='Data Slicer')  
tab2 = Frame(tabControl)        # 创建选项卡（tab）合并
tabControl.add(tab2, text='Data Merge')
tabControl.pack(padx =6,pady=6,fill =BOTH,expand =True)

#标签栏
Data_Load = LabelFrame(tab1,text='Data Load')
Data_Load.pack(anchor =NW,padx =6,pady=6,fill = X)

list1 = Frame(Data_Load)
list1.pack(anchor =W,padx =3,pady=3)

#第一行
a_label = Label(list1, text="Data Path:    ")
a_label.pack(side= LEFT,padx =3,pady=3)
a_entry =Entry(list1,width =40,textvariable = a_entry_str)
a_entry.pack(side= LEFT,padx =3,pady=3)
a_button = Button(list1, text="Load",command =openfile)
a_button.pack(side= LEFT,padx =15,pady=3)

#第二行
list2 = Frame(Data_Load)
list2.pack(anchor =W,padx =3,pady=3)

b_label = Label(list2, text="Save Path:    ")
b_label.pack(side= LEFT,padx =3,pady=3)
b_entry =Entry(list2,width =40,textvariable = b_entry_str)
b_entry.pack(side= LEFT,padx =3,pady=3)

Split_Files = LabelFrame(tab1,text='Split Files')
Split_Files.pack(anchor =NW,padx =6,pady=6,fill = X)

list3 = Frame(Split_Files)
list3.pack(anchor =W,padx =3,pady=3)

c_label = Label(list3, text="Split Unit:    ")
c_label.pack(side= LEFT,padx =3,pady=3)
c_entry =Entry(list3,width =18,textvariable = c_entry_str)
c_entry.pack(side= LEFT,padx =3,pady=3)
c2_button = Checkbutton(list3, text="Have Lable",variable = var2,command =state_button)
c2_button.pack(side= LEFT,padx =15,pady=3)
c_button = Checkbutton(list3, text="Same Lable",variable = var1,state =DISABLED)
c_button.pack(side= LEFT,padx =15,pady=3)



list4 = Frame(Split_Files)
list4.pack(anchor =W,padx =3,pady=3)

d_label = Label(list4, text="Split Num:    ")
d_label.pack(side= LEFT,padx =3,pady=3)
d2_label = Label(list4,textvariable = d2_label_str,width =20)
d2_label.pack(side= LEFT,padx =3,pady=3)
d_button = Button(list4, text="Excute",command =Excute)
d_button.pack(side= RIGHT,padx =3,pady=3)



e_entry_str =StringVar()
e2_entry_str =StringVar()
#存储路径
e3_entry_str=StringVar()
#tab2
#标签栏
Data_Load2 = LabelFrame(tab2,text='Data Load')
Data_Load2.pack(anchor =NW,padx =6,pady=6,fill = X)

list5 = Frame(Data_Load2)
list5.pack(anchor =W,padx =3,pady=3)

#第一行
e_label = Label(list5, text="Data Path_1:    ")
e_label.pack(side= LEFT,padx =3,pady=3)
e_entry =Entry(list5,width =40,textvariable = e_entry_str)
e_entry.pack(side= LEFT,padx =3,pady=3)
e_button = Button(list5, text="Load",command =openfile2)
e_button.pack(side= LEFT,padx =15,pady=3)

list6 = Frame(Data_Load2)
list6.pack(anchor =W,padx =3,pady=3)

e2_label = Label(list6, text="Data Path_2:    ")
e2_label.pack(side= LEFT,padx =3,pady=3)
e2_entry =Entry(list6,width =40,textvariable = e2_entry_str)
e2_entry.pack(side= LEFT,padx =3,pady=3)
e2_button = Button(list6, text="Load",command =openfile3)
e2_button.pack(side= LEFT,padx =15,pady=3)

Merge_File = LabelFrame(tab2,text='Merge File')
Merge_File.pack(anchor =NW,padx =6,pady=6,fill = X)

list7 = Frame(Merge_File)
list7.pack(anchor =W,padx =3,pady=3)

e3_label = Label(list7, text="Save Path:    ")
e3_label.pack(side= LEFT,padx =3,pady=3)
e3_entry =Entry(list7,width =40,textvariable = e3_entry_str)
e3_entry.pack(side= LEFT,padx =3,pady=3)

list8 = Frame(Merge_File)
list8.pack(anchor =CENTER,padx =3,pady=3)

e4_button = Button(list8, text="Merge",command=Merge)
e4_button.pack(side =TOP,padx =15,pady=3)



window.mainloop()