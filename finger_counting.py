import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'   

import logging
logging.getLogger('mediapipe').setLevel(logging.CRITICAL)

import cv2
import mediapipe as mp
import time


class HandDetector():
    def __init__(self, mode=False, maxHands=2, detectionConfidence=0.5, trackConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,
                                        max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionConfidence,
                                        min_tracking_confidence=self.trackConfidence)

        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks and draw:

            for handLms in self.results.multi_hand_landmarks:

                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img):
        all_hands_landmarks = []

        if self.results.multi_hand_landmarks:
            h, w, c = img.shape
            
            for hand in self.results.multi_hand_landmarks:
                
                hand_landmarks = []
                
                for id, lm in enumerate(hand.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    hand_landmarks.append([id, cx, cy])

                all_hands_landmarks.append(hand_landmarks)

        return all_hands_landmarks

    def fingerCountingAndLabeling(self, img):

        fingerTips = [4, 8, 12, 16, 20]

        fingerNames = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
        h, w, c = img.shape
        totalCount = 0

        if self.results.multi_hand_landmarks:
            for handIdx, handLms in enumerate(self.results.multi_hand_landmarks):

                handedness = self.results.multi_handedness[handIdx].classification[0].label

                landmarks = [(int(lm.x * w), int(lm.y * h)) for lm in handLms.landmark]

                count = 0
                labels = []

                
                if handedness == "Left":
                    if landmarks[4][0] > landmarks[3][0]:
                        count += 1
                        labels.append("Thumb")
                else:
                    if landmarks[4][0] < landmarks[3][0]:
                        count += 1
                        labels.append("Thumb")

                 
                for i in range(1, 5):
                    if landmarks[fingerTips[i]][1] < landmarks[ fingerTips[i] - 2 ][1]:

                        count += 1
                        labels.append(fingerNames[i])

                totalCount += count

                
                for i, finger in enumerate(fingerNames):
                    x, y = landmarks[fingerTips[i]]
                    color = (0, 255, 0) if finger in labels else (0, 0, 255)
                    cv2.putText(img, f'{finger}', (x - 20, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

                 
                cv2.putText(img, f'Hand {handIdx+1}: {count}', (landmarks[0][0] - 30, landmarks[0][1] - 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)

        
        cv2.putText(img, f'Total Fingers: {totalCount}', (10, 130),cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)

        return img


def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    detector = HandDetector()
    ptime = 0

    while True:
        success, img = cap.read()
        if not success:
            print("Error reading from camera")
            continue

        img = detector.findHands(img)
        _ = detector.findPosition(img)
        img = detector.fingerCountingAndLabeling(img)

        
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)

        cv2.imshow("Finger Counter", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
