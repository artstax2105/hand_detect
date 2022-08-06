import cv2
import win32con

import HandTrackingModule as htm
import cvzone
import numpy as np
import win32api
import pyautogui

import mediapipe as mp
import time
import math


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = htm.handDetector(detectionCon=0.8)
colorR = (255, 0, 255)

cx, cy, w, h = 1000, 1000, 1920, 1080
pTime = 0
cTime = 0


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    dim = (1920, 1080)
    img = cv2.resize(img, dim)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)


    if len(lmList) != 0:
        cursor = lmList[8][1:]  # index finger tip landmark
        # call the update

        win32api.SetCursorPos((cursor[0], cursor[1]))
        length, _, _ = detector.findDistance(12, 4, img, draw=False)
        if length < 40:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, cursor[0], cursor[1], 0, 0)
        else:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, cursor[0], cursor[1], 0, 0)




    cv2.waitKey(1)
    cTime = time.time()
    fps = 1. / (cTime - pTime)
    pTime = cTime
    print(fps)

