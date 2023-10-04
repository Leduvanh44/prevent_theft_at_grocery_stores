import cv2
import mediapipe as mp
from mediapipe.modules import pose_landmark
camera1 = cv2.VideoCapture(0)
frame2 = cv2.imread('silco.jpeg')
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while True:
        ret1, frame1 = camera1.read()
        if ret1:
            width_to_keep = int(frame1.shape[1] * 0.8)
            cropped_frame11 = frame1[:, :width_to_keep]
            frame2 = cv2.resize(frame2, (frame1.shape[1], frame1.shape[0]))
            if frame1.shape[:2] == frame2.shape[:2]:
                merged_frame = cv2.hconcat([frame1, frame2])
            else:
                merged_frame = frame1
        image = cv2.cvtColor(merged_frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = True
        res = pose.process(image)
        image.flags.writeable = False
        mp_drawing.draw_landmarks(image, res.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2))

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imshow('image', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera1.release()
cv2.destroyAllWindows()