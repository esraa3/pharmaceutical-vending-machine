from SeleniumMasterCompareImage import ImageCompare
imageCompare=ImageCompare()
a=imageCompare.compare('1.jpg','2.jpg')
print 'Images Equal?',a
