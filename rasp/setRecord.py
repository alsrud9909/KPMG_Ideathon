# -*- coding: utf-8 -*-
"""setRecord.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rT-ch-otPtGK_JyndYrj5Kd7ASwYpuri
"""

from darkflow.net.build import TFNet #경로 수정 필요
import datetime
import cv2
import sympy

#물체 인식을 위한 설정
opoptions = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.1}
tfnet = TFNet(options)

# 영상의 의미지를 연속적으로 캡쳐할 수 있게 하는 class
capture = cv2.VideoCapture('..경로')#경로수정
fourcc = cv2.VideoWriter_fourcc(*'AVI')#인코딩방식
recird = False
count = 0
now = datetime.datetime.now().strftime("%d_%H-%M-%S")
fps = capture.get(cv2.CAP_PROP_FPS)#동영상 프레임 추출
length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))#동영상 길이
split = (fps*length)/(fps*3)

#면적 평균 변화율을 구하기 위한 변수들
tlx = 0 		#바운드 박스 topleft x값
tly = 0 		#바운드 박스 topleft y값

brx = 0     #바운드 박스 bottomright x값
bry = 0			#바운드 박스 bottomright y값

S  = 0 #현재 사각형 넓이
PS = 0 #이전 사각형 넓이
while(vidcap.isOpened()):
    ret, image = vidcap.read()
 
    if(int(vidcap.get(1)) % split == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite("../images/frame%d.jpg" % count, image)
				imgcv = cv2.imread("../images/frame%d.jpg")#opencv이용해 처리
				result = tfnet.return_predict(imgcv)#JSON포맷으로 이미지정보결과 저장
				S = (brx-tlx)*(tly-bry)
		    if(녹화중&&변화율<임계값)
					녹화종료
		    if( S - PS > 임계값 ??) #변화율 조건 필요
					녹화시작
		     
        print('Saved frame%d.jpg' % count)
        count += 1

for i in range(1,count)

#get() 함수를 이용하여 전체 프레임 중 1/20의 프레임만 가져와 저장
#최대 30초 동영상이라고 가정.변화율 측정에 최소 3초가 필요하다고 가정.
#파이카메라의 제원이 1080p-30fps, 720p-60fps이므로
#30*30=900, 30*60=1800 -> 만약 30fps의 30초 동영상이면, split=10이 되어야함
capture.release()