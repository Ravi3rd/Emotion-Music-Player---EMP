{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "3be606dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2 #import openCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "aaea2885",
   "metadata": {},
   "outputs": [],
   "source": [
    "face_cascade=cv2.CascadeClassifier('C:/Users/HP/anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')\n",
    "# using pretrained classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "f4db8140",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(288, 243, 3)\n"
     ]
    }
   ],
   "source": [
    "img=cv2.imread(\"C:/Users/HP/Downloads/here.jpg\",1) #get image in RGB \n",
    "print(img.shape) #dimension of image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "ef178872",
   "metadata": {},
   "outputs": [],
   "source": [
    "face=face_cascade.detectMultiScale(img,1.1,4) #detecting face in image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "fbf8cae1",
   "metadata": {},
   "outputs": [],
   "source": [
    "for (x,y,w,h) in face:\n",
    "    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle on image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "992d81c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "cv2.imshow('Nw Image',img) #show image at a window\n",
    "cv2.waitKey(0) #wait for user to press any key\n",
    "cv2.destroyAllWindows() #destroy all windows which are activated."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "835d7b75",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
