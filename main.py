import json
from PIL import Image
from io import BytesIO
from io import BytesIO as Bytes2Data
import cv2
import numpy as np
import base64
with open("/DATA3/image.json",'r') as load_f:
     load_dict = json.load(load_f)
     print(len(load_dict))
     for i in range(10000):
         aa=[]
         img=load_dict[i]['img']
         eng=load_dict[i]['TMEN']
         chi=load_dict[i]['TMCN']
         file=open('dataset.txt','a+')
         print(i)
         ss=''
         ss+=str(i)
         ss += ','
         ss += str(eng)

         ss += ','
         ss += str(chi)
         ss += '\n'
         file.write(ss)
         file.close()
         img = base64.b64decode(img)
         file = open('./img10000/'+str(i)+'.jpg', 'wb')
         file.write(img)
         file.close()
