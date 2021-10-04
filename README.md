

**&#x1F4D9; 2020 KU 스마트 캠퍼스 해커톤**
---------------------------------------------------
#### SK미래관 SSS지수 분석 앱 개발: 개인 맞춤형 학습공간 추천 시스템
**최우수상 수상작**

![Alt text](https://raw.githubusercontent.com/Soyeon-ErinLee/KU-2020-SMART-CAMPUS-DATATHON/master/SSS.png)
--------------------------------------------------------------------------------------------------


###### ➊ Code 폴더 - App개발 코드(Pycharm, .py, .kivy) 폴더

* 해당 폴더는 앱 개발을 위해 사용된 코드와 이미지 파일로 
앱을 실행시키기 위해서는 'App개발 코드' 폴더를 한 번에 다운 받아야 함. 
폴더에 존재하는 "main.py" 파일에 앱을 실행하기 위한 메인 소스 코드가 포함되어 있으며, 
이를 실행하기 위해선 아래 메뉴얼을 참고.

   1. Anaconda 3 다운로드 및 설치 (https://www.anaconda.com/distribution/)

   2. Anaconda prompt를 실행하여 가상환경에 kivy 설치
   
      프롬프트 창에 아래 코드를 작성할 것.

      conda create -n my_python_env
      activate my_python_env
      conda install kivy -c conda-forge

   3. Pycharm 다운로드 및 설치 (https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)

      설치 시 설치 옵션에서 create associations-.py의 박스에 체크할 것.

   4. Pycharm 실행 - Settings - Project Interpreter 설정

   5. 추가 버튼을 클릭하여 conda environment - existing environment 선택 - 
      interpreter 경로는 users/이름/Anaconda3/envs/my_python_env(가상환경)/python.exe

   6. New projects 생성 - 'App 개발 코드' 폴더를 경로로 설정, 그중 main.py 파일 불러오기

   7. main.py 파일 실행 시 구현된 애플리케이션이 구동되는 것을 확인할 수 있음.


#####################################################################################


###### ➊ Code 폴더 -  Google Colab 데이터 분석 코드(.ipynb) 폴더 

* 해당 폴더 내 파일들은 .ipynb 형식의 파일로, Google drive 내 Google Colaboratory를 통해 실행하거나, Anaconda 3의 Jupyter(Notebook / Lab)을 사용하여 열람해야 함. (Google Colab 사용 권장) 기본적으로 실행되어있는 상태이며, 재실행을 원할 경우 코드 왼쪽의 PLAY 버튼을 클릭할 것 *

   [Converting API data to csv.ipynb]

      iot.api(https://datahubapi.korea.ac.kr/datathon/iot) 를 통해 실시간으로 업데이트되는 API 데이터를 가공하고 구현된 파이썬 코드와 호환되도록 .csv 파일로 저장하는 코드

   [Crawling Weather Data.ipynb]

      기상청에서 실시간으로 배포하는 성북구 안암동의 온도 및 습도를 크롤링하기 위해 사용되는 코드

   [Data Preprocessing.ipynb]

      제공된 SK 미래관 내 IoT 센서 데이터를 통합한 "data.csv"파일로 데이터 전처리 및 EDA를 시행한 코드. 
      co2, dust, temperature, humidity 변수의 분포 측정, '시간'과 'Floor' 변수 추가를 통해 시간별, 층별 그룹화 진행.
      각 변수의 분포 시각화, 상관 관계 분석 및 PCA, 층별 다중비교를 위한 Tukey's HSD test 등 변수의 전반적인 특성을 파악하고 시각화하기 위한 코드.

   [Regression with Weather Data.ipynb]

      크롤링한 기상청 온/습도 데이터만으로 기타 학습 공간의 온/ 습도를 추정하는 회귀식을 적합해보기 위해 사용된 코드

   [Regression Time Series AR(8) Model vs Weather + Each Variable + Mean.ipynb]★

      기타 학습 공간의 온/습도 데이터를 주변 학습 공간의 온/습도 데이터와 기상청 온/습도 데이터로 추정하는 회귀식을 적합하기 위해서 사용된 코드. 
      시계열 AR(8) 모형을 사용하여 적합한 식과 'Weather + Each Variable + Mean' 모형의 비선형 회귀식을 비교.
      이밖의 다른 코드들에서 적합된 회귀식과도 비교. Stepwise Selection을 통해 가장 낮은 AIC를보이는 'Weather + Each Variable + Mean' 모델이 최종적으로 선정되었음. 
      즉, 최종적으로 선택된 회귀식은
      '기타 학습 공간의 온도/습도 ~ 기상청 데이터를 통해 수집된 성북구 안암동의 온도/습도 + 주변 공간의 온도/습도 + 주변 공간의 온도/습도의 평균'이다.

   [Regression with Interaction.ipynb]

      기타 학습 공간의 온/습도 데이터를 주변 학습 공간의 온/습도 데이터와 기상청 온/습도 데이터로 추정하는 회귀식을 적합하기 위해서 사용된 코드. 
   [Regression with Mean Variable.ipynb] 코드에서 적합한 회귀식에 추가적으로 기상청 온/습도 데이터와 주변 학습 공간 데이터의 교호 작용 (Interaction Term) 변수를 추가함.

   [Regression with Mean Variable.ipynb]

      기타 학습 공간의 온/습도 데이터를 주변 학습 공간의 온/습도 데이터와 기상청 온/습도 데이터로 추정하는 회귀식을 적합하기 위해 사용된 코드.
      여기서 Mean Variable은 "주변공간.txt" 파일에서 정의된 각 기타 학습공간에 대응되는 '주변 학습 공간'의 온도 및 습도의 평균으로 만들어진 새로운 변수를 의미함. 

   [SSS지수 개발작업(with 0616 data).ipynb]

      2020년 6월 16일의 IoT 센서 데이터를 예시로, SSS지수를 계산하는 코드. 
      음수값, 지나치게 큰 값 들을 제거하는 이상치 제거 코드, 사용자 맞춤형 가중치 계산 코드, 
      각 점수화 알고리즘에 따라 환경 변수에 점수를 부여하는 코드,
      그리고 환경 변수들의 점수를 가중평균하여 SSS지수를 계산하는 코드가 포함되어 있음.
      결과물로 '0616SSSdata.csv' 파일이 출력되도록 코딩되어있음.

   [SSS지수 시각화 구현(with 0616 17시 data).ipynb]★

      앞서 [SSS지수 개발작업(with 0616 data).ipynb]의 결과물인 "0616SSSdata.csv"파일과 "0616weather_data.csv"파일을 불러와 2020년 6월 16일 5시 SK 미래관 내부 캐럴실 및 스터디룸과 기타 학습 공간의 SSS지수를 약도 위에 시각화하여 나타내는 코드.
      각 기타 학습 공간의 SSS지수는 앞서 구현된 회귀 모형에 의해 예측된 값.
      이 프로젝트의 가장 메인 코드

   [T-test comparison(humidity).ipynb]

      "data_for_regression.csv" 파일의 데이터를 통해 2020년 8월 11일 5시경 아두이노 장치를 통하여 직접 측정한 각 기타 학습 공간의 온도와 SK 미래관 IoT 센서 API를 통해 측정된 스터디룸 및 캐럴실의 습도에 차이가 있는지 알아보기 위해 T-test를 적용한 코드.

   [T-test comparison(temperature).ipynb]

      "data_for_regression.csv" 파일의 데이터를 통해 2020년 8월 11일 5시경 아두이노 장치를 통하여 직접 측정한 각 기타 학습 공간의 온도와 SK 미래관 IoT 센서 API를 통해 측정된 스터디룸 및 캐럴실의 온도에 차이가 있는지 알아보기 위해 T-test를 적용한 코드.


   #########################################################################################


###### ➊ Code 폴더 - 기타 코드(.R, .ino) 폴더

   * 해당 폴더 내 파일은 아두이노 장치를 통한 '기타 학습 공간' 온/습도 측정을 위해 사용된 .ino 코드와 
   회귀 모형 최적화를 위한 Quadratic Programming 실행용 R 코드로 구성됨.
   .ino 파일의 경우 Wemos 온습도 측정 전용 드라이버와 라이브러리를 설치해야 하며,
   R 코드의 경우 R 또는 R Studio를 설치하여 실행해야 함.

   [code.ino]
   
      아두이노 장치를 통해 SK 미래관 내 온/습도를 직접 측정하기 위한 실행 코드

   [Quadratic Programming.R]

      QP Solver를 이용하여 회귀식의 손실함수를 최적화하기 위해서 사용된 코드

   [stop.ino]
  
      아두이노 장치를 통한 센서 측정을 중지하기 위한 코드

   [WiFiClient.ino]
   
      아두이노 장치를 무선 와이파이와 연결하는 클라이언트 코드


#########################################################################################


###### ➊ Images 폴더

   [floorB1-final.png ~ floor5-final.png]

      보다 사용자 친화적인 UI와 직관적인 시각화를 위해 도면을 기반으로 직접 그린 약도 이미지 파일.
      이후 SSS 지수 시각화를 위해 필요.


#######################################################################################


###### ➊ Raw Data(.csv or .txt) 폴더

* 프로젝트에 사용한 모든 Raw Data. 열람하기 위해선 엑셀, 메모장, 또는 .csv / .txt 전용 리더가 필요하다.*

   [0616SSSdata.csv]

      6월 16일 자의 iot 센서 데이터에 계산된 온도, 습도, co2, dust 각각의 점수와 이를 통해 계산된 SSS지수를 컬럼으로 추가한 데이터 파일.
      "SSS지수 시각화 구현(with 0616 17시 data).ipynb" 파일을 실행시키기 위해 필요.

   [0616weather_data.csv]

      직접 크롤링한 6월 16일자 기상청 온도 및 습도 측정 데이터.
      "SSS지수 시각화 구현(with 0616 17시 data).ipynb" 파일을 실행시키기 위해 필요.

   [0811weather_data.csv]

      직접 크롤링한 8월 11일자 기상청 온도 및 습도 측정 데이터.
      SK 미래관 내 '기타 학습 공간' 환경 변수(온/습도) 예측 모형을 구축할 때 사용하였던 데이터이다.

   [data.csv]

      .txt 파일로 제공받은 여러 IoT 센서 데이터 파일을 합하여 가공하기 쉬운 형식의 .csv 파일로 통일한 파일

   [data_for_regression.csv]

      SK 미래관 내 기타 학습 공간의 환경 변수(온/습도)를 예측하는 회귀식을 적합하기 위해 사용된 데이터. 
      2020년 8월 11일 각 기타 학습 공간에서 30분씩 아두이노 장치를 통해 직접 측정한 데이터와 동시간대에 SK 미래관 IoT 센서 API에서 측정된 강의실 데이터를 병합해놓은 파일.

   [iot_11_5322.txt ~ iot_11_5325.txt]

      2020.06-2020.07 에 측정된 SK 미래관 iot 센서 데이터.

   [iot_11_26.txt ~ iot_11_34.txt]

      2020.01-2020.03 에 측정된 SK 미래관 iot 센서 데이터.

   [roompixel.txt]

      자체 제작한 SK 미래관 내 약도 (Images 폴더 내 png 파일 참조) 위에 SSS지수를 시각화하기 위해 각 학습 공간(강의실, 기타 학습 공간 등)과 약도 내 픽셀 값을 매칭시킨 텍스트 파일. 이후 SSS지수 시각화 코드 작동 위해 필요.

   [주변공간.txt]

      기타 학습 공간의 환경 변수를 예측 할 때 필요한 '주변 학습 공간'을 정의해 놓은 파일.
      각 기타 학습 공간과 그 주변에 존재하는 학습 공간(캐럴실 및 스터디룸)을 매칭하여 정리해놓은 파일.


#######################################################################################
