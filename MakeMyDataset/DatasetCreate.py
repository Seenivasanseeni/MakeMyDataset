import os
import tools
import matplotlib.pyplot as plt
import Camera
from PIL import Image

DataDirectory="../Dataset"

labels=["seeni","NOTSeeni"]

#make dirs as needed

path={
    "seeni":os.path.join(DataDirectory,labels[0]),
    "NOTSeeni":os.path.join(DataDirectory,labels[1])
}

os.makedirs(DataDirectory,exist_ok=True)
os.makedirs(path["seeni"],exist_ok=True)
os.makedirs(path["NOTSeeni"],exist_ok=True)


#read Configuration
configLocation="../Conf/config.json"
conf=tools.readConf(configLocation)

def getPathName(label):
    file_path=os.path.join(path[label],label+str(conf[label]))+".png"
    conf[label]+=1
    tools.writeConf(path=configLocation,conf=conf)
    return file_path

def saveImage(ImageData,label):
    file_path=getPathName(label)
    im=Image.fromarray(ImageData)
    im.save(file_path)
    return

def LabelIt():
    print("Enter the class 1 for {} and  0 for {}".format(labels[0],labels[1]))
    choice=int(input())
    if(choice):
        return "seeni"
    return "NOTSeeni"


def makeData(cam):
    image=cam.captureImage()
    plt.imshow(image)
    plt.show()
    label=LabelIt()
    saveImage(image,label)
    return

def capture():
    cam=Camera.Camera()
    makeData(cam)
    return

capture()
