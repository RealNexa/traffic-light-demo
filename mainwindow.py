import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
import PySide6.QtGui as qtg

from traffic_lights_demo import TrafficLight

class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Traffic Light Demo")
        self.traffic_light = TrafficLight()

        self.setCentralWidget(self.traffic_light)


        g = qtw.QPushButton("Green")
        g.clicked.connect(lambda: self.traffic_light.set_state(TrafficLight.GREEN))

        y = qtw.QPushButton("Yellow")
        y.clicked.connect(lambda: self.traffic_light.set_state(TrafficLight.YELLOW))

        r = qtw.QPushButton("Red")
        r.clicked.connect(lambda: self.traffic_light.set_state(TrafficLight.RED))

        custom_input = qtw.QLineEdit()
        custom_input_button = qtw.QPushButton("Set")
        custom_input_button.clicked.connect(lambda: self.traffic_light.set_state(int(custom_input.text().strip())))

        self.statusBar().addWidget(g)
        self.statusBar().addWidget(y)
        self.statusBar().addWidget(r)
        self.statusBar().addWidget(custom_input)
        self.statusBar().addWidget(custom_input_button)
