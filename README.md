# ooo 안녕하세요
# 23.09.04

* 파이토치 프로그래밍 시작!
* 공유에 필요한 정보
* 오늘 배운 내용 
    * torch1 ~ torch6
    * 클래스, 상속(inheritance), 객체지향, 스페셜 메소드(special method), 생성자(constructor),오버라이딩 (overriding), 부모 자식, 깃허브, README 코드에 오늘 배운 내용 정리하는 법, torch, 판다스 불러오기, csv파일 불러오기, 텐서 생성

* 데이터
* 스칼라 (scala)
* 하나의 숫자를 의미
* 벡터 (vector)
* 벡터는 숫자(스칼라)의 배열
* 행렬 (Matrix)
* 2차원의 배열
* 텐서 (tensor)
* 3차원 또는 그 이상의 배열


```python
import torch1
from torch1 import Torch

class PyTorch(Torch):
    def __init__(self, name):
        super().__init__(name)
        self.pyname = 'py최수길'
        
    def __str__(self):
        return '파이네임 : ' + self.pyname+ '\n이름은 :' +self.name
    
    def __eq__(self, value):
        return self.pyname == value.pyname
    
def main():
    t = Torch('최수길')
    t2 = PyTorch('최아무개')
    t3 = PyTorch('최아무개')
    t.print()
    t2.print()
    print(t2)
    # t2.sub_print()
    # print(isinstance(t, object))
    print(t2 == t3)

if __name__ == '__main__':
    main() 
```


```python
import time
def main():
    print('this is test') 
```


# 23.09.05

* 오늘 배운 내용  torch7 ~ torch9
    * 데이터셋 분포
    * 데이터셋 변환
    * 데이터셋 분리
    * 모델 네트워크 생성
    * 모델 클래스의 객체 생성
    * 모델 정확도
    * 모델 재현율
    * 모델 정확도
    * CPU/GPU 사용 지정
    * 지도 학습
        * 분류와 회귀의 차이

    * 분류
        * 데이터 유형 : 이산형 데이터

    * 회귀
        * 데이터 유형 : 연속형 데이터

    * 분류 학습 모델
        * K - 최근접 이웃 (K-Nearest Neighbor)
        * K - 최근접 이웃은 직관적이며 사용하기 쉽기 때문에 초보자가 사용하기 좋고
        * 훈련 데이터를 충분히 확보할 수 있는 환경에서 사용하면 좋다.


# 23.09.06

* 오늘 배운 내용 
    * torch9 ~ torch16
* 지도 학습
    * 서포터 백신 (Support Vector Machine, SVM)
        * 주어진 데이터에 대한 분류, 서포트 벡터 머신은 커널만 적절히 선택한다면 정확도가 상당히 좋기 때문에 정확도를 요구하는 분류 문제를 다룰 때 사용하면 좋고 텍스트를 분류할 때도 사용됨.
    * 결정 트리 (decision tree) 
        * 회귀
            * 변수가 두 개 주어졌을 때 한 변수에서 다른 변수를 예측하거나 두 변수의 관계를 규명하는데 사용하는 방법

* 로지스틱 회귀
    * 로지스틱 회귀
        * 로지스틱 회귀 (Logistic Regression)는 예측 분석을 위한 회귀분석 중에서 특히 종속 변수가 이분형일 때 수행할 수 있는 회귀 분석 기법의 한 종류이다.
        * (로지스틱 회귀) 주어진 데이터에 대한 분류를 함.
        * 분석하고자 하는 대상들이 두 집단 혹은 그 이상의 집단으로 나누어진 경우, 개별 관측치들이 어느 집단으로 분류될 수 있는지 분석하고 이를 예측하는 모형을 개발하는 데 사용되는 통계 기법입니다.
        * 로지스틱 회귀 분석은 주어진 데이터에 대한 확신이 없거나(예를 들어 분류 결과에 대해 확신이 없을 때) 향후 주기적으로 훈련 데이터셋을 수집하여 모델을 훈련시킬 수 있는 환경에서 사용하면 유용합니다.

