from skimage import io
from PIL import Image
import numpy as np
from .models import Print
import logging
from io import BytesIO
from django.contrib.staticfiles.storage import staticfiles_storage


from vit_keras import vit, utils
from keras.applications.vgg16 import VGG16
from keras.applications.vgg19 import VGG19
from keras.applications.efficientnet import EfficientNetB0
import tensorflow
from vit_keras.vit import preprocess_inputs, vit_b16

import pandas as pd


image_size = 224
def load_Model():
    path = Print.objects.last().image_url
    print (path)
    data=img_preprocess(path)
    feat=feat_extraction(data)
    model = tensorflow.keras.models.load_model(staticfiles_storage.path('assets/oralcancer.h5'))
    output=model.predict(feat)
    return output

def feat_extraction(data):
    features=[]
    feat1=pd.DataFrame(vit(data))
    feat2=pd.DataFrame(vgg16(data))
    feat3=pd.DataFrame(vgg19(data))
    feat4=pd.DataFrame(resnet50(data))
    feat5=pd.DataFrame(efficientNetB0(data))

    features=pd.concat([feat1,feat2,feat3,feat4,feat5],axis=1)
    y =np.load(staticfiles_storage.path('assets/selected.npy'))
    selected_feat = pd.Index(y,dtype=np.int64)
    feat_new=features.iloc[:,selected_feat].values
    return feat_new

def img_preprocess(image):
    Qry = Image.open(image)
    Qry = Qry.convert("RGB")
    Qry = np.array(Qry.resize((224,224)))
    Qry = Qry.reshape([224,224,3])
    x = preprocess_inputs(Qry).reshape(1,224, 224, 3)
    return x

def vit(data):
    model = vit_b16(image_size=image_size,pretrained=True,)
    features_new=model.predict(data)
    features=np.array(features_new.flatten())
    features=features.reshape(1,1000)
    return features

def vgg16(data):
    model=VGG16(weights='imagenet',include_top=False)
    feat=model.predict(data)
    feat=np.array(feat.flatten())
    return feat.reshape(1,25088)

def vgg19(data):
    model=VGG19(weights='imagenet',include_top=False)
    feat=model.predict(data)
    feat=np.array(feat.flatten())
    return feat.reshape(1,25088)

def resnet50(data):
    model=tensorflow.keras.applications.ResNet50(weights='imagenet',include_top=False)
    feat=model.predict(data)
    feat=np.array(feat.flatten())
    return feat.reshape(1,100352)

def efficientNetB0(data):
    model=EfficientNetB0(weights='imagenet',include_top=False)
    feat=model.predict(data)
    feat=np.array(feat.flatten())
    return feat.reshape(1,62720)




    



