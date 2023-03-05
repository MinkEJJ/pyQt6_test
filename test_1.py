import sys
from PyQt6.QtWidgets import (QHBoxLayout,QRadioButton,QWidget,QVBoxLayout,QApplication,QPushButton,QMainWindow,QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,QLineEdit, QSpinBox, QDoubleSpinBox, QSlider)
import requests
import json

class Myapp (QWidget):
    def __init__(self):
        super(Myapp, self).__init__()
        self.setWindowTitle("당신의 생각은?")
        self.initUi()
         
    def the_button_was_clicked(self): #버튼 클릭시 생기는 상세 이벤트
        self.button.setText("loading..")# 버튼의 글씨가 바뀜
        self.button.setEnabled(False)# 버튼 비활성화 : 연속 두번 실행을 방지
        self.setWindowTitle("실행중")# 윈도우 타이틀도 실행중으로 변함
        a=self.emotion.text()
        client_id = ""
        client_secret = ""
        url="https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze"
        headers = {
            "X-NCP-APIGW-API-KEY-ID": client_id,
            "X-NCP-APIGW-API-KEY": client_secret,
            "Content-Type": "application/json"
            }

        # 텍스트 파일에서 문자열 받아오기
        file_path = "파일의 절대경로 입력"
        with open(file_path, "r", encoding="UTF-8") as file:
            tmp = file.read()
        # tmp에서 행바꿈(\n)을 제거한 문자열을 content에 저장
        content = tmp.replace("\n", "")
        data = {
        "content": content
        }

        response = requests.post(url, data=a, headers=headers)
        rescode = response.status_code
        if(rescode == 200):
            # string(response.text) > dictionary로 자료형 변경
            json_object = json.loads(response.text)
            print(json_object["document"]['sentiment'])
            
        else:
            print("Error : " + response.text)
        
        
    
    def initUi(self):
        l1 = QLabel('당신을 위한 작품을 추천드립니다. 하단의 나의 기분을 적어봅시다. [작품 추천 프로그램 로고]',self)
        l1.move(500,500)
        self.emotion = QLineEdit(self)
        #self.emotion.setText("Hello!")
        rb = QRadioButton('개인정보 수집,이용에 대한 동의 / 동의함',self) #개인정보 동의함 디자인 구현
        self.button = QPushButton("전송")
        self.button.clicked.connect(self.the_button_was_clicked)#버튼 클릭시 연결되는 이벤트
        #self.setCentralWidget(self.button) #버튼이 화면 정중앙에 위치
       

        lay0 = QHBoxLayout()
        layout = QVBoxLayout()
        
        lay0.addSpacing(100)
        lay0.addLayout(layout)
        # lay0.addSpacing(100)
        
        layout.addSpacing(100)
        layout.addWidget(l1)
#        layout.addSpacing(100)
        layout.addStretch(10)
        layout.addWidget(self.emotion)
        layout.addStretch(1)
#        layout.addSpacing(100)
        layout.addWidget(rb)
        layout.addStretch(10)
#        layout.addSpacing(100)

        layout.addWidget(self.button)
        layout.addSpacing(100)
        
        self.setLayout(lay0)
#        self.resize(1000,1000)
        self.setGeometry(0,0,2000,1000)
        self.show()
        


        
        #self.input_user()
    
    # def input_user(self):
    #     l1 = QLabel('당신의 오늘 하루 어떠신가요?',self)
    #     l1.move(10,10)
    #     l1font = l1.font()
    #     l1font.setPointSize(20)
    #     layout = QVBoxLayout()
    #     layout.addWidget(l1)
    #     self.setLayout(layout)
    #     self.setGeometry(500,500,500,500)
    #     self.show()

                #input레이블
"""
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        #layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)
    
        self.button = QPushButton("전송") # 로그램 실행시 사용자에게 보여지는 UI화면
        self.button.clicked.connect(self.the_button_was_clicked)#버튼 클릭시 연결되는 이벤트
        self.setCentralWidget(self.button) #버튼이 화면 정중앙에 위치

    def the_button_was_clicked(self): #버튼 클릭시 생기는 상세 이벤트
        self.button.setText("loading..")# 버튼의 글씨가 바뀜
        self.button.setEnabled(False)# 버튼 비활성화 : 연속 두번 실행을 방지
        self.setWindowTitle("실행중")# 윈도우 타이틀도 실행중으로 변함
 """       



"""
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("당신의 오늘 하루 어떠신가요?")

        layout = QVBoxLayout()
        
        self.button = QPushButton("전송") # 로그램 실행시 사용자에게 보여지는 UI화면
        self.button.clicked.connect(self.the_button_was_clicked)#버튼 클릭시 연결되는 이벤트
        self.setCentralWidget(self.button) #버튼이 화면 정중앙에 위치

    def the_button_was_clicked(self): #버튼 클릭시 생기는 상세 이벤트
        self.button.setText("loading..")# 버튼의 글씨가 바뀜
        self.button.setEnabled(False)# 버튼 비활성화 : 연속 두번 실행을 방지
        self.setWindowTitle("실행중")# 윈도우 타이틀도 실행중으로 변함
        

        #input레이블

        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        #layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)



        # 버튼 레이
"""    


        
        
"""
#텍스트 레이블
        widget = QLabel("당신의 지금 기분은 작성해보세요")
        font = widget.font()
        font.setPointSize(15)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setCentralWidget(widget)
       """

    
     
"""      
    def the_button_was_toggled(self,checked):
        print("clicked!?",checked)
"""

app = QApplication(sys.argv)
ex = Myapp()
sys.exit(app.exec())