* 선형 회귀
    * 선형회귀
        * 선형회귀(Linear Regression)는 y=f(x)+ε의 형태로 입력 변수 x와 출력 변수 y 사이의 선형 상관 관계를 모델링하는 분석 기법이다.
        *  (선형회귀) 주어진 데이터에 대한 분류
        * 선형 회귀는 주어진 데이터에서 독립 변수(x)와 종속 변수(y)가 선형 관계를 가질 때 사용하면 유용합니다.

* 비지도 학습
    * 비지도 학습은 레이블이 필요하지 않으며 정답이 없는 상태에서 훈련시키는 방식이다.

* K-평균 군집화
    * 주어진 데이터에 대한 군집화하며 주어진 데이터셋을 이용하여 몇 개의 클러스터를 구성할지 사전에 알 수 있을 때 사용하면 유용하다.

* 밀도 기반 군집 분석 (DBSCAN)
    * 주어진 데어터에 대한 군집화하며 K-평균 군집화와는 다르게 사전에 클러스터의 숫자를 알지 못할 때 사용하면 유용하다.
주어진 데이터에 이상치가 많이 포함되었을 때 사용하면 좋음. (DBSCAN에서는 노이즈를 명확히  정의할 수가 있더느느 장점이 있음.)

* 주성분 분석 (PCA)
    * PCA란, 기존 데이터의 정보를 최대한 살리면서 차원이 축소된 새로운 좌표세계를 만들어서 표현하는 방법이다.
    * 주어진 데이터의 간소화하며 특성 p개를 두세 개 정도로 압축해서 데이터를 시각화하여 살펴보고 싶을 때 유용한 알고리즘이다.

# 23.09.07 
* 오늘 배운 내용 torch17 ~ torch19
    * AND 게이트
        * AND 게이트는 부울 대수의 AND 연산을 하는 게이트로, 두 개의 입력 A와 B를 받아 A와 B 둘 다 1이면 결과가 1이 되고, 나머지 경우에는 0이 된다.

    * OR 게이트
        * OR 게이트는 두입력의 최대값을 구하는 기능을 수행
    * XOR 게이트
        * XOR(exclusive OR) 게이트는 두 개의 입력 A와 B를 받아 입력 값이 같으면 0을 출력하고, 입력 값이 다르면 1을 출력한다.
    * 가중치
        * 노드와 노드 간 연결 강도
    * 바이어스
        * 가중합에 더해 주는 상수로, 하나의 뉴런에서 활성화 함수를 거쳐 최종적으로 출력되는 값을 조절하는 역할을 함
    * 가중합 또는 전달 함수
        * 가중치와 신호의 곱을 합한 것
    * 활성화 함수
        * 신호를 입력받아 이를 적절히 처리하여 출력해 주는 함수
    * 손실함수
        * 가중치 학습을 위해 출력 함수의 결과와 실제 값 간의 오차를 측정하는 함수
    * 심층 신경망
    * 순환 신경망
    * 심층 신뢰 신경망
    * 합성곱 신경망
    * 풀링층
    * 완전연결층
    * 특성 추출 기법
* 딥러닝 
    * 퍼셉트론
        * 인공 신경망에서 이용하는 구조(입력층, 출력층, 가중치로 구성된 구조)로 이루어진 선형 분류기이다.

# 23.09.11
* 오늘 배운 내용 torch19 ~ torch20
* 파라미터 학습 유무 지정
* 함수 생성
* 파라미터 학습 결과 옵티마이저에 전달
* 테스트 데이터를 평가 함수에 적용
* 예측 이미지 출력을 위한 전처리 함수
* 특성 맵 시각화
* 모델 객체화
* tensor.clone() 계산 그래프에 계속 상주
* tensor.datach()계산 그래프에 상주하지 않음
* tensor.clone().detach()계산 그래프에 상주하지 않음


