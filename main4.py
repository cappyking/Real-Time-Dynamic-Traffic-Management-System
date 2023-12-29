from pyfiglet import Figlet
from c4 import lane4
import time
import cv2
import numpy as np
from coun import counterfun
from rich import print,pretty
import matplotlib.pyplot as plt

def fourlaneanalysis(minwait):

    d1,d2,d3,d4=lane4()
    if(d1<=d2 and d1<=d3 and d1<=d4):
        sig1w=minwait
        sig2w=(d2/d1*minwait)
        sig3w=d3/d1*minwait
        sig4w = d4 / d1 * minwait

    elif(d2<=d1 and d2<=d3 and d2<d4):
        sig2w=minwait
        sig1w=(d1/d2*minwait)
        sig3w=d3/d2*minwait
        sig4w = d4 / d2 * minwait
    elif(d3<=d2 and d3<=d1 and d3<d4):
        sig3w=minwait
        sig1w=(d1/d3*minwait)
        sig2w=d2/d3*minwait
        sig4w = d4 / d3 * minwait
    else:
        sig4w=minwait
        sig1w=(d1/d4*minwait)
        sig2w=d2/d4*minwait
        sig3w=d3/d4*minwait

    return (sig1w,sig2w,sig3w,sig4w,d2,d3,d4)


