import numpy as np
import sys

caffe_root = '/home/user/caffe/'
sys.path.insert(0, caffe_root + 'python')
import caffe


MEAN_PROTO_PATH = '/home/user/extract_feature/mean.binaryproto'
MEAN_NPY_PATH = '/home/user/extract_feature/mean.npy'

blob = caffe.proto.caffe_pb2.BlobProto()           # create protobuf blob
data = open(MEAN_PROTO_PATH, 'rb' ).read()         # read mean.binaryproto
blob.ParseFromString(data)                         # parse mean.binaryproto to blob

array = np.array(caffe.io.blobproto_to_array(blob))
mean_npy = array[0]
np.save(MEAN_NPY_PATH ,mean_npy)
