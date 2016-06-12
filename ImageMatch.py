import cv2
import numpy as np
import argparse
import imutils
def compare(capture,im2):
    match=False   #initial value of match
    (im2Height,im2Width)=im2.shape[:2]  #access to dimensions of second image
    res=cv2.matchTemplate(capture,im2,cv2.TM_CCOEFF) #matching with CCOEFF method
    (_,_,minLoc,maxLoc)=cv2.minMaxLoc(res) #to find where good matching are
    topLeft=maxLoc
    botRight=(topLeft[0]+im2Width,topLeft[1]+im2Height)
    res=capture[topLeft[1]:botRight[1],topLeft[0]:botRight[0]] #(res)result img from matching 
    row1, cols1, channel1 = res.shape  #determine r,c,ch for roi(result)
    row2, cols2, channel2 = im2.shape  #img from data
    if (row1 != row2) and (cols1 != cols2) or (channel1 != channel2):
        print "two images are different"
        match=False
        return match
    else:
        mismatch = 0
        for i in range(1, row1):
            for j in range(1, cols1):
                px1 = res[i, j]
                px2 = im2[i, j]
                if (px1.sum() != px2.sum()):
                    mismatch = mismatch + 1
        print 'total mismatch equals :', mismatch
        if(mismatch<=55000):
            match=True
        else:
            match=False
        return match
    #C:\Users\Hard ware\Desktop\
    #C:\Users\Hard ware\Desktop\money5\
capture=cv2.imread('C:\Users\Hard ware\Desktop\money5\imag2.jpg') #img from camera
image2=cv2.imread('C:\Users\Hard ware\Desktop\money5\imae.png') #img1 from data
image3=cv2.imread('C:\Users\Hard ware\Desktop\money5\imz.png')  #img2 from data
image4=cv2.imread('C:\Users\Hard ware\Desktop\money5\imm.png')  #img3 from data
## imageList=[image2,image3,image4]
##for i in imageList:
##    a=compare(capture,i)
##    print "matching !!",a
b=compare(capture,image2)
print "matching !!",b
c=compare(capture,image3)
print "matching !!",c
d=compare(capture,image4)
print "matching !!",d
if (b==True) and (c==True) and (d==True):
    print "total matching is True"
elif (b==True) and (c==True) and (d==False):
    print "total matching is True"
elif (b==True) and (c==False) and (d==True):
    print "total matching is True"    
elif (b==False) and (c==True) and (d==True):
    print "total matching is True"
else :
    print "==========================="
    print "total matching is False"
        

