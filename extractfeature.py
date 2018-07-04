import numpy as np
import sys
caffe_root='/home/user/caffe/'
sys.path.insert(0,caffe_root+'python')
import caffe
import os
caffe.set_mode_cpu()
model_def = '/home/user/extract_feature/py_deploy.prototxt'
model_weights='/home/user/extract_feature/ResNet11.caffemodel'
net = caffe.Net(model_def,      # defines the structure of the model
                model_weights,  # contains the trained weights
                caffe.TEST)     # use test mode (e.g., don't perform dropout)
mu=np.load('/home/user/extract_feature/mean.npy')
mu = mu.mean(1).mean(1)
print 'mean-subtracted values:', zip('BGR', mu)
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))  # move image channels to outermost dimension
transformer.set_mean('data', mu)            # subtract the dataset-mean value in each channel
transformer.set_raw_scale('data', 255)      # rescale from [0, 1] to [0, 255]
transformer.set_channel_swap('data', (2,1,0))  # swap channels from RGB to BGR
# set the size of the input (we can skip this if we're happy
#  with the default; we can also change it later, e.g., for different batch sizes)
net.blobs['data'].reshape(3,        # batch size
                          3,         # 3-channel (BGR) images
                          96, 96)  # image size is 227x227
image = caffe.io.load_image('/home/user/extract_feature/img/img_3.jpg')
transformed_image = transformer.preprocess('data', image)
net.blobs['data'].data[...] = transformed_image
### perform classification
output = net.forward()
feature=net.blobs['fc1'].data[0]
filehandle=open('py_out.txt','a')
filehandle.write(' '.join(str(a) for a in feature))
filehandle.write('\n')
filehandle.close
