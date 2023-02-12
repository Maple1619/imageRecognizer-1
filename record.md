# record


1. Othello
2. Find the wrong picture
3. Pyramid
4. Onecard
5. web, ui, db

**Team members**

kangshwan(개발자, 팀장),  honorrrrulru(PM),  ghrnwjd(개발자)

## 회의 내용

### 2023-01-06

팀장이 생각하는 프로그램의 이미지 공유 
거기에 대한 자료조사 실시
최종 완료: 3월 말

### 2023-01-11

자료 공유

진행 순서 정하기
  1. Othello
  2. Find the wrong picture
  3. Pyramid
  4. Onecard
  5. web, ui, db
  
  
  
**Othello**

완성된 진행과정 이미지 공유

          사진업로드
          사진업로드
<img width="{50%}" src="{https://user-images.githubusercontent.com/62336155/218310493-ce7be22d-a0c1-4191-8c42-5d5cb5af48b4.PNG}"/>
<img width="{50%}" src="{https://user-images.githubusercontent.com/62336155/218310500-9dee224b-9ab1-4584-966a-61740f9212f9.PNG}"/>


화면 인식 및 이미지추출 자료조사 및 구현(kangshwan,ghrnwjd)

### 2023-02-01

이미지 추출 구현과정 공유

kangshwan

이미지 업로드 - 이미지의 흑백화 - 세로필터와 가로필터를 통해 게임판을 추출 - 추출한 게임판을 가지고 막힌 장소를 값으로 변환하여 게임 값을 가져옴 - 게임값을 웹페이지 게임판으로 변환
 
            사진업로드
 
ghrnwjd
 
이미지 업로드 - 이미지에서 게임판을 추출 - 게임판을 8X8로 변환 - 각 칸의 중간 부분 RGB값 가져옴 - 그중 RGB값이 다른 칸들보다 극히 낮은 점은 막핀장소라 판단하여 게임값을 가져옴 -게임값을 웹페이지 게임판으로 변환

            사진업로드

ml모델개발 및 웹 초기화면 구현 진행
  1) 웹 초기화면 구현 시 게임값에 따라 게임판 생성
  2) 이미지업로드 구현

### 2023-02-08

중간 점검

초기 웹페이지 구현 (ghrnwjd)

진행 과정 공유
 
웹 페이지 수정사항 및 오류 수정
  1) 이미지 업로드 시 업로드된 이미지 지우기
  2) 이미지 업로드 후 게임이 끝날때 까지 이미지 재업로드 막아두기
  3) 선공, 후공 체크 박스 생성
  4) 되돌리기버튼 생성 및 오류수정 
  **5) 최종완성날짜 연장 4월말~5월초 정도로 생각중**
  
 
