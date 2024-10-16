from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout

from qfluentwidgets import ElevatedCardWidget
from qfluentwidgets import ComboBox
from qfluentwidgets import CaptionLabel
from qfluentwidgets import StrongBodyLabel

class ComboBoxCard(ElevatedCardWidget):

    def __init__(self, title: str, description: str, items: list[str], init = None, currentIndexChanged = None):
        super().__init__(None)
        
        # 设置容器
        self.setBorderRadius(4)
        self.container = QHBoxLayout(self)
        self.container.setContentsMargins(16, 16, 16, 16) # 左、上、右、下

        # 文本控件
        self.vbox = QVBoxLayout()
        
        self.title_label = StrongBodyLabel(title, self)
        self.description_label = CaptionLabel(description, self)
        self.description_label.setTextColor(QColor(96, 96, 96), QColor(160, 160, 160))

        self.vbox.addWidget(self.title_label)
        self.vbox.addWidget(self.description_label)
        self.container.addLayout(self.vbox)

        # 填充
        self.container.addStretch(1)
        
        # 下拉框控件
        self.combo_box = ComboBox(self)
        self.combo_box.addItems(items)

        if init:
            init(self)

        if currentIndexChanged:
            self.combo_box.currentIndexChanged.connect(lambda index: currentIndexChanged(self, index))

        self.container.addWidget(self.combo_box)

    def set_items(self, items: list) -> None:
        self.combo_box.clear()
        self.combo_box.addItems(items)

    def find_text(self, text: str) -> int:
        return self.combo_box.findText(text)

    def get_current_text(self) -> str:
        return self.combo_box.currentText()

    def set_current_index(self, index) -> None:
        self.combo_box.setCurrentIndex(index)