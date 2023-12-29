from coun import counterfun
import cv2
import time
from rich import print,pretty
cap = cv2.VideoCapture('Lohiya.mp4')
cap1 = cv2.VideoCapture('Lohiya.mp4')
cap2 = cv2.VideoCapture('Lohiya.mp4')



def lane3():
    start=time.time()
    count1 = 0
    count2 = 0
    count3 = 0

    while(True):
        ret, frame = cap.read()
        ret2, frame2 = cap1.read()
        ret3, frame3 = cap.read()
        if not(ret ):
            print("[bold][red]Stream 1 failed during 10 second analysis")
            break
        if not(ret2):
            print("[bold][red]Stream 2 failed during 10 second analysis")
            break
        if not(ret3):
            print("[bold][red]Stream 3 failed during 10 second analysis")
            break
        #cv2.imshow("F1",frame)
        #cv2.imshow("F2", frame2)
        if(int((time.time()-start))==10):
            count1,a=counterfun(frame)
            print("Density in LANE 1:>"+str(count1))
        if(int((time.time()-start))==10):
            count2,a=counterfun(frame2)
            print("Density in LANE 2:>"+str(count2))

        if(int((time.time()-start))==10):
            count3,a=counterfun(frame3)
            print("Density in LANE 3:>"+str(count3))
            break



        #cv2.imshow("F3", frame3)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    print("[green]Analysis Completed")

    if (count3 == 0):
        count3 = 1
    if (count2 == 0):
        count2 = 1
    if (count1 == 0):
        count1 = 1
    return(4,5,6)



cv2.destroyAllWindows()


