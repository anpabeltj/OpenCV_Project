import cv2 
import numpy as np

def main():
    while True:
        print("=== Welcome to my Motion Detector Program!===")
        try:
            w = int(input("Please input the width of the resolution: "))
            h = int(input("Please input the height of the resolution: "))
            break

        except ValueError:
            print("Please just input in integer!")


    cam = cv2.VideoCapture(0)
    cam.set(3,w)
    cam.set(4,h)

    print(cam.get(3))
    print(cam.get(4))

    if cam.isOpened():
        bentuk = cam.read()

    else:
        bentuk = False

    bentuk, frame1 = cam.read()
    bentuk, frame2 = cam.read()


    while bentuk:
        divide = cv2.absdiff(frame1, frame2)

        abu = cv2.cvtColor(divide, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(abu, (5,5), 0)

        bentuk, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

        dilated = cv2.dilate(thresh, np.ones((3,3), np.uint8), iterations=1)

        kontur, h = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(frame1, kontur, -2, (0, 0, 255), 3)



        cv2.imshow("Input", frame2)
        cv2.imshow("Output", frame1)

        if cv2.waitKey(1) == 27:
            break
        frame1 = frame2 
        bentuk, frame2 = cam.read()

    cv2.destroyAllWindows()
    cam.release()
if __name__ == "__main__":
    main()