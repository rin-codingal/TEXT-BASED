import cv2
import mediapipe as mp
import time
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=, min_tracking_confidence=)
mp_draw = mp.solutions.drawing_utils

# Filters to cycle through
filters = [
            None, # No filter
            'GRAYSCALE', # Grayscale filter
            'SEPIA', # Sepia filter
            'NEGATIVE', # Negative filter
            'BLUR' # Blur filter
            ]

current_filter = 0 # Starting filter

# Webcam setup
cap = 

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()


# Timestamp for debouncing gestures
last_action_time = 0
debounce_time = 1 # 1 second debounce between actions


# Function to apply filters
def apply_filter(frame, filter_type):
    if filter_type == 'GRAYSCALE':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    elif filter_type == 'SEPIA':
        sepia_filter = np.array([[],
                                [],
                                []])

        sepia_frame = cv2.transform(frame, sepia_filter)
        sepia_frame = np.clip() # Clip values to ensure valid range
        return sepia_frame.astype(np.uint8)

    elif filter_type == 'NEGATIVE':
        return 

    elif filter_type == 'BLUR':
        return 

    return frame

while True:
    success, img = cap.read()

    if not success:
        print("Failed to read frame from webcam.")
        break

    img =  # Flip the image for a mirror effect
    img_rgb = 
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, )


            # Get key landmarks
            thumb_tip = hand_landmarks.landmark[]
            index_tip = hand_landmarks.landmark[]
            middle_tip = hand_landmarks.landmark[]
            ring_tip = hand_landmarks.landmark[]
            pinky_tip = hand_landmarks.landmark[]


            # Frame dimensions
            frame_height, frame_width, _ = img.shape

            # Convert normalized coordinates to pixel coordinates
            thumb_x, thumb_y = int( * frame_width), int( * frame_height)
            index_x, index_y = int( * frame_width), int( * frame_height)
            middle_x, middle_y = int( * frame_width), int( * frame_height)
            ring_x, ring_y = int( * frame_width), int( * frame_height)
            pinky_x, pinky_y = int( * frame_width), int( * frame_height)


            # Draw circles for landmarks
            cv2.circle(img, (), 10, (), )
            cv2.circle(img, (), 10, (), )
            cv2.circle(img, (), 10, (), )
            cv2.circle(img, (), 10, (), )
            cv2.circle(img, (), 10, (), )

            # Gesture Logic
            current_time = time.time()

            # Click picture: Thumb touches Index finger
            if abs(thumb_x - index_x) < 30 and abs(thumb_y - index_y) < 30:
                if current_time - last_action_time > debounce_time:
                    cv2.putText(img, , (), cv2.FONT_HERSHEY_SIMPLEX, 1, (), 2)
                    last_action_time = current_time
                    cv2.imwrite(f"{int(time.time())}.jpg", img)
                    print()


            # Change filter: Thumb touches any other finger
            elif (abs(thumb_x - middle_x) < 30 and abs(thumb_y - middle_y) < 30) or \
                (abs(thumb_x - ) < 30 and abs( - ) < 30) or \
                (abs( - ) < 30 and abs(thumb_y - ) < 30):

                if current_time - last_action_time > debounce_time:
                    current_filter = ( + 1) % len(filters)
                    last_action_time = current_time
                    print(f"Switched to filter: {}")



    # Apply the current filter
    filtered_img = apply_filter(img, filters[current_filter])


    # Display the output

    if filters[current_filter] == 'GRAYSCALE':
        cv2.imshow()

    else:
        cv2.imshow()


    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# Release resources
cap.release()
cv2.destroyAllWindows()