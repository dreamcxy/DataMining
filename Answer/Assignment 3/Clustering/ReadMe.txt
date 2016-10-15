Python版本为Python 2.7.10，如果采用Python 3.x版本则运行可能出错。Python需要额外安装numpy包来进行矩阵等数学运算。

实验所用数据集有两个，分别是german.txt和mnist.txt，在kMeans算法中采用的距离为标准的二维平面的欧式距离，其中NMF算法中用到矩阵的F范数。

运行代码时可采用两种方法，分别是直接使用cmd命令行界面，切换进源码所在文件夹，运行python clustering.py即可。或者使用IntelliJ新建工程，导入代码，然后Run运行clustering。以上两种方法都必须将german.txt文件和mnist.txt文件放在与源码相同的文件夹下。

由于数据集规模较大，所以整个代码的运行时间较长，需要等待较久的时间。