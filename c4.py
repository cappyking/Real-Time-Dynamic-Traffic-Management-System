from coun import counterfun
import cv2
import time

cap = cv2.VideoCapture('Lohiya.mp4')
cap1 = cv2.VideoCapture('Lohiya.mp4')
cap2 = cv2.VideoCapture('Lohiya.mp4')
cap3 = cv2.VideoCapture('Lohiya.mp4')

count1=0
count2=0
count3=0
count4=0

def lane4():
    start=time.time()

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    while(True):
        ret, frame = cap.read()
        ret2, frame2 = cap1.read()
        ret3, frame3 = cap2.read()
        ret4,frame4=cap3.read()

        if not(ret ):
            print("Stream 1 Failed")
            break
        if not(ret2):
            print("Stream 2 Failed")
            break
        if not(ret3):
            print("Stream 3 Failed")
            break
        if not(ret4):
            print("Stream 4 Failed")
            break

        #cv2.imshow("F1",frame)
        #cv2.imshow("F2", frame2)
        if(int((time.time()-start))==10):
            count1,a=counterfun(frame)
            print("Density in LANE 1:>"+str(count1))
            #cv2.imshow("Lane 1",a)

        if(int((time.time()-start))==10):
            count2,a=counterfun(frame2)
            print("Density in LANE 2:>"+str(count2))
            #cv2.imshow("Lane 2",a)

        if(int((time.time()-start))==10):
            count3,a=counterfun(frame3)
            print("Density in LANE 3:>"+str(count3))
            #cv2.imshow("Lane 3",a)

        if(int((time.time()-start))==10):
            count4,a=counterfun(frame4)
            print("Density in LANE 4:>"+str(count4))
            #cv2.imshow("Lane 4",a)
            break


        #cv2.imshow("F3", frame3)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    print("Analysis Completed")
    print("--------------------------------------------")
    if (count4 == 0):
        count4 = 1
    if (count3 == 0):
        count3 = 1
    if (count2 == 0):
        count2 = 1
    if (count1 == 0):
        count1 = 1
    return(4,5,6,5)






