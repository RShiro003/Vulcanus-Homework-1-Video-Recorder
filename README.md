# 🎥 OpenCV 비디오 레코더

OpenCV를 사용하여 웹캠 영상을 **실시간으로 표시하고 녹화**할 수 있는 프로그램입니다.  
또한 **영상 회전 및 스크린샷 저장 기능**이 포함되어 있습니다.

![녹화 화면](images/recording_preview.png)

---

## **✨ 주요 기능**
✅ **카메라 영상 미리보기** – 실시간으로 웹캠 화면 표시  
✅ **비디오 녹화** – `Space` 키를 눌러 녹화 시작/중지  
✅ **영상 회전** – `R` 키를 눌러 90도씩 회전 (0 → 90 → 180 → 270 → 0)  
✅ **스크린샷 저장** – `S` 키를 눌러 현재 화면을 이미지로 저장  
✅ **자동 파일명 생성** – 저장 시 날짜와 시간을 포함한 파일명 생성  
✅ **녹화 중 표시** – 녹화 중일 때 **빨간 점** 표시  
✅ **`ESC` 키로 프로그램 종료**  

---

## **🎮 조작 방법**
| 키 | 기능 |
|----|------|
| `Space` | 녹화 시작 / 중지 |
| `R` | 영상 90도 회전 (0 → 90 → 180 → 270 → 0) |
| `S` | 현재 화면 스크린샷 저장 |
| `ESC` | 프로그램 종료 |

---

## **🛠 설치 방법**
1. Python 패키지 설치:
   ```bash
   pip install opencv-python
