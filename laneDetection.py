
import cv2
import numpy as np
import matplotlib.pylab as plt
cap=cv2.VideoCapture("test2.mp4")
while cap.isOpened():
   ret,image=cap.read()
   image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
   height=image.shape[0]
   width=image.shape[1]
   roi=[(0,height),(width/2,height/2),(width,height)]
   def roii(image,ver):
      mask=np.zeros_like(image)
      match_mask_color=255
      cv2.fillPoly(mask,ver,match_mask_color)
      masked_image=cv2.bitwise_and(image,mask)
      return masked_image
   gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
   canny_image=cv2.Canny(gray,100,200)
   cropped_image=roii(canny_image,np.array([roi],np.int32))
   lines=cv2.HoughLinesP(cropped_image,6,np.pi/60,160,minLineLength=40,maxLineGap=25)
   def dl(image,lines):
      image=np.copy(image)
      blank_image=np.zeros((image.shape[0],image.shape[1],3),np.uint8)
      for line in lines:
         for x1,y1,x2,y2 in line:
            cv2.line(blank_image,(x1,y1),(x2,y2),(0,255,0),2)
      image=cv2.addWeighted(image,0.8,blank_image,1,0.0)
      return image
    

   image=dl(image,lines)

   cv2.imshow("dd",image)
   if cv2.waitKey(1) & 0xFF==ord('q'):
      break
cap.release()
cv2.destroyAllWindows()
