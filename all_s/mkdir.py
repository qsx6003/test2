import os

class mymkdir:
    
    def __init__(self,path):
        self.path=path.strip().strip("\\")

    def mkdir(self):
       
 # 判断路径是否存在
    
        isExists=os.path.exists(self.path)
    
        # 判断结果
        if not isExists:# 如果不存在则创建目录# 创建目录操作函数
            os.makedirs(self.path) 
    
            print(self.path+' 创建成功')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(self.path+' 目录已存在')
            return False
if __name__ == "__main__":
    f = mymkdir("d:/音乐/")
    f.mkdir()
