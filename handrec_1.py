#necessary imports
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
save_name = 'output.avi' 
out = cv2.VideoWriter( save_name, fourcc, 20.0, (640, 480))
i = 0   #Screenshot counter
pStr = 'Marker'

while True:

    #Load image from webcam and perform a\basic processing on it
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converting the image to grayscale
    gray = cv2.GaussianBlur(gray, (5, 5), 0)   #applying a Gaussian blur to smooth out the image

    ret, edge = cv2.threshold(gray, 100, 255, 0)

    #detect contours
    im2, contours, hierarchy = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #only keep the 5 largest contours, sorted in descending order
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:3]
    
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.01 * peri, True)
        if len(approx) == 4:
            #draw contours on the image
            cv2.drawContours(frame, [approx], -1,[0, 255, 0], 2)    #-1 indicates all contours
            cv2.putText(frame, pStr, (0, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, str(approx[0][0]), (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

    #display the final image
    cv2.imshow('Final Image', frame)
    out.write(frame)

    #Take screenshot when 'p' is pressed:
    if cv2.waitKey(1) & 0xFF == ord('p'):
        imname = 'screenshot_' + str(i) + '.png'
        i+=1
        cv2.imwrite(imname, frame)
        
    #exit sequence: Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the VideoCapture and destroy all the windows
cap.release()
out.release()
cv2.destroyAllWindows()
