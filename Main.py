import cv2
import datetime
import os  # 스크린샷 저장 폴더 생성용

# 카메라 캡처 객체 생성
cap = cv2.VideoCapture(0)

# 비디오 저장을 위한 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정
fps = 20.0  # 프레임 속도
frame_size = (int(cap.get(3)), int(cap.get(4)))  # 해상도 가져오기
output = None  # 녹화 파일 객체

# 모드 변수
recording = False
rotate_mode = 0  # 회전 상태 저장 (0도, 90도, 180도, 270도)

# 스크린샷 저장 폴더 만들기
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 🔹 회전 적용
    if rotate_mode == 90:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    elif rotate_mode == 180:
        frame = cv2.rotate(frame, cv2.ROTATE_180)
    elif rotate_mode == 270:
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # 🔹 현재 모드 표시 (녹화 중일 때 빨간 원)
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
            # 🔹 녹화 파일 생성 (해상도는 회전 상태에 따라 변경 필요)
            filename = f'recordings/recording_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.avi'
            if rotate_mode in [90, 270]:  # 90도 또는 270도 회전 시 해상도 변경
                frame_size = (frame_size[1], frame_size[0])
            output = cv2.VideoWriter(filename, fourcc, fps, frame_size)
        else:
            # 녹화 중지
            output.release()
            output = None

    # 🔹 R 키를 누르면 90도씩 회전
    elif key == ord('r'):
        rotate_mode = (rotate_mode + 90) % 360  # 90도씩 증가, 360도 넘어가면 0도로 리셋
        print(f"영상 회전: {rotate_mode}도")

    # 🔹 S 키를 누르면 스크린샷 저장
    elif key == ord('s'):
        screenshot_filename = f'screenshots/screenshot_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
        screenshot_frame = frame.copy()

        # 회전된 상태로 저장
        if rotate_mode == 90:
            screenshot_frame = cv2.rotate(screenshot_frame, cv2.ROTATE_90_CLOCKWISE)
        elif rotate_mode == 180:
            screenshot_frame = cv2.rotate(screenshot_frame, cv2.ROTATE_180)
        elif rotate_mode == 270:
            screenshot_frame = cv2.rotate(screenshot_frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        cv2.imwrite(screenshot_filename, screenshot_frame)
        print(f"📸 스크린샷 저장 완료: {screenshot_filename}")

    # 🔹 녹화 중이면 회전된 프레임 저장
    if recording and output is not None:
        rotated_frame = frame.copy()
        if rotate_mode == 90:
            rotated_frame = cv2.rotate(rotated_frame, cv2.ROTATE_90_CLOCKWISE)
        elif rotate_mode == 180:
            rotated_frame = cv2.rotate(rotated_frame, cv2.ROTATE_180)
        elif rotate_mode == 270:
            rotated_frame = cv2.rotate(rotated_frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        output.write(rotated_frame)  # 회전된 프레임 저장

cap.release()
if output:
    output.release()
cv2.destroyAllWindows()
