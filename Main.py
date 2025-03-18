import cv2
import datetime

# 카메라 캡처 객체 생성
cap = cv2.VideoCapture(0)

# 비디오 저장을 위한 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정
fps = 20.0  # 프레임 속도
frame_size = (int(cap.get(3)), int(cap.get(4)))  # 해상도 가져오기
output = None  # 녹화 파일 객체

# 모드 변수
recording = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 현재 모드 표시 (녹화 중일 때 빨간 원)
    if recording:
        cv2.circle(frame, (50, 50), 10, (0, 0, 255), -1)

    cv2.imshow('Video Recorder', frame)

    # 키 입력 처리
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC 키로 종료
        break
    elif key == 32:  # Space 키로 녹화 모드 전환
        recording = not recording
        if recording:
            # 녹화 파일 생성
            filename = f'recordings/recording_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.avi'
            output = cv2.VideoWriter(filename, fourcc, fps, frame_size)
        else:
            # 녹화 중지
            output.release()
            output = None

    # 녹화 중이면 프레임 저장
    if recording and output is not None:
        output.write(frame)

cap.release()
if output:
    output.release()
cv2.destroyAllWindows()