# 23.09.12
* 오늘 배운 내용 torch21 ~ torch22
* 이미지 분류를 위한 신경망
* LeNet-5
* 데이터셋 이미지 출력
* 데이터셋 예측 결과 이미지 출력
* AleNet
* GoogLeNet
* 객체 인식을 위한 신경망
* R-CNN
* 공간 피라미드 풀링
* 이미지 분할을 위한 신경망
* 완전 합성곱 네트워크
    * 합성곱 신경망이라는 개념을 최초로 얀 르쿤이 개발한 구조
    합성곱과 다운 샘플링(혹은 풀링)을 반복적으로 거치면서 마지막에 완전연결층에서 분류를 수행
     * 합성곱 신경망은 은 시각적 영상을 분석하는 데 사용되는 다층의 피드-포워드적인 인공신경망의 한 종류이다. 필터링 기법을 인공신경망에 적용하여 이미지를 효과적으로 처리할 수 있는 심층 신경망 기법으로 행렬로 표현된 필터의 각 요소가 데이터 처리에 적합하도록 자동으로 학습되는 과정을 통해 이미지를 분류하는 기법이다.

```python 
class ImageTransform():
    def __init__(self, resize, mean, std):
        self.data_transfrom = {
            "train" : transforms.Compose([
                transforms.RandomResizedCrop(resize, scale=(0.5, 1.0)),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize(mean, std)
            ]),
            "val" : transforms.Compose([
                transforms.Resize(256),
                transforms.CenterCrop(resize),
                transforms.ToTensor(),
                transforms.Normalize(mean, std)
            ])
        }
    
    def __call__(self, img, phase):
        return self.data_transfrom[phase](img)
```

# 23.09.13
* 오늘 배운 내용 flaskbook/apps/minimalapp
* 파이썬 플라스크 소개
    * 플라스크
        * 마이크로 웹 프레임워크이다.
        * 최소한의 규약만 있어 앱 구성 자유롭게 결정 가능
* 장고
    * 개발에 필요한 많은 기능이 구현되어 있어 풀스택 프레임워크로 불림
    * 파이썬 웹 프레임워크 중에서도 가장 유명하며 중규모 이상 웹을 구축시에 자주 사용
* 보틀
    * 웹 앱을 만들기 위한 프레임워크 중에는 가장 단순함
    * 마이크로 웹 프레임워크 중 하나로 플라스크보다 단순하고 빠르고 가벼움
* FastAPI
    * 빠른 성능을 가진 파이썬 프레임 워크
    * 거의 모든 부분에서 가능한 자동완성
    * 쉽게 뱌우도록 설계 및 적은 문서 읽기 시간 
    * 비동기 지원
* MVT(Model, View, Template) 모델
    * MVT 
        * 웹 프로그래밍 시 일반적으로 언급되는 MVCModel-View-Controller 패턴이란 데이터(Model), 사용자 인터페이스(View), 데이터를 처리하는   로직(Controller)을 구분해서 한 요소가 다른 요소들에 영향을 주지 않도록 설계하는 방식을 의미
    * Model
        * 모델이란 사용될 데이터에 대한 정의를 담고 있는 장고의 클래스
    * View
        * 일반적으로 뷰는 웹 요청을 받아서 데이터베이스 접속 등 해당 애플리케이션의 로직에 맞는 처리를 하고 그 결과 데이터를 HTML로 변환하기 위해 템플릿 처리를 한 후 최종 HTML로 된 응답 데이터를 웹 클라이언트로 반환합니다.
    * Template
        * 장고가 클라이언트에게 반환하는 최종 응답은 HTML 텍스트입니다. 개발자가 응답에 사용할 *.html 파일을 작성하면 장고는 이를 해석해서 최종 HTML 텍스트 응답을 생성하고 이를 클라이언트에게 보냅니다. 클라이언트(보통 웹 브라우저)는 응답으로 받은 HTML 텍스트를 해석해서 우리가 보는 웹 브라우저 화면에 UI를 표시합니다. 이러한 과정에서 개발자가 작성하는 *.html 파일을 템플릿이라 부르며 이 파일에 화면에 표시되는 UI를 템플릿 문법에 맞게 작성합니다.
