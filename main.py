import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QListWidget, QHBoxLayout, QInputDialog
from PyQt5.QtGui import QIcon  # Import QIcon to set the application icon

class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the application icon (this will also set the icon in the taskbar)
        self.setWindowIcon(QIcon('./icon.ico'))  # Path to your icon file

        # Window settings
        self.setWindowTitle("Baala ka PA")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # Always-on-top
        self.setAttribute(Qt.WA_TranslucentBackground)  # Transparent background
        self.setWindowOpacity(0.9)  # Adjust transparency

        # Layout and widgets
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.task_list_widget = QListWidget()  # To display tasks
        self.task_list_widget.setStyleSheet("QListWidget { background: transparent; }")
        self.task_list_widget.setStyleSheet("""
            QListWidget {
                background: transparent;
                color: white;  /* Font color to white */
                font-size: 14px;
            }
            QListWidget::item:selected {
                background: rgba(255, 255, 255, 30);  /* Light transparent selection */
                color: white;  /* Selected text color */
            }
        """)  # Make the task list background transparent
        layout.addWidget(self.task_list_widget)

        # Button to add a task
        add_task_btn = QPushButton("Add Task")
        add_task_btn.clicked.connect(self.add_task)

        # Button to edit a task
        edit_task_btn = QPushButton("Edit Task")
        edit_task_btn.clicked.connect(self.edit_task)

        # Button to remove a task
        remove_task_btn = QPushButton("Remove Task")
        remove_task_btn.clicked.connect(self.remove_task)

        # Adding buttons to the layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(add_task_btn)
        button_layout.addWidget(edit_task_btn)
        button_layout.addWidget(remove_task_btn)
        layout.addLayout(button_layout)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_task(self):
        # Get task from user input
        task, ok = QInputDialog.getText(self, "Add Task", "Enter your task:")
        if ok and task.strip() != "":
            self.task_list_widget.addItem(task)

    def edit_task(self):
        selected_task = self.task_list_widget.currentItem()
        if selected_task:
            # Get the updated task from the user
            new_task, ok = QInputDialog.getText(self, "Edit Task", "Edit your task:", text=selected_task.text())
            if ok and new_task.strip() != "":
                selected_task.setText(new_task)

    def remove_task(self):
        selected_task = self.task_list_widget.currentItem()
        if selected_task:
            row = self.task_list_widget.row(selected_task)
            self.task_list_widget.takeItem(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = TodoApp()
    todo_app.show()
    sys.exit(app.exec_())
