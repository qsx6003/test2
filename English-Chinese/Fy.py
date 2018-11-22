from tkinter import *
import requests
from getk import Py4Js
import time

def get_html(tr,tk):
    header = {'accept':'*/*',
    'accept-encoding':'gzip, deflate',
    'braccept-language':'zh-CN,zh;q=0.8',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
    AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36'}


    if ord(tr[0])>= 128:
        data = {'q':tr,"tk":tk}
        url = 'https://translate.google.cn/translate_a/single?'\
        'client=t&sl=auto&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld'\
        '&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1'
    else:
        data =  data = {'q':tr,"tk":tk}
        url = 'https://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1'
    rep = requests.get(url,params=data,headers=header).json()
    return rep
def get_data(tr):
    js = Py4Js()
    tk = js.getTk(tr)
    return tk
def jiexi(resul):

    return resul[0][0][0]
def show(tr,res):
    if len(tr)>len(res):
        a = len(tr)
    else:
        a = len(res)


    print(tr,"翻译为-->:",res)
 

def flush(s):
    t.update()
    E.delete(0.0,END)
    T.delete(0.0,END)
    s.delete(0.0,END)

def cut(s):
    s.event_generate("<<Cut>>")
def copy(E):
    E.event_generate("<<Copy>>")
def paste(s):
    s.event_generate('<<Paste>>')


def main(s):
    start = time.time()
    tr = s.get(1.0,END).strip()  #得到输入框
    if not tr:
        return
    tk = get_data(tr)
    resul = get_html(tr,tk)
    res = jiexi(resul)

    E.delete(0.0,END)
    E.insert(INSERT,res)
    E.tag_add("w","0.9","3.12")
    E.tag_config("w",font=("微软雅黑",15))


    end = time.time()
    m = round((end-start),2)
    
    T.delete(0.0,END)
    T.insert(INSERT,"用 时 : {} 秒".format(m))
    T.tag_add("w","0.9","3.12")
    T.tag_config("w",font=("微软雅黑",12))
    
    
    
def mytk():
    global t    
    t = Tk()     #窗口对象
    t.attributes("-alpha",0.9)
    t.attributes("-transparentcolor","red")
    # t.attributes("-topmost",0.1)
    t.title(' '*50+'qsx中英互译')  #窗口标题
    t.geometry("500x208") #尺寸
    t.resizable(False,False)
    path = PhotoImage(file="English-Chinese/335.png")
    Label(t,image=path,compound=CENTER).pack()     
    s = Text(t,height=6,width=60,fg="black",bg="teal")  #输入框属性
    s.place(relx=0,rely=0)   #输入框位置
    s.insert(INSERT,s.get(1.0,END))
    
    s.tag_add("w","0.0","3.12")
    s.tag_config("w",font=("微软雅黑",15))
    Button(t,text="翻译",font=("楷体",15),command=lambda:main(s),bg="aqua")\
            .place(relx=0.88,rely=0.05)  #执行按钮
    Button(t,text="清空",font=("楷体",15),command=lambda:flush(s),bg="pink")\
            .place(relx=0.88,rely=0.80)  #清空
   
    global E   #输出文本框
    E = Text(t,height=7.5,width=60,fg="black",bg="teal")  #输出框属性
    E.place(relx=0,rely=0.35)


    global T   #用时间

    T = Text(t,height=2,width=60,fg="red",bg="teal")  #输出框属性
    T.place(relx=0.0,rely=0.85)
    
    menubar=Menu(t)
    filemenu=Menu(menubar)
    t.config(menu=menubar)
    filemenu.add_command(label="Cut",command=lambda:cut(s))
    filemenu.add_command(label="Copy",command=lambda:copy(E))
    filemenu.add_command(label="Paste",command=lambda:paste(s))
    menubar.add_cascade(label="operating",menu=filemenu)   
    t.mainloop()
if __name__ == "__main__":
    mytk()