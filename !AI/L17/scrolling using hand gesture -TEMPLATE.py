import cv2
import mediapipe as mp
import pyautogui
import time
from math import hypot

# ==============================

# Configuration Parameters

# ==============================

# Scroll speed can be adjusted as per requirement
SCROLL_SPEED =  # Positive value for scroll up, negative for scroll down

# Delay between consecutive scroll actions to prevent rapid scrolling
SCROLL_DELAY =  # in seconds

# Camera settings
CAMERA_WIDTH = 
CAMERA_HEIGHT = 

# ==============================

# Initialize MediaPipe Hands

# ==============================

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, # Maximum number of hands to detect
        min_detection_confidence=,min_tracking_confidence=)

mp_draw = mp.solutions.

# ==============================

# Gesture Detection Function

# ==============================

def detect_gesture(, ):
    """
    Detects whether the hand gesture is an open palm or a closed fist.

    Args:
    hand_landmarks: The landmarks of the detected hand.
    handedness: 'Left' or 'Right' hand.

    Returns:
    A string indicating the gesture: "scroll_up", "scroll_down", or "none".
    """

    # List to hold the status of each finger (1: up, 0: down)
    fingers = []

    # Define finger tip landmarks
    finger_tips_ids = [mp_hands.HandLandmark.INDEX_FINGER_TIP,
                        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                        mp_hands.HandLandmark.RING_FINGER_TIP,
                        mp_hands.HandLandmark.PINKY_TIP
                        ]

    # Retrieve necessary landmarks
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

    # Check each finger (except thumb) to see if it's up
    for tip_id in finger_tips_ids:
        finger_tip = hand_landmarks.landmark[]
        finger_pip = hand_landmarks.[tip_id - 2] # PIP joint

        if finger_tip.y < finger_pip.y:
            fingers.(1) # Finger is up
        else:
            fingers.(0) # Finger is down

    # Check if thumb is open
    if  == 'Right':
        if thumb_tip. > thumb_ip.:
            fingers.append(1) # Thumb is open
        else:
            fingers.(0) # Thumb is closed

    else:
        if thumb_tip. < thumb_ip.:
            fingers.(1) # Thumb is open
        else:
            fingers.(0) # Thumb is closed

    # Total number of fingers up
    total_fingers = fingers.(1)

    # Determine gesture based on number of fingers up
    if total_fingers == 5:
        return ""
    elif total_fingers == 0:
        return ""
    else:
        return "none"

# ==============================

# Main Function

# ==============================

def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    cap.(cv2.CAP_PROP_FRAME_WIDTH, )
    cap.(cv2.CAP_PROP_FRAME_HEIGHT, )

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    pTime = 0 # Previous time for FPS calculation
    last_scroll_time = 0 # Timestamp of the last scroll action

    print("Hand Gesture Scroll Control is running...")
    print("Show an open palm to scroll up.")
    print("Make a fist to scroll down.")
    print("Press 'q' to exit.")

    while True:
        success, img = cap.read()

        if not success:
            print("Failed to grab frame.")
            break

        img = cv2.flip(img, 1) # Flip the image for a mirror effect
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        gesture = "none"
        handedness = "Unknown"

        if results.multi_hand_landmarks and results.:

            for hand_landmarks, hand_info in zip(results.multi_hand_landmarks, results.):

                # Get hand label (Left/Right)
                handedness_label = hand_info.[0].label
                handedness = handedness_label

                # Draw hand landmarks on the image
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                        mp_draw.DrawingSpec(color=(0, 255, 0), =2, =2),
                                        mp_draw.DrawingSpec(color=(0, 0, 255), =2)
                                        )

                # Detect the gesture
                gesture = detect_gesture(hand_landmarks, )

                # Get current time
                current_time = time.time()

                # Perform scrolling action based on gesture with delay
                if gesture ==  and (current_time - last_scroll_time) > SCROLL_DELAY:
                    pyautogui.scroll(SCROLL_SPEED) # Scroll up
                    last_scroll_time = current_time

                elif gesture ==  and (current_time - last_scroll_time) > SCROLL_DELAY:
                    pyautogui.scroll(-SCROLL_SPEED) # Scroll down
                    last_scroll_time = current_time

        # Calculate Frames Per Second (FPS)
        cTime = time.time()
        fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
        pTime = cTime

        # Display gesture and FPS on the image
        cv2.putText(img, f': {gesture}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.putText(img, f': {int(fps)}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.putText(img, f': {handedness}', (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Show the image
        cv2.imshow("Hand Gesture Scroll Control", img)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()