import os
# os.path.abspath(__file__) 当前文件的绝对路径
# 所在目录的名字 os.path.dirname()
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)