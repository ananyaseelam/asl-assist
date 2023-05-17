# Adding Imports
import cv2
import os
import time
import uuid


IMAGES_PATH = '/Users/ananyaseelam/junior/sp23/ai-prac/asl-assist/detectWords/Tensorflow/workspace/images/'

# labels = ['hello']

labels = ['thanks', 'yes', 'no', 'iloveyou', 'water', 'please', 'time', 'food', 'bathroom']
num_imgs = 15


for label in labels:
#     !mkdir {'Tensorflow\workspace\images\collectedimages\\'+label}
    os.mkdir('/Users/ananyaseelam/junior/sp23/ai-prac/asl-assist/detectWords/Tensorflow/workspace/images/'+label)
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(num_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        print(imagename)
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()