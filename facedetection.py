# Detect facial landmarks
# from mtcnn import MTCNN
# import cv2
# detector=MTCNN()
# img = cv2.imread('/home/anushka/Documents/facedetection/MTCNN_Image1.jpeg')
# resized_img=cv2.resize(img,(500,500))
# output=detector.detect_faces(resized_img)
# print(output)
# x,y,width,height=output[0]['box']
# cv2.rectangle(resized_img,pt1=(x,y),pt2=(x+width,y+height),color=(255,0,0),thickness=3)
# lefteye_x,lefteye_y=output[0]['keypoints']['left_eye']
# righteye_x,righteye_y=output[0]['keypoints']['right_eye']
# nose_x,nose_y=output[0]['keypoints']['nose']
# mouthleft_x,mouthleft_y=output[0]['keypoints']['mouth_left']
# mouthright_x,mouthright_y=output[0]['keypoints']['mouth_right']
# cv2.circle(resized_img,center=(lefteye_x,lefteye_y),color=(0,255,0),radius=15)
# cv2.circle(resized_img,center=(righteye_x,righteye_y),color=(0,255,0),radius=15)
# cv2.circle(resized_img,center=(nose_x,nose_y),color=(0,255,0),radius=15)
# cv2.circle(resized_img,center=(mouthleft_x,mouthleft_y),color=(0,255,0),radius=15)
# cv2.circle(resized_img,center=(mouthright_x,mouthright_y),color=(0,255,0),radius=15)
# cv2.imshow('image',resized_img)
# cv2.waitKey(0)
