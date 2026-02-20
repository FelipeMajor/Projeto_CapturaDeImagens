import numpy as np
import cv2 as cv
import time
'''
cap = cv.VideoCapture(0)

# Get current width of frame
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)   # float
# Get current height of frame
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT) # float
# Define Video Frame Rate in fps
fps = 10.0

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('saida.avi', fourcc, fps, (int(width),int(height)) )

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #frame = cv.flip(frame, 0)
    # write the flipped frame
    out.write(frame)
    cv.imshow('Imagem Normal', frame)
    if cv.waitKey(1) == ord('q'):
        break
     '''   
cap = cv.VideoCapture('saida.avi')

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret==True:
        # show the frame
        cv.imshow('frame',frame)

        #wait next frame by 40ms - 25fps
        time.sleep(1/100.0) 
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
               
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()


