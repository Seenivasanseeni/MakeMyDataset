import cv2

class Camera():
    def __init__(self,dev_id=0):
        try:
            self.camera=cv2.VideoCapture(dev_id)
        except:
            raise Exception("Error in Opening device dev_id="+str(dev_id))
        return

    def captureImage(self):
        if( not self.camera.isOpened()):
            print("Camera is Closed.")
            return
        ret,frame=self.camera.read()
        if(ret):
            return frame
        raise Exception("Cant capture the Image")

    def release(self):
        self.camera.release()
