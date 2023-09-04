import PySide6.QtGui
import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
import PySide6.QtGui as qtg



class TrafficLight(qtw.QWidget):

    RATIO = 1.61
    RECT_OFFSET = 20

    RED = 0x1
    YELLOW = 0x2
    GREEN = 0x4

    def __init__(self):
        super().__init__()
        self.setMinimumSize(100, 100)

        # 0x0 = None
        # 0x1 = RED
        # 0x2 = YELLOW
        # 0x4 = GREEN 
        self.state = 0

    def set_state(self, state):
        if state not in range(0, 8):
            raise ValueError 

        else:
            self.state = state

        self.update()

    def paintEvent(self, event) -> None:
        painter = qtg.QPainter(self)
        widget_width = painter.device().width()
        widget_height = painter.device().height()
        
        # The width is restricting
        if widget_height > widget_width*self.RATIO:
            widget_height = widget_width*self.RATIO
        # The height is restricting
        else:
            widget_width = widget_height/self.RATIO


        brush = qtg.QBrush()

        # Draw Background
        brush.setColor(qtg.QColor('white'))
        brush.setStyle(qtc.Qt.BrushStyle.SolidPattern)
        rect = qtc.QRect(0, 0, widget_width, widget_width)
        painter.fillRect(rect, brush)


        # Draw traffic light
        brush.setColor(qtg.QColor("gray"))
        brush.setStyle(qtc.Qt.BrushStyle.SolidPattern)        
        rect = qtc.QRect(
            self.RECT_OFFSET,
            self.RECT_OFFSET,
            widget_width-self.RECT_OFFSET*2,
            widget_height-self.RECT_OFFSET*2
        )
        painter.fillRect(rect, brush)

        top_point = qtc.QPoint(self.RECT_OFFSET+((widget_width-self.RECT_OFFSET*2)/2), self.RECT_OFFSET+((widget_height-self.RECT_OFFSET*2)/4))
        middle_point = qtc.QPoint(self.RECT_OFFSET+((widget_width-self.RECT_OFFSET*2)/2), self.RECT_OFFSET+((widget_height-self.RECT_OFFSET*2)/2))
        bottom_point = qtc.QPoint(self.RECT_OFFSET+((widget_width-self.RECT_OFFSET*2)/2), self.RECT_OFFSET+(3*(widget_height-self.RECT_OFFSET*2)/4))
        
        circle_radius = ((widget_height-self.RECT_OFFSET*2)/10)

        #painter.drawEllipse(top_point, circle_radius, circle_radius)
        #painter.drawEllipse(middle_point, circle_radius, circle_radius)
        #painter.drawEllipse(bottom_point, circle_radius, circle_radius)
 
        # top red offline light
        off_state_path = qtg.QPainterPath()
        off_state_path.addEllipse(top_point, circle_radius, circle_radius)
        brush.setColor(qtg.QColor(32, 0, 0))
        painter.fillPath(off_state_path, brush)

        # middle yellow offline light
        off_state_path = qtg.QPainterPath()
        off_state_path.addEllipse(middle_point, circle_radius, circle_radius)
        brush.setColor(qtg.QColor(32, 32, 0))
        painter.fillPath(off_state_path, brush)

        # bottom green offline light
        off_state_path = qtg.QPainterPath()
        off_state_path.addEllipse(bottom_point, circle_radius, circle_radius)
        brush.setColor(qtg.QColor(0, 32, 0))
        painter.fillPath(off_state_path, brush)

        
        if (self.state & self.RED) != 0:
            path = qtg.QPainterPath()
            path.addEllipse(top_point, circle_radius, circle_radius)
            brush.setColor(qtg.QColor(255,0,0))
            painter.fillPath(path, brush)
        
        if (self.state & self.YELLOW) != 0:
            path = qtg.QPainterPath()
            path.addEllipse(middle_point, circle_radius, circle_radius)
            brush.setColor(qtg.QColor(255,255,0))
            painter.fillPath(path, brush)

        if (self.state & self.GREEN) != 0:
            path = qtg.QPainterPath()
            path.addEllipse(bottom_point, circle_radius, circle_radius)
            brush.setColor(qtg.QColor(0,255,0))
            painter.fillPath(path, brush)
