import requests
from getk import Py4Js
from tulinpost import *
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
    while True:
        # a = chat(0)
        a = input("请输入要翻译的内容>>: ")
        tr = a
        if not tr:
            break
        tk = get_data(tr)
        resul = get_html(tr,tk)
        res = jiexi(resul)
        show(tr,res)


if __name__ == "__main__":
    main()