* flask run 명령어 실행하기
* 디버그 모드
* Rule에 변수 지정하기
* 쿠키
* 세션
* 응답

# 23.09.14
* 오늘 배운 내용 
* 데이터베이스를 이용한 앱 만들기
* CRUD 앱의 모듈 작성하기
* Blueprint
* 데이터베이스 조작하기
* 데이터베이스를 사용한 CRUD 앱 만들기
* 템플릿의 공통화와 상속
* config 설정하기
* *flask-sqlalchemy
* flask-migrate
* flask-wtf

# 23.09.18
* flask-login
    * is_authenticated 로그인 시는 true를 반환하고 미로그인시는 false를 반환하는 함수이다.
    * is_active 사용자 계정이 활성 상태인지에 대한 boolean 반환
    * is_anonymous	로그인 사용자는 false를 반환하고 익명 사용자는 true를 반환하는 함수
    * get_id 로그인 사용자의 유니크 ID
* 릴레이션십
    * backref	다른 모델에 대해서 양방향으로 릴레이션함
    * lazy	관련한 객체를 지연하여 취득하는 옵션 디폰트는 select이며 다른 옵션에는 immediate, joined, subquery,noload, dynamic 등 옵션이 있음
    * order_by	정렬할 컬럼을 지정함

# 23.09.19
* 오늘 배운 내용
* flaskbook/apps | flaskbook/apps/detector
    * detector/index.html
    ```python 
    <div class="dt-image-username">{{ user_image.User.username }}</div>
<div class="dt-image-username">{{ user_image.UserImage.user_image_name }}</div>
```

# 23.09.20
* torch23 ~ torch26
* 시계열 분석
    * 독립 변수를 사용하여 종속 변수를 예측하는 일반적인 머신 러닝에서 시간을 독립 변수로 사용함
* ARIMA 모델
    * 자기회귀 이동평균 모델은 자기회귀 모델(AR)과 이동평균 모델(MA)을 융합하여 모형화한 수학적 모델이다. 
    * (자기 회귀와 이동 평균을 둘 다 고려하는 모형)
    * ARMA와 달리 과거 데이터의 선형 관계뿐만 아니라 추세까지 고려한 모델
    * 절차 
    * p: 자기 회귀 차수
    * d: 차분 차수
    * q: 이동 평균 차수
    * fit() 
    * predict()
* 순환 신경망 
    * 시계열은 일정 시간 간격으로 배치된 데이터들의 수열을 말한다
    * (시간적으로 연속성이 있는 데이터를 처리하려고 고안된 인공 신경망)
    * RNN의반복되는 이전 은닉층이 현재 은닉층의 입력이 되면서 반복되는 순환 구조를 갖는다는 의미
    * 기존 네트워크와의 차이점은 기억(memory)을 갖는다는 것이다.
* RNN의 셀 유형
    * nn.RNNCell
    * nn.GRUCell
    * nn.LSTMCell
* RNN 계산
    * 은닉층 계산
* 출력층 계산
    * 심층 신경망과 계산 방법이 동일
* 오차 (E)
* 역전파

