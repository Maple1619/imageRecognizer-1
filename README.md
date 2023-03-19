# MINIGAME Story

OKR
|objective|메이플 미니게임 통합인공지능 구축(미니게임스토리)|
|------|------|
|key results1|3월 31일전 마감(minimum 다음 여름방학이벤트 전까지)|
|key results2|게임승률 90%|
|key results3|모든미니게임에 대해 지원가능|


gantt chart
```mermaid
gantt
    dateFormat  YYYY-MM-DD
    section Work
    자료조사 : a1, 2023-01-06, 6d
    화면인식 및 이미지 추출 자료조사 : a2, after a1, 14d
    게임판 이미지 추출 구현 : a3, after a2, 7d
    웹 초기화면 구현:a4, after a3, 7d
    전반적인 웹 문제점 수정:a5, after a4, 7d
    ml모델 구현 자료조사:a6, after a5, 7d
    ml모델 개발:a7, after a6, 15d
    ml모델 학습:a8,after a7, 14d
    기초적인 웹디자인:2023-03-17,7d
    
    section Meeting
    청사진찍기 :2023-01-06, 1d
    자료공유 및 우선순위 : 2023-01-11,  1d
    구현과정 : 2023-02-01, 1d
    중간점검 : 2023-02-08, 1d
    웹 수정 확인 : 2023-02-15, 1d
    ml모델 구현 자료확인: 2023-02-22, 1d
    ml모델 구현 확인 및 웹 연동 자료조사: 2023-03-09, 1d
    ml모델 학습 및 기초적인 웹디자인 확인:2023-03-23,1d
    
    section Othello
    화면인식 및 이미지 추출 자료조사 :  after a1, 14d
    이미지 추출 구현 : after a2, 7d
    ml모델개발 구현(kangshwan): b1, after a3, 14d
    알파고 제로 학습이론에 대한 이해(kangshwan):b2, after a5, 7d
    모델 구현: b3, after b2, 15d
    모델 학습: b4, after b3, 14d
    웹 초기화면 구현(ghrnwjd): c1, after a3, 7d
    전반적인 웹 문제점 수정(ghrnwjd): c2, after c1, 7d
    웹과 모델 연동 자료조사 및 학습: c3, after c2, 22d
    웹 디자인:c4, after c3, 14d

```
