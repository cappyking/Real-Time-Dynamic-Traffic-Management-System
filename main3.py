from c3 import lane3
import time
import cv2
import numpy
from coun import counterfun
from rich import print,pretty
from pyfiglet import Figlet





def threelaneanalysis(minwait):
    d1,d2,d3=lane3()
    if(d1<=d2 and d1<=d3):
        sig1w=minwait
        sig2w=(d2/d1*minwait)
        sig3w=d3/d1*minwait
    elif(d2<=d1 and d2<=d3):
        sig2w=minwait
        sig1w=(d1/d2*minwait)
        sig3w=d3/d2*minwait
    else:
        sig3w=minwait
        sig1w=(d1/d3*minwait)
        sig2w=d2/d3*minwait

    return (sig1w,sig2w,sig3w,d2,d3)


def threelane(minwait):
    ared = cv2.resize(cv2.imread("000.jpg"), (0, 0), fx=0.4, fy=0.4)
    g1 = cv2.resize(cv2.imread("100.jpg"), (0, 0), fx=0.4, fy=0.4)
    g2 = cv2.resize(cv2.imread("010.jpg"), (0, 0), fx=0.4, fy=0.4)
    g3 = cv2.resize(cv2.imread("001.jpg"), (0, 0), fx=0.4, fy=0.4)
    s1w = 0
    s2w = 0
    s3w = 0
    count1 = 0
    count2 = 0
    count3 = 0
    countc2 = 0
    countp2 = 0
    countc3 = 0
    countp3 = 0
    flag1 = 0
    flag2 = 0
    flag3 = 0
    print("--------------------------------------------")
    print("Status:> All Signals are [red]RED ")
    cv2.imshow("Status", ared)
    start = time.asctime()
    print("Standard 10 second Wait Analysis for 3 Lanes Underway...")
    s1w,s2w,s3w,countp2,countp3=threelaneanalysis(minwait)
    start=time.time()
    cap = cv2.VideoCapture('Lohiyaa.mp4')
    cap1 = cv2.VideoCapture('Lohiyaa.mp4')
    cap2 = cv2.VideoCapture('Lohiyaa.mp4')
    minn=int(min(s1w,s2w,s3w))
    s1w = int(s1w)
    s2w = int(s2w)
    s3w = int(s3w)
    print("Time for Lane 1:> " + str(s1w))
    print("Time for Lane 2:> " + str(s2w))
    print("Time for Lane 3:> " + str(s3w))
    print("The Standard Analysis Time has been switched to:>"+str(minn))
    print("--------------------------------------------")

    while(True):
        if(int(time.time()-start)<=int(s1w)):
            cv2.imshow("Status",g1)

        if(int(time.time()-start)>int(s1w) and (time.time()-start)<=int(s1w+s2w)) :
            cv2.imshow("Status",g2)
        if((int(time.time()-start))>int(s1w+s2w)) :
            cv2.imshow("Status",g3)
        ret, frame = cap.read()
        ret2, frame2 = cap1.read()
        ret3, frame3 = cap2.read()
        if not (ret):
            print("[bold][red]Stream 1 Failed")
            break
        if not (ret2):
            print("[bold][red]Stream 2 Failed")
            break
        if not (ret3):
            print("[bold][red]Stream 3 Failed")
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
            countc2,b= (counterfun(frame2))

            count2=countc2-countp2
            countp2=count2
            print("Lane 2 Density:> "+str(count2))
            flag2=1
            print("[green]Analysis started for Lane 3")
            countc3,c= (counterfun(frame))
            count3=countc3-countp3
            countp3=count3
            print("Lane 3 Density:> "+str(count3))
            time.sleep(0.5)
            flag3=1
        if(flag1==1 and flag2==1 and flag3==1 and int(time.time()-start)==int(s1w+s2w+s3w)):
            print("[bold][yellow]Recalculating...")
            flag1 = 0
            flag2 = 0
            flag3 = 0
            if (count3 == 0):
                count3 = 1
            if (count2 == 0):
                count2 = 1
            if (count1 == 0):
                count1 = 1
            if (count1 <= count2 and count1 <= count3):
                s1w = minwait
                s2w = (count2 / count1 * minwait)
                s3w = count3 / count1 * minwait
            elif (count2 <= count1 and count2 <= count3):
                s2w = minwait
                s1w = (count1 / count2 * minwait)
                s3w = (count3 / count2) * minwait
            else:
                s3w = minwait
                s1w = (count1 / count3 * minwait)
                s2w = count2 / count3 * minwait
            s1w = int(s1w)
            s2w = int(s2w)
            s3w = int(s3w)
            if (s1w >50):
                s1w=50
            if (s2w >50):
                s2w=50
            if (s3w >50):
                s3w=50
            minn=int(min(s1w,s2w,s3w))
            print("Time for Lane 1:> "+str(s1w))
            print("Time for Lane 2:> "+str(s2w))
            print("Time for Lane 3:> " + str(s3w))
            print("The Standard Analysis Time has been switched to:>" + str(minn))
            print("--------------------------------------------")
            start = time.time()
         # cv2.imshow("Image", img)
        if cv2.waitKey(30) & 0xFF == ord('q'): break

    cv2.destroyAllWindows()






