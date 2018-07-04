# 提取caffe隐含层特征
基于python与cpp两个版本。
详细说明见[我的博客](http://www.luameows.wang/2018/07/04/%E5%88%A9%E7%94%A8cpp%E6%8F%90%E5%8F%96caffe%E7%89%B9%E5%BE%81/)
## extractfeature.py
python版本提取特征。
## classification.cpp
基于classification.cpp例程修改后提取隐含层特征。
## mean2npy.py
将.binaryproto转化为python读取的.npy格式。
## .prototxt
py_deploy用于python，而ResNet11_classification用于cpp
## out.py
用于测试提取后特征之间相似度。
## .txt
py_result来自python提取的特征，classificaiton_mean来自cpp提取的特征。
