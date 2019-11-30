# ida_python_extractCode
ida提取特征码脚本
python版本 2.7

环境配置
1.把tq.py 放到ida/python 目录下

2.在ida/python 中找到 init.py ，打开此初始化脚本，然后拖到最下边 找到 
  from idc      import *
  
  from idautils import *
  
  import idaapi
  
  #在下面加一行 
  import tq

3.打开ida测试。快捷键为 ALT+Z

FQA：
  本人是IDA6.8 英文版，没有汉化，如果您是汉化版IDA 提示会出现乱码，不会影响功能！
  
  如果您是汉化版，在引入脚本前，修改文件的编码，然后在进行使用
  

联系方式：QQ 471194425 By:小火（火哥），QQ群号:1026716399 欢迎大家加群学习。


演示动画
![image](http://www.heiwuxs.cn/gif/ida_demo.gif?raw=true)
