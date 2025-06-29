import sys
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from qt_jsonschema_form import WidgetBuilder

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Zod Schema Form")

        # Load the JSON schema
        try:
            with open("schema.json", "r") as f:
                full_schema = json.load(f)
            schema = full_schema['definitions']['UserSchema']
        except FileNotFoundError:
            print("Error: schema.json not found. Please run convert.bat first.")
            sys.exit(1)

        # Create the form widget
        builder = WidgetBuilder()
        form = builder.create_form(schema, {})

        # Set up the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(form)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())