import cv2
import sys
import os.path
from glob import glob


def detect(filename):
    #cascade = cv2.CascadeClassifier("/home/estel/PycharmProjects/spider/lbpcascade_animeface.xml")
    cascade = cv2.CascadeClassifier("/home/estel/PycharmProjects/spider/haarcascade_frontalface_alt.xml")
    image = cv2.imread(filename, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    #cv2.imshow('iiii', gray)
    #cv2.waitKey(0)
    faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(24, 24))

    for i, (x, y, w, h) in enumerate(faces):
         face = image[y: y+h, x:x + w, :]
         face = cv2.resize(face, (96, 96))
         save_filename = '%s-%d.jpg' % (os.path.basename(filename).split('.')[0], i)
         print(save_filename)
         cv2.imwrite("/home/estel/PycharmProjects/spider/faces/" + save_filename, face)


if __name__ == '__main__':
    if os.path.exists('faces') is False:
        os.makedirs('faces')

    file_list = glob('新垣结衣/*.jpg')
    for filename in file_list:
        print(filename)
        try:
            detect(filename)
            print('======')
        except:
            print('======')
    file_list2 = glob('新垣结衣/*.jpeg')
    for filename2 in file_list2:
        print(filename2)
        try:
            detect(filename2)
            print('======')
        except:
            print('======')