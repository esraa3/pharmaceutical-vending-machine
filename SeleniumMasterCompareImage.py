import cv2
import numpy as np
import argparse
import imutils
class ImageCompare():
    def __init__(self):
        print "compare images in python"
    def compare(self,image1,image2):
        match=False
#pound1.tif #cur.png #ppp.tif  #po.png #poo.png  #puz.jpg  #waldo.jpg
#pooo.png  #cut.jpg  #ppp.tif  #pound.png
        capture=cv2.imread('G:\money\poo.png') #load first image
        im2=cv2.imread('G:\money\po.png')  #load second image
        (im2Height,im2Width)=im2.shape[:2]  #access to dimensions of second image
        res=cv2.matchTemplate(capture,im2,cv2.TM_CCOEFF) #matching with CCOEFF method
        (_,_,minLoc,maxLoc)=cv2.minMaxLoc(res)  #to find where good matching are
        topLeft=maxLoc
        botRight=(topLeft[0]+im2Width,topLeft[1]+im2Height)
        roi=capture[topLeft[1]:botRight[1],topLeft[0]:botRight[0]]
        row1, cols1, channel1 = roi.shape
        row2, cols2, channel2 = im2.shape
        if (row1 != row2) or (cols1 != cols2) or (channel1 != channel2):
            print "two images are different"
            match=False
            return match
        else:
            print "two images are not different"
            match=True
            return match
##        mask=np.zeros(capture.shape,dtype="uint8")
##        capture=cv2.addWeighted(capture,0.25,mask,0.75,0)
##        capture[topLeft[1]:botRight[1],topLeft[0]:botRight[0]]=roi
##        cv2.imshow("capture",imutils.resize(capture,height=650))
##        cv2.imshow("capture",capture)
##        cv2.imshow("im2",im2)
##        imageCompare=ImageCompare()
##        a=imageCompare.compare('1.jpg','2.jpg')
##        print 'Images Equal?',a

        cv2.waitKey(0)

