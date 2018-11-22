from tkinter import *



import requests
from getk import Py4Js
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
 


def main():
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


    
def mytk():
    t = Tk()     #窗口对象
    t.title("qsx中英互译")  #窗口标题
    t.geometry("500x200") 



    global s     #尺寸
    s = Text(t,height=6,width=60)  #输入框属性
    s.place(relx=0,rely=0)   #输入框位置
    s.insert(INSERT,s.get(1.0,END))
    
    s.tag_add("w","0.0","3.12")
    s.tag_config("w",font=("微软雅黑",15))



    Button(t,text="翻译",font=("楷体",15),command=main).place(relx=0.88,rely=0.05)  #执行按钮


    global E
    E = Text(t,height=6,width=60)  #输出框属性
    E.place(relx=0,rely=0.5)
    
    
    
    
    
    
    
    t.mainloop()







if __name__ == "__main__":
    mytk()