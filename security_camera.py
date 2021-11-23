import cv2
import time
import datetime

# Store video capture in a variable
capture = cv2.VideoCapture(0)

# Load classifiers (requires grayscale image)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Variables
detection = False
detection_stopped_time = None
timer_started = False
t_record_after_detection = 5
# Setting frame size for recording
frame_size = (int(capture.get(3)), int(capture.get(4)))
# Set up Four character code == unique identifier for the specific format our video will be saved as
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# while loop to always update the frame of the webcam
while True:
    _, frame = capture.read()
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Find face and body in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5)

    # Start of program; have not detected body or face
    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime('%m-%d-%Y @ %H-%M-%S')
            # Output stream == (file name, 4 character code, frame rate, frame size)
            out = cv2.VideoWriter(f'{current_time}.mp4', fourcc, 10, frame_size)
            print('Started Recording')
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= t_record_after_detection:
                detection = False
                timer_started = False
                out.release()
                print('Stopped Recording!')
        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)

    # Show or Don't show frame... Case varies
    # cv2.imshow('Camera', frame)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
capture.release()
cv2.destroyAllWindows()
