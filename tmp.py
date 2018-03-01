import cv2
import sys
import os.path
from glob import glob
filename = '/home/estel/PycharmProjects/spider/2.jpeg'
image = cv2.imread(filename)

image = cv2.imread(filename, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)

#face_cascade = cv2.CascadeClassifier("/home/estel/PycharmProjects/spider/lbpcascade_animeface.xml")
face_cascade = cv2.CascadeClassifier("/home/estel/PycharmProjects/spider/haarcascade_frontalface_alt.xml")

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(24, 24))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)


for i, (x, y, w, h) in enumerate(faces):
    face = image[y: y + h, x:x + w, :]
    face = cv2.resize(face, (96, 96))

    save_filename = '%s-%d.jpg' % (os.path.basename(filename).split('.')[0], i)
    print(save_filename)
    cv2.imwrite("/home/estel/PycharmProjects/spider/face/" + save_filename, face)
    cv2.imshow("AnimeFaceDetect", image)
    cv2.waitKey(0)







#cascade = cv2.CascadeClassifier('/home/estel/PycharmProjects/spider/hd2.xml')
#
#

#cv2.imshow('image', image)
#cv2.waitKey(0)