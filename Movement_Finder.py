#    IN THIS PROJECT FROM CV2 ONLY THESE FUNCTIONS/METHODS ARE USED                                       
#        absdiff    cap.read    cv2.VideoCapture    cv2.imshow  cv2.waitKey cv2.rectangle
#
#    THERE IS NO BUILT-IN/READY TO USE DATAS OR DETECTION SETS OR OTHER THINGS(SUCH AS FACEDETECTION SETS)USED


import cv2

## Function for summing the small partitions of image
def square_counter(init_x, init_y, init_y_original, boundry, array, summation):    
    for x in range(init_x, init_x+boundry):
        
        for y in range(init_y_original,init_y_original+boundry):
            
           summation=summation+array[x,y]  #This will hold our sum data 
            
##     can be used for seeing which pixel exactly we are looking at:
##            print(str(x)+","+str(y))
##           y=y+1                   
    return summation

## Takes difference of two images
def frame_difference(prev_frame, cur_frame, next_frame):

    diff_frames_1 = cv2.absdiff(next_frame,cur_frame)
    diff_frames_2=cv2.absdiff(cur_frame,prev_frame)

    return diff_frames_1&diff_frames_2

##Takes image from camera
def get_frame(cap):
    _, frame = cap.read()
##    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    return frame

if __name__=='__main__':
## Defining initial images
    cap = cv2.VideoCapture(0)

    prev_frame = get_frame(cap)

    cur_frame = get_frame(cap)

    next_frame = get_frame(cap)

while True:
    a=frame_difference(prev_frame,cur_frame, next_frame)
    agray=cv2.cvtColor(a, cv2.COLOR_RGB2GRAY)
##    cv2.imshow('Object Movement',agray)
    prev_frame = cur_frame
    cur_frame = next_frame
    next_frame = get_frame(cap)
    sampleframe=cur_frame
    newframe=sampleframe
##    cv2.rectangle(sampleframe,(int(0),int(0)),(int(0+40),int(0+40)),(0,0,255),1,4)

##    cv2.imshow("sample", sampleframe)
##    cv2.imshow("final",sampleframe)
##    cv2.imshow("final",newframe)
    
    
    for y_wag in range(0,640,60):
        
        
        for x_wag in range(0,479,60):
                  
            bilgi=square_counter(x_wag, y_wag, y_wag, 40, agray, 0)
##              print(bilgi)
            if bilgi>(9000):
                newframe=cv2.rectangle(sampleframe,(int(y_wag),int(x_wag)),(int(y_wag+60),int(x_wag+60)),(0,0,255),1,24)
                cv2.imshow("final",newframe)
            else:
                cv2.imshow("final",newframe)
        cv2.imshow("final",newframe)
    sampleframe=0
    newframe=0
    key = cv2.waitKey(1)
    if key == 27:
        break
