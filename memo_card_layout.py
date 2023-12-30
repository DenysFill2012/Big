from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QTableWidget, QListWidget, QListWidgetItem,
       QLineEdit, QFormLayout,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QButtonGroup, QRadioButton, 
       QPushButton, QLabel, QSpinBox)

app = QApplication([])
btn_Menu = QPushButton("Meny")
btn_Sleep = QPushButton("Bidpozutu")

box_Minutes = QSpinBox()
box_Minutes.setValue(30)

btn_OK = QPushButton("Bidpovistu")
lb_Question = QLabel("")

RadioGroupBox = QGroupBox("Bariantu Bidp")
RadioGroup = QButtonGroup()

rdtn_1 = QRadioButton("")
rdtn_2 = QRadioButton("")
rdtn_3 = QRadioButton("")
rdtn_4 = QRadioButton("")

RadioGroup.addButton(rdtn_1)
RadioGroup.addButton(rdtn_2)
RadioGroup.addButton(rdtn_3)
RadioGroup.addButton(rdtn_4)

AnsGroupBox = QGroupBox("Rezultat")

ld_Result = QLabel("")
ld_Correct = QLabel("")

Layout_ans1 = QHBoxLayout()
Layout_ans2 = QVBoxLayout()
Layout_ans3 = QVBoxLayout()
Layout_ans2.addWidget(rdtn_1)
Layout_ans2.addWidget(rdtn_2)
Layout_ans3.addWidget(rdtn_4)
Layout_ans3.addWidget(rdtn_3)

Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3)

RadioGroupBox.setLayout(Layout_ans1)

Leyout_res = QVBoxLayout()
Leyout_res.addWidget(ld_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
Leyout_res.addWidget(ld_Correct, alignment = Qt.AlignHCenter, stretch=2)
AnsGroupBox.hide()

Layout_line1 = QHBoxLayout()
Layout_line2 = QHBoxLayout()
Layout_line3 = QHBoxLayout()
Layout_line4 = QHBoxLayout()

Layout_line1.addWidget(btn_Menu)
Layout_line1.addStretch(1)
Layout_line1.addWidget(btn_Sleep)
Layout_line1.addWidget(box_Minutes)
Layout_line1.addWidget(QLabel("XBulun"))

Layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
Layout_line3.addWidget(RadioGroupBox)
Layout_line3.addWidget(AnsGroupBox)

Layout_line4.addStretch(1)
Layout_line4.addWidget(btn_OK, stretch=2)
Layout_line4.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(Layout_line1, stretch=1)
layout_card.addLayout(Layout_line2, stretch=2)
layout_card.addLayout(Layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(Layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)