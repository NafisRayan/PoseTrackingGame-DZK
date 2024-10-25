import cv2
import mediapipe as mp
import math
import random
import time

# Initialize MediaPipe's hand detection and landmark models
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

# Capture video from the default camera
cap = cv2.VideoCapture(0)

# Circle parameters
circle_radius = 30
circle_center = (0, 0)
circle_visible = False
circle_appear_time = 0

# Function to generate a random position for the circle
def generate_random_position(frame_width, frame_height):
    x = random.randint(circle_radius, frame_width - circle_radius)
    y = random.randint(circle_radius, frame_height - circle_radius)
    return (x, y)

while True:
    # Read each frame from the video capture object
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to RGB format
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmarks using MediaPipe's hand detection model
    results = hands.process(image)

    # Check if any hand landmarks are detected
    if results.multi_hand_landmarks is not None:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the image
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4),
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
            )

            # Get the coordinates of the index finger tip
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_tip_x = int(index_tip.x * frame.shape[1])
            index_tip_y = int(index_tip.y * frame.shape[0])

            # Calculate the distance between the index finger tip and the circle center
            distance = math.dist((index_tip_x, index_tip_y), circle_center)

            # Check if the index finger is extended and touches the circle
            if index_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and distance <= circle_radius:
                # Display "IN" in the right bottom corner
                cv2.putText(frame, "IN", (frame.shape[1] - 70, frame.shape[0] - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                # Display "OUT" in the right bottom corner
                cv2.putText(frame, "OUT", (frame.shape[1] - 70, frame.shape[0] - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    current_time = time.time()

    # Check if the circle should appear or disappear
    if circle_visible:
        # Check if the circle should disappear
        if current_time - circle_appear_time >= 3:
            circle_visible = False
    else:
        # Check if the circle should appear
        if current_time - circle_appear_time >= 3:
            circle_visible = True
            circle_center = generate_random_position(frame.shape[1], frame.shape[0])
            circle_appear_time = time.time()

    # Draw the green circle if it is visible
    if circle_visible:
        cv2.circle(frame, circle_center, circle_radius, (0, 255, 0), -1)

    # Display the resulting frame
    cv2.imshow('Hand Landmark Detection', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()