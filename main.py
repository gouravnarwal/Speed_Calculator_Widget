#student project 
import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()
        self.setLayout(grid)

        #create widgets
        name_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()

        dob_label = QLabel("Time(hours): ")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)
        self.output_label = QLabel()

        selection_label = QLabel("Select Option: ")
        self.selection_list = QComboBox()
        self.selection_list.addItems(["Metric(km)","Imperial(miles)"])


        #add widgets to grid
        grid.addWidget(name_label,0, 0)
        grid.addWidget(self.distance_line_edit,0,1)
        grid.addWidget(selection_label,0,2)
        grid.addWidget(self.selection_list,0,3)
        grid.addWidget(dob_label,1,0)
        grid.addWidget(self.time_line_edit,1,1)
        grid.addWidget(calculate_button,2,0,1,4)
        grid.addWidget(self.output_label,3,0,1,4)

    def calculate(self):
        distance = self.distance_line_edit.text()
        distance = float(distance)
        time = self.time_line_edit.text()
        time = float(time)
        speed = distance / time
        speed = float(speed)
        selected_option = self.selection_list.currentText()

        if selected_option == "Metric(km)":
            return self.output_label.setText(f"Average speed is {speed} km/h")

        if selected_option == "Imperial(miles)":
            return self.output_label.setText(f"Average speed is {speed} miles/h")

app=QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())