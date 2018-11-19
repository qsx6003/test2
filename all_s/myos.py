# import os
# a = 1
# print(a)


# os.system('python tulin-post.py')
# print(a)
# print(a)
# print(a)



params = {'app_id':'app_id',                #请求包，需要根据不同的任务修改，基本相同
              'image':'img',                    #文字类的任务可能是‘text’，由主函数传递进来
              'mode':'0' ,                    #身份证件类可能是'card_type'
              'time_stamp':'time_stamp',        #时间戳，都一样
              'nonce_str':'nonce_str',          #随机字符串，都一样
              #'sign':''                      #签名不参与鉴权计算，只是列出来示意
             }

sort_dict= sorted(params.items(), key=lambda item:item[0], reverse = False)  #字典排序
print(sort_dict)