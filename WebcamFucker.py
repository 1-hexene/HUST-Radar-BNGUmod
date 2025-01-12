import cv2

class webcamFucker:
    def __init__(self, webcam = 0):
        self.webcam = webcam
        self.cap = None
        pass
    
    def fuckExposure(self, exposure=80):
        self.cap = cv2.VideoCapture(self.webcam)
        self.cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
        self.cap.set(cv2.CAP_PROP_EXPOSURE, 80)
        print("[webcamfucker] webcam Fucked.")
        #while True:
        #    ret, frame = cap.read()
        #    cv2.imshow("webcam", frame)

        #    if cv2.waitKey(1) == ord("q"):
        #        break

        self.cap.release()
        #cv2.destroyAllWindows()

    def resetExposure(self):
        self.cap = cv2.VideoCapture(self.webcam)
        self.cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
        self.cap.release()
    