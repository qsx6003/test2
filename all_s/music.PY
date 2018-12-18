import json,requests
from mkdir import *
def yinyue():
    geming=input("请输入歌名：")
    data={'key':geming}
    header = { 'Host': 'c.y.qq.com','Referer': 'http://c.y.qq.com/','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0'}
    url = 'https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg?is_xml=0&format=jsonp&'\
            'g_tk=5381&jsonpCallback=SmartboxKeysCallbackmod_top_search1814'\
            '&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&'\
            'outCharset=utf-8#172;ice=0&platform=yqq&needNewCode=0h'
    da=requests.get(url,params=data,headers=header)
    html = json.loads(da.text.strip('SmartboxKeysCallbackmod_top_search1814()[]'))
    html=html["data"]
    html=html["song"]
    html=html["itemlist"]
    lists=[]
    for i,l in enumerate(html):
       geshou=l["singer"]
       mingcheng=l["name"]
       mid=l["mid"]
       lists.append([i,mingcheng,geshou,mid])
    for i, l in enumerate(lists):
        print("%s：%s---%s"%(l[0],l[1],l[2]))
    i=int(input("请选择歌曲："))
    return lists[i][3]
def url():
    while True:
        mid={'mid':'%s'%yinyue()}
        ur='http://www.douqq.com/qqmusic/qqapi.php'
        da=requests.post(ur,data=mid)
        html=json.loads(da.text)
        html=json.loads(html)
        geshou=html["singername"].replace("/","-").replace(" ","")
        geming=html["songname"]
        m4a=html["m4a"]
        mp31=html["mp3_h"]
        mp32=html["mp3_l"]
        ape=html["ape"]
        flac=html["flac"]
        list=[m4a,mp31,mp32,ape,flac]
        print('0. m4a视频')
        print('1. mp3普通品质')
        print('2. mp3高品质')
        print('3. ape高品无损')
        print('4. flac无损音频')
        select = int(input("请选择要下载的音质:"))
        url=list[select]
        print("下载中，请稍后....")
        header =  {
                'Accept': '*/*',
                'Accept-Encoding': 'identity;q=1, *;q=0',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Host': 'dl.stream.qqmusic.qq.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
                    }
        url=requests.get(url,headers= header).contxient
        path = "d:/音乐"
        # f = mymkdir(path)
        # f.mkdir()
        print(path+"{}.mp3".format(("%s-%s"%(geming,geshou))))
        with open(path+"/{}.mp3".format(("%s-%s"%(geming,geshou))),'wb')as wj:
            wj.write(url)
            print("歌曲下载成功")
        l = f.findfile()
        print(l)
 
if __name__ == '__main__':
    url()
