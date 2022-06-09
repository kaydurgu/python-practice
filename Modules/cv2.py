#before running the program check out if u download a camera by ip and dont forget to change url if its different

import requests
import cv2
import numpy as np	
import imutils

url = "http://192.168.60.101:8080/shot.jpg"

while True:
	img_resp = requests.get(url)
	img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
	img = cv2.imdecode(img_arr, -1)

	img = imutils.resize(img, width=1800, height=2500)

	cv2.imshow("Android_cam", img)

	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()
