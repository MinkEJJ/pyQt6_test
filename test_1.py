import sys
from PyQt6.QtWidgets import (QHBoxLayout,QRadioButton,QWidget,QVBoxLayout,QApplication,QPushButton,QMainWindow,QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,QLineEdit, QSpinBox, QDoubleSpinBox, QSlider)
#from PyQt6.QtCore import QSize,Qdt # 작동오류가 나타나는 이유를 찾아야함.
#from layout_colorwidget import Color # 레이아웃을 제작하려면 필요한 모듈

class Myapp (QWidget):
    def __init__(self):
        super(Myapp, self).__init__()
        self.setWindowTitle("당신의 오늘 하루 어떠신가요?")
        self.initUi()
        
        
    
    def initUi(self):
        l1 = QLabel('당신의 오늘 하루 어떠신가요?',self)
        l1.move(500,500)
        emotion = QLineEdit(self)
        rb = QRadioButton('ex',self)
        button = QPushButton('ex')
        lay0 = QHBoxLayout()
        layout = QVBoxLayout()
        
        lay0.addSpacing(100)
        lay0.addLayout(layout)
        # lay0.addSpacing(100)
        
        layout.addSpacing(100)
        layout.addWidget(l1)
#        layout.addSpacing(100)
        layout.addStretch(1)
        layout.addWidget(emotion)
        layout.addStretch(1)
#        layout.addSpacing(100)
        layout.addWidget(rb)
        layout.addStretch(1)
#        layout.addSpacing(100)

        layout.addWidget(button)
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