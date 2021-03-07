# Using method background substraction.
import cv2
import numpy as np
def median(force , frame):
    force = cv2.medianBlur(force, 3)
    frame = cv2.medianBlur(frame, 3)
    return force , frame

if __name__ == "__main__":
    first_picture = False
    # Create a VideoCapture object and read from input file.
    # If the input is the camera , argument = 0 instead of video file name.
    cap = cv2.VideoCapture("C:/Users/Administrator/Downloads/Video/11.mp4")
    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
    # Check if video open successfull.
    if cap.isOpened() == False:
        print("File video is error")
    # Read until video is completed
    while(cap.isOpened()):
        ret , frame = cap.read()
        # ret is return true if frame is avaliable.
        # Display frame.
        if ret == True:
            fgmk = fgbg.apply(frame)
            fgmk = cv2.medianBlur(fgmk , 5)
            contours , _ = cv2.findContours(fgmk, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                x,y,w,h = cv2.boundingRect(contour)
                if cv2.contourArea(contour) < 1000:
                    continue
                cv2.rectangle(frame,(x,y), (x+w,y+h),(0,255,0), 2)
            cv2.imshow('img', frame)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