def fourlane(minwait):
    ared = cv2.resize(cv2.imread("0000.jpg"), (0, 0), fx=0.4, fy=0.4)
    g1 = cv2.resize(cv2.imread("1000.jpg"), (0, 0), fx=0.4, fy=0.4)
    g2 = cv2.resize(cv2.imread("0100.jpg"), (0, 0), fx=0.4, fy=0.4)
    g3 = cv2.resize(cv2.imread("0010.jpg"), (0, 0), fx=0.4, fy=0.4)
    g4 = cv2.resize(cv2.imread("0001.jpg"), (0, 0), fx=0.4, fy=0.4)

    f = Figlet(font='banner')
    a=b=c=d=cv2.resize(cv2.imread("1000.jpg"), (0, 0), fx=0.4, fy=0.4)
    s1w = 0
    s2w = 0
    s3w = 0
    s4w = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    countc = 0
    countp = 0
    countc2 = 0
    countp2 = 0
    countc3 = 0
    countp3 = 0
    flag1 = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0
    print("--------------------------------------------")
    print("Status:> All Signals are RED ")
    cv2.imshow("Status", ared)
    print("Standard 10 second Wait Analysis for 4 Lanes Underway...")

    start = time.asctime()
    s1w,s2w,s3w,s4w,countp,countp2,countp3=fourlaneanalysis(minwait)
    start=time.time()
    cap = cv2.VideoCapture('a1.mp4')
    cap1 = cv2.VideoCapture('a2.mp4')
    cap2 = cv2.VideoCapture('a3.mp4')
    cap3 = cv2.VideoCapture('a4.mp4')
    minn=min(s1w,s2w,s3w,s4w)
    s1w = int(s1w)
    s2w = int(s2w)
    s3w = int(s3w)
    s4w = int(s4w)
    print("Time for Lane 1:> " + str(s1w))
    print("Time for Lane 2:> " + str(s2w))
    print("Time for Lane 3:> " + str(s3w))
    print("Time for Lane 4:> " + str(s4w))
    print("The Standard Analysis Time has been switched to:>"+str(minn))
    print("--------------------------------------------")

    while(True):
        if(int(time.time()-start)<=int(s1w)):
            cv2.imshow("Status",g1)

        if(int(time.time()-start)>int(s1w) and (time.time()-start)<=int(s1w+s2w)) :
            cv2.imshow("Status",g2)

        if(int(time.time()-start)>int(s1w+s2w) and (time.time()-start)<=int(s1w+s2w+s3w)) :
            cv2.imshow("Status",g3)

        if((int(time.time()-start))>int(s1w+s2w+s3w)) :
            cv2.imshow("Status",g4)

        ret, frame = cap.read()
        ret2, frame2 = cap1.read()
        ret3, frame3 = cap2.read()
        ret4, frame4 = cap3.read()
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.rectangle(frame, (0, 0), (70, 50), [0, 0, 0], -1)
        cv2.rectangle(frame2, (0, 0), (70, 50), [0, 0, 0], -1)
        cv2.rectangle(frame3, (0, 0), (70, 50), [0, 0, 0], -1)
        cv2.rectangle(frame4, (0, 0), (70, 50), [0, 0, 0], -1)

        cv2.putText(frame, "Lane 1", (10,30), font, 1, (0, 255, 255), 2)
        cv2.putText(frame2, "Lane 2", (10,30), font, 1, (0, 255, 255), 2)
        cv2.putText(frame3, "Lane 3", (10,30), font, 1, (0, 255, 255), 2)
        cv2.putText(frame4, "Lane 4", (10,30), font, 1, (0, 255, 255), 2)

        if not (ret):
            print("[bold][red]Stream 1 Failed")
            break
        if not (ret2):
            print("[bold][red]Stream 2 Failed")
            break
        if not (ret3):
            print("[bold][red]Stream 3 Failed")
            break

        if not (ret4):
            print("[bold][red]Stream 4 Failed")
            break
        verti=np.concatenate((frame,frame2),axis=1)
        verti2 = np.concatenate((frame3, frame4), axis=1)
        hori=np.concatenate((verti,verti2),axis=0)
        cv2.imshow("Live Feed",hori)

        if(int(time.time()-start)==int(s1w+minn)):
            print("[green]Analysis started for Lane 1")
            count1,a=(counterfun(frame))
            print("Lane 1 Density:> "+str(count1))
            time.sleep(1)
            flag1=1

        if(int(time.time()-start)==(minn)):
            print("--------------------------------------------")

            print("[green]Analysis started for Lane 2")
            countc,b= (counterfun(frame2))
            count2=countc-countp
            countp=count2
            print("Lane 2 Density:> "+str(count2))
            flag2=1


            print("[green]Analysis started for Lane 3")
            countc2,c= (counterfun(frame3))
            count3=countc2-countp2
            countp2=count3
            print("Lane 3 Density:> "+str(count3))
            flag3=1


            print("[green]Analysis started for Lane 4")
            countc3,d= (counterfun(frame4))
            count4=countc3-countp3
            countp3=count4
            print("Lane 4 Density:> "+str(count4))
            flag4=1


            time.sleep(0.5)

        if (flag1 == 1 and flag2 == 1 and flag3 == 1 and flag4 == 1 and int(time.time() - start) == int(s1w + s2w + s3w+s4w)):
            print("[bold][yellow]Recalculating...")
            det=np.concatenate((a,b,c,d),axis=0)
            cv2.imshow("Detection",det)
            flag1 = 0
            flag2 = 0
            flag3 = 0
            flag4 = 0
            if (count3 == 0):
                count3 = 1
            if (count2 == 0):
                count2 = 1
            if (count1 == 0):
                count1 = 1
            if (count4 == 0):
                count1 = 1

            if (count1 <= count2 and count1 <= count3 and count1 <= count4):
                s1w = minwait
                s2w = (count2 / count1 * minwait)
                s3w = count3 / count1 * minwait
                s4w = count4 / count1 * minwait
            elif (count2 <= count1 and count2 <= count3 and count2 <= count4):
                s2w = minwait
                s1w = (count1 / count2 * minwait)
                s3w = count3 / count2 * minwait
                s4w = count4 / count2 * minwait
            elif (count3 <= count1 and count3 <= count2 and count3 <= count4):
                s3w = minwait
                s1w = (count1 / count3 * minwait)
                s2w = count2 / count3 * minwait
                s4w = count4 / count3 * minwait
            else:
                s4w = minwait
                s1w = (count1 / count4 * minwait)
                s2w = count2 / count4 * minwait
                s3w = count3 / count4 * minwait

            s1w = int(s1w)
            s2w = int(s2w)
            s3w = int(s3w)
            s4w = int(s4w)
            if (s1w > 50):
                s1w = 50
            if (s2w > 50):
                s2w = 50
            if (s3w > 50):
                s3w = 50
            if (s4w > 50):
                s4w = 50
            minn = int(min(s1w, s2w, s3w,s4w))
            print("Time for Lane 1:> " + str(s1w))
            print("Time for Lane 2:> " + str(s2w))
            print("Time for Lane 3:> " + str(s3w))
            print("Time for Lane 4:> " + str(s4w))
            print("The Standard Analysis Time has been switched to:>" + str(minn))
            print("--------------------------------------------")
            start = time.time()




    # cv2.imshow("Image", img)
        if cv2.waitKey(30) & 0xFF == ord('q'): break

    cv2.destroyAllWindows()