# 23.09.22
* torch26 ~ torch31
* LSTM
    * 순전파
        * 기울기 소멸 문제를 해결하기 위해 망각, 입력, 출력 게이트라는 새로운 요소를 은닉층의 각 뉴런의 추가함
    * 망각 게이트
        * 과거 정보를 어느 정도 기억할지 결정
        * 과거 정보와 현재 데이터를 입력받아 시그모이드를 취한 후 그 값을 과거 정보에 곱함
        * 시그모이드의 출력이 0이면 과거 정보를 버리고, 1이면 과거 정보는 온전히 보존
    * 입력 게이트
        * 현재 메모리에 새로운 정보를 반영할지 결정하는 역할을 함
    * 셀
        * 각 단계에 대한 은닉 노드(hidden node)를 메모리 셀이라 함
        * 총합(sum)을 사용하여 셀 값을 반영, 이것으로 기울기 소면 문제 해결
        * 셀 업데이트
            * 망각 게이트와 입력 게이트의 이전 단계 셀 정보를 계산, 현재 단계의 셀 상태를 업데이트
    * 출력 게이트
        * 과거 정보와 형재 데이터를 사용하여 뉴런의 출력을 결정
    * 역전파
        * LSTM은 셀을 통해 역전파를 수행하기 때문에 중단없는 기울기(uninterrupted gradient flow)라고도 함
    * GRU 
        * 별도의 업데이트 게이트로 구성
        * 망각 게이트
        * 업데이트 게이트
        * 후보군
        * 은닉층 계산
    * 양방향 RNN / 양방향 LSTM
        * 하나의 출력 값을 예측하는 데 메모리 셀 두 개를 사용
        * 첫 번째 메모리 셀은 이전 시점의 은닉 상태(forward state)를 전달받아 현재의 은닉 상태를 계산
        * 두 번째 메모리 셀은 다음 시점의 은닉 상태(backward state)를 전달받아 현재의 은닉 상태를 계산
        * 값 두 개를 모두 출력층에서 출력 값을 예측하는 데 사용

# 23.09.25
* torch31 ~ torch34
* 성능 최적화
    * 조기 종료를 이용한 성능 최적화
        * 조기 종료(early stopping)는 뉴럴 네트워크가 과적합을 회피하는 규제 기법
        * 훈련 데이터와 별도로 검증 데이터를 준비, 매 에포크마다 검증 데이터에 대한 오차(validation loss)를 측정하여 모델의 종료 시점 제어
        * 과적합이 발생하기 전까지 학습에 대한 오차(training loss)와 검증에 대한 오차 모두 감소하지만, 과적합이 발생하면 훈련 데이터셋에 대한 오차는 감소하는 반면 검증 데이터셋에 대한 오차는 증가, 따라서 조기 종료는 검증 데이터셋에 대한 오차가 증가하는 시점에서 학습을 종료하도록 조정
* 자연어 처리
    * 우리가 일상생활에서 사용하는 언어 의미를 분석하여 컴퓨터가 처리할 수 있도록 하는 과정
    * 영어는 명확한 띄어쓰기가 있지만, 중국어는 띄어쓰기가 없기에 단어 단위의 임베딩이 어려움
    * 인간 언어에 대한 이해도 필요하며, 언어 종류가 다르고 그 형태가 다양하기 때문에 처리가 매우 어렵다.

* 자연어 처리 용어
    * 말뭉치 (corpus(코퍼스))
        * 자연어 연구를 위해 특정한 목적에서 표본을 추출한 집합
    * 토큰 (token)
        * 자연어 처리를 위한 문서는 작은 단위로 나누어야 하는데, 이때 문서를 나누는 단위가 토큰
    * 토큰화 (tokenization)
        * 텍스트를 문장이나 단어로 분리하는 것
    * 불용어 (stop words)
        * 분석과 관계없으며, 자주 등장하는 빈도 때문에 성능에 영향을 미치므로 사전에 제거
            * 불용어 예로 a, the, she, he 등이 있음
    * 어간 추출 (stemming)
        * 단어를 기본 형태로 만드는 작업
    * 품사 태깅 (part-of-speech tagging)
        * 주어진 문장에서 품사를 식별하기 위해서 붙여 주는 태그(식별 정보)를 의미

