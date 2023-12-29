from pyfiglet import Figlet
from c2 import lane2
import time
import cv2
import numpy
from coun import counterfun
from rich import print,pretty


f=Figlet(font='banner')


def twolaneanalysis(minwait):
    d1,d2=lane2()
    if(d1>=d2):
        sig1w=(d1/d2)*minwait
        sig2w=minwait
    else:
        sig2w = (d2 / d1) * minwait
        sig1w = minwait
    return (sig1w,sig2w,d2)

def twolane(minwait):
    ared = cv2.resize(cv2.imread("00.jpg"), (0, 0), fx=0.4, fy=0.4)
    g1 = cv2.resize(cv2.imread("10.jpg"), (0, 0), fx=0.4, fy=0.4)
    g2 = cv2.resize(cv2.imread("01.jpg"), (0, 0), fx=0.4, fy=0.4)
    s1w = 0
    s2w = 0
    count1 = 0
    count2 = 0
    countc = 0
    countp = 0
    flag1 = 0
    flag2 = 0
    print("--------------------------------------------")
    print("Status:> All Signals are [red] RED ")
    cv2.imshow("Status",ared)
    start=time.asctime()
    print("Standard 10 second Wait Analysis for 2 Lanes Underway...")
    s1w,s2w,countp=twolaneanalysis(minwait)
    s1w = int(s1w)
    s2w = int(s2w)
    start=time.time()
    cap = cv2.VideoCapture('Lohiya.mp4')
    cap1 = cv2.VideoCapture('Lohiya.mp4')
    minn=min(s1w,s2w)
    print("Time for Lane 1:> " + str(s1w))
    print("Time for Lane 2:> " + str(s2w))
    print("The Standard Analysis Time has been switched to:>"+str(minn))
    print("--------------------------------------------")

    while(True):
        if((time.time()-start)<=s1w):
            cv2.imshow("Status",g1)

        if((time.time()-start)>s1w):
            cv2.imshow("Status",g2)
            if(int(time.time()-start)==int(s1w+s2w)):
                start=time.time()

        ret, frame = cap.read()
        ret2, frame2 = cap1.read()
        if not (ret):
            print("[bold][red]Stream 1 Failed")
            break
        if not (ret2):
            print("[bold][red]Stream 2 Failed")
            break

        if(int(time.time()-start)==int(s1w+minn)):
            print("[green]Analysis started for Lane 1")
            count1,a=(counterfun(frame))
            print("Lane 1 Density:> "+str(count1))
            time.sleep(1)
            flag1=1
        if(int(time.time()-start)==minn):
            print("--------------------------------------------")
            print("[green]Analysis started for Lane 2")
            countc,b= (counterfun(frame))
            count2=countc-countp
            countp=count2
            print("Lane 2 Density:> "+str(count2))
            time.sleep(1)
            flag2=1
        if(flag1==1 and flag2==1):
            print("[bold][yellow]Recalculating...")
            if (count2 == 0):
                count2 = 1
            if (count1 == 0):
                count1 = 1
            flag1 = 0
            flag2 = 0
            if (count1 >= count2):
                s1w = (count1 / count2) * minwait
                s2w = minwait
            else:
                s2w = (count2/ count1) * minwait
                s1w = minwait
            if (s1w >50):
                s1w=50
            if (s2w >50):
                s2w=50

            minn=int(min(s1w,s2w))
            print("Time for Lane 1:> "+str(s1w))
            print("Time for Lane 2:> "+str(s2w))
            print("The Standard Analysis Time has been switched to:>" + str(minn))
            print("--------------------------------------------")





    # cv2.imshow("Image", img)
        if cv2.waitKey(30) & 0xFF == ord('q'): break

    cv2.destroyAllWindows()






