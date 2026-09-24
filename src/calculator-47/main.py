"""Calculator"""
import traceback

from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup
from PySide6.QtCore import QRect, QPropertyAnimation, Qt
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, QEvent
# from PySide6.QtCore import QSizeGrip
from ui_calculator import Ui_MainWindow
from gui_calculator import Calculator

from sexagesimal import to_sexagesimal

# pyside6-uic calculator.ui -o ui_calculator.py
# pyside6-designer


class CalculatorWindow(QMainWindow):
    """Calculator"""

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Show calculator
        calc_w = self.ui.frame.width()
        calc_h = self.ui.frame.height()

        self.ui.frame.move(0, 0)
        self.ui.frame_2.setGeometry(0, 0, calc_w, calc_h)
        self.setFixedSize(calc_w, calc_h)

        self.ui.radioButton_decimal.setChecked(True)

        self.rbgroup = QButtonGroup(self)
        self.rbgroup.addButton(self.ui.radioButton_decimal)
        self.rbgroup.addButton(self.ui.radioButton_octal)
        self.rbgroup.addButton(self.ui.radioButton_hexidecimal)
        self.rbgroup.addButton(self.ui.radioButton_binary)
        self.rbgroup.addButton(self.ui.radioButton_base60)

        menu_w = self.ui.menu_frame.width()
        hist_w = self.ui.history_frame.width()
        hist_y = self.ui.history_frame.y()
        hist_h = self.ui.history_frame.height()

        self.menu_closed_rect = QRect(-menu_w, 0, menu_w, calc_h)
        self.menu_open_rect = QRect(0, 0, menu_w, calc_h)

        self.history_closed_rect = QRect(calc_w, hist_y, hist_w, hist_h)
        self.history_open_rect = QRect(calc_w - hist_w, hist_y, hist_w, hist_h)

        self.ui.menu_frame.setGeometry(self.menu_closed_rect)
        self.ui.history_frame.setGeometry(self.history_closed_rect)

        #
        memory_w = self.ui.memory_frame.width()
        memory_h = self.ui.memory_frame.height()

        self.memory_closed_rect = QRect(0, calc_h, memory_w, memory_h)
        self.memory_open_rect = QRect(0, calc_h - memory_h, memory_w, memory_h)

        self.ui.memory_frame.setGeometry(self.memory_closed_rect)

        # Tooitip
        self.ui.btn_clear_history.setToolTip("Clear all history")
        self.ui.btn_history.setToolTip("History")
        self.ui.btn_menu1.setToolTip("Navigation")
        self.ui.btn_menu2.setToolTip("Navigation")

        # Close history when clicking outside
        self.ui.history_frame.installEventFilter(self)
        self.installEventFilter(self)

        self.history_open = False

        # Icons
        self.ui.btn_clear_history.setIcon(QIcon("icons/trash.png"))

        self.ui.btn_clear_history.setIconSize(QSize(20, 20))

        # Discoloration of the display
        self.ui.display.setStyleSheet("""
            QLineEdit {
            background: transparent;
            border: none;
            font-weight: bold;
            }
        """)

        # Setting from the Right
        self.ui.display.setAlignment(Qt.AlignRight)

        # Cannot type on the display
        self.ui.display.setReadOnly(True)

        # Font
        self.ui.display.textChanged.connect(self.update_display_font)

        self.setup_button_styles()

        self.frame_color_style()

        self.setup_memory_buttons_style()

        self.setup_icon_buttons_style()

        # = = = =

        self.memory_list_data = []

        self.memory_open = False
        self.memory_animation = QPropertyAnimation(
            self.ui.memory_frame, b"geometry"
        )

        self.memory_animation.setDuration(250)

        # = = = =

        self.calculator = Calculator()
        self.result_shown = False

        self.memory = 0.0

        self.history_animation = QPropertyAnimation(
            self.ui.history_frame, b"geometry"
        )

        self.history_animation.setDuration(250)

        # = = = =

        self.menu_open = False

        self.menu_animation = QPropertyAnimation(
            self.ui.menu_frame, b"geometry"
        )

        self.menu_animation.setDuration(250)

        # = = = =
        self.button_animations = []

        self.connect_buttons()

    # =================================================================
    def setup_button_styles(self):
        """Setup button style"""
        number_color = "#333232"
        operator_color = "#424040"
        equal_color = "#0078d4"

        number_buttons = [
            self.ui.btn_sign,
            self.ui.btn_dot,
            self.ui.btn_0,
            self.ui.btn_1,
            self.ui.btn_2,
            self.ui.btn_3,
            self.ui.btn_4,
            self.ui.btn_5,
            self.ui.btn_6,
            self.ui.btn_7,
            self.ui.btn_8,
            self.ui.btn_9,
        ]

        operator_buttons = [
            self.ui.btn_add,
            self.ui.btn_sub,
            self.ui.btn_mul,
            self.ui.btn_div,
            self.ui.btn_backspace,
            self.ui.btn_clear,
            self.ui.btn_sqrt,
            self.ui.btn_square,
            self.ui.btn_reciprocal,
            self.ui.btn_ce,
            self.ui.btn_percent,
        ]

        for button in number_buttons:
            self.set_button_style(button, number_color, "#424040")

        for button in operator_buttons:
            self.set_button_style(button, operator_color, "#333232")

        self.set_button_style(self.ui.btn_equal, equal_color, "#005a9e")

    def set_button_style(self, button, normal_color, pressed_color):
        """Button color"""

        button.setStyleSheet(
            f"""QPushButton {{
                background-color: {normal_color};
                color: white;
                border-radius: 7px;
                }}
            QPushButton:hover{{
                background-color: {pressed_color};
                }}
            QPushButton:pressed{{
                background-color: {pressed_color};
                }}""")

    # =================================================================

    def frame_color_style(self):
        """Frame color"""

        self.set_frame_style(self.ui.frame, "#11024CFF")  # 11024CFF

    def set_frame_style(self, frame, color):
        """Set frame color"""
        frames = [
            self.ui.frame,
        ]

        for frame in frames:
            frame.setStyleSheet(f"""
                QFrame {{
                    background-color: {color};
                    border-radius: 5px;
                }}
            """)

    # =============================style===============================
    def setup_memory_buttons_style(self):
        """Memory buttons style"""

        memory_buttons = [
            self.ui.btn_mc,
            self.ui.btn_mr,
            self.ui.btn_mplus,
            self.ui.btn_mminus,
            self.ui.btn_ms,
            self.ui.btn_mdown,
        ]

        for mbutton in memory_buttons:
            mbutton.setStyleSheet("""
                QPushButton {
                background-color: transparent;
                border: none;
                color: white;
                font-size: 14px;
                }
                QPushButton:hover {
                background-color: #1F1D23FF;
                border-radius: 8px;
                }
                QPushButton:pressed {
                background-color: #1F1D23FF;
                }
            """)

        important_buttons = [
            self.ui.btn_history,
            self.ui.btn_menu1,
            self.ui.btn_menu2,
            self.ui.label,
        ]

        for ibutton in important_buttons:
            ibutton.setStyleSheet("""
                QPushButton {
                background-color: transparent;
                border: none;
                color: white;
                font-size: 20px;
                }
                QPushButton:hover {
                background-color: #1F1D23FF;
                border-radius: 8px;
                }
                QPushButton:pressed {
                background-color: #1F1D23FF;
                }
            """)

        list_screen = [
            self.ui.history_list,
        ]

        for screen in list_screen:
            screen.setStyleSheet("""
                QListWidget {
                background-color: transparent;
                border: none;
                color: white;
                font-size: 15px;
                }
                QListWidget:hover {
                background-color: transparent;
                border-radius: 8px;
                }
                QListWidget::item {
                background-color: transparent;
                border-radius: 6px;
                }
                QListWidget::item:hover {
                background-color: #15284d;
                border-radius: 6px;
                }
            """)

            self.ui.history_frame.setStyleSheet("""
                QFrame {
                background-color: rgba(18, 18, 24, 210);
                border-radius: 5px;
                }
            """)

            self.ui.menu_frame.setStyleSheet("""
                QFrame {
                background-color: rgba(18, 18, 24, 210);
                border-radius: 5px;
                 }
            """)

            self.ui.label.setStyleSheet("""
                QLabel {
                background-color: transparent;
                }
            """)

    # =============================icon================================
    def setup_icon_buttons_style(self):
        """Icon buttons style"""
        self.ui.btn_clear_history.setStyleSheet("""
            QPushButton {
            border:none;
            background-color: transparent;
            }
            QPushButton:hover {
            background-color: #1F1D23FF;
            border-radius: 8px;
            }
       """)

    # =================================================================
    def add_to_display(self, value):
        """Add to display"""

        if self.result_shown:
            if value.isdigit() or value == ".":
                self.ui.display.clear()
        self.result_shown = False

        self.ui.display.insert(value)

    # =================================================================
    def update_display_font(self):
        """Font"""
        length = len(self.ui.display.text())
        font = self.ui.display.font()
        font_size = 42

        if length <= 5:
            font_size = 42
        elif length <= 10:
            font_size = 30
        else:
            font_size = 20

        font.setPointSize(font_size)
        self.ui.display.setFont(font)

    # =================================================================
    def show_history(self):
        """Show history"""
        # Show all previous calculations.

        self.ui.history_list.clear()

        for item in self.calculator.history:
            self.ui.history_list.addItem(item)

        self.ui.history_frame.raise_()

        if not self.history_open:
            self.history_animation.setStartValue(self.history_closed_rect)
            self.history_animation.setEndValue(self.history_open_rect)
        else:
            self.history_animation.setStartValue(self.history_open_rect)
            self.history_animation.setEndValue(self.history_closed_rect)

        self.history_animation.start()

        self.history_open = not self.history_open

    # =================================================================
    def show_menu(self):
        """Show menu"""

        self.ui.menu_frame.raise_()

        if not self.menu_open:
            self.menu_animation.setStartValue(self.menu_closed_rect)
            self.menu_animation.setEndValue(self.menu_open_rect)
        else:
            self.menu_animation.setEndValue(self.menu_closed_rect)
            self.menu_animation.setStartValue(self.menu_open_rect)

        self.menu_animation.start()

        self.menu_open = not self.menu_open

    # =================================================================
    def eventFilter(self, obj, event):
        """Close history when clicking outside"""

        if event.type() == QEvent.MouseButtonPress:

            if self.history_open:
                pos = self.mapFromGlobal(event.globalPosition().toPoint())

                history_rect = self.ui.history_frame.geometry()

                if not history_rect.contains(pos):
                    self.show_history()

        return super().eventFilter(obj, event)

    # =================================================================
    def show_memory(self):
        """Show memory panel"""

        self.ui.memory_list.clear()

        for value in self.memory_list_data:
            self.ui.memory_list.addItem(str(value))

        self.ui.memory_frame.raise_()

        if not self.memory_open:
            self.memory_animation.setStartValue(self.memory_closed_rect)
            self.memory_animation.setEndValue(self.memory_open_rect)
        else:
            self.memory_animation.setStartValue(self.memory_open_rect)
            self.memory_animation.setEndValue(self.memory_closed_rect)

        self.memory_animation.start()

        self.memory_open = not self.memory_open

    # =================================================================
    def memory_clear(self):
        """Clear all memory"""

        self.memory_list_data.clear()
        self.ui.memory_list.clear()

    # =================================================================
    def memory_store(self):
        """Store current value as a nem memory entry"""

        try:
            value = self.calculator.calculate_expression(
                self.ui.display.text()
            )
            self.memory_list_data.append(value)
            self.result_shown = True

        except (ZeroDivisionError, SyntaxError, NameError, ValueError):
            self.show_error()

    # =================================================================
    def memory_recall(self):
        """Recall the most recent memory value"""

        if self.memory_list_data:
            self.ui.display.setText(str(self.memory_list_data[-1]))
            self.result_shown = True

    # =================================================================
    def memory_add(self):
        """Add current value to the list memory entry"""

        try:
            value = self.calculator.calculate_expression(
                self.ui.display.text()
            )
            if self.memory_list_data:
                self.memory_list_data[-1] += value
            else:
                self.memory_list_data.append(value)
            self.result_shown = True

        except (ZeroDivisionError, SyntaxError, NameError, ValueError):
            self.show_error()

    # =================================================================
    def memory_subtract(self):
        """Subtract current value from the list memory entry"""

        try:
            value = self.calculator.calculate_expression(
                self.ui.display.text()
            )
            if self.memory_list_data:
                self.memory_list_data[-1] -= value
            else:
                self.memory_list_data.append(-value)
            self.result_shown = True

        except (ZeroDivisionError, SyntaxError, NameError, ValueError):
            self.show_error()

    # =================================================================
    def recall_from_memory_list(self, item):
        """Recall a value clicked inside the memory panel"""

        self.ui.display.setText(item.text())
        self.result_shown = True

    # =================================================================
    def clear_history(self):
        """Clear history"""

        self.calculator.clear_history()
        self.ui.history_list.clear()

    # =================================================================
    def clear_display(self):
        """Clear display"""
        self.ui.display.clear()

    # =================================================================
    def clear_entry(self):
        """Clear current entry"""

        text = self.ui.display.text()

        if not text:
            return

        operators = ["+", "-", "×", "÷"]

        for operator in operators:
            if operator in text:
                parts = text.rsplit(operator, 1)

                self .ui.display.setText(parts[0] + operator)
                return

        self.ui.display.clear()

    # =================================================================
    def persent(self):
        """Persent"""

        try:
            value = self.calculator.calculate_expression(
                self.ui.display.text()
            )
            self.ui.display.setText(str(value / 100))

        except (ZeroDivisionError, SyntaxError, NameError, ValueError):
            self.show_error()

    # =================================================================
    def backspace(self):
        """Delete character before cursor"""

        self.ui.display.backspace()

    # =================================================================
    def square(self):
        """square"""

        try:
            value = self.calculator.calculate_expression(
                self.ui.display.text()
            )
            self.ui.display.setText(str(value ** 2))

        except (ZeroDivisionError, SyntaxError, NameError, ValueError):
            self.show_error()

    # =================================================================
    def square_root(self):
        """square root"""

        try:
            value = self.calculator.calculate_expression(
                self.ui.display.text()
            )
            self.ui.display.setText(str(self.calculator.square_root(value)))

        except (ZeroDivisionError, SyntaxError, NameError, ValueError):
            self.show_error()

    # =================================================================
    def reciprocal(self):
        """Reciprecal"""

        try:
            value = self.calculator.calculate_expression(
                self.ui.display.text()
            )
            self.ui.display.setText(str(1 / value))

        except (ZeroDivisionError, SyntaxError, NameError, ValueError):
            self.show_error()

    # =================================================================
    def change_sign(self):
        """Change sign"""

        try:
            value = self.calculator.calculate_expression(
                self.ui.display.text()
            )
            self.ui.display.setText(str(-value))

        except (ZeroDivisionError, SyntaxError, NameError, ValueError):
            self.show_error()

    # =================================================================
    def calculate(self):
        """Calculate expression"""

        expression = self.ui.display.text()

        try:
            result = self.calculator.calculate_expression(expression)

            if self.ui.radioButton_octal.isChecked():
                result = oct(int(result))
            elif self.ui.radioButton_hexidecimal.isChecked():
                result = hex(int(result))
            elif self.ui.radioButton_base60.isChecked():
                result = to_sexagesimal(int(result))

            history_text = f"{expression} = {result}"
            self.calculator.history.append(history_text)
            self.calculator.save_history(history_text)

            self.ui.display.setText(str(result))
            self.result_shown = True

        except (ZeroDivisionError, SyntaxError, NameError, ValueError):
            self.show_error()
            print(traceback.format_exc())
        except Exception as e:
            self.show_error()
            # print(traceback.format_exc())

    # =================================================================
    def connect_buttons(self):
        """Connect buttons"""

        numbers = [
            ("btn_0", "0"),
            ("btn_1", "1"),
            ("btn_2", "2"),
            ("btn_3", "3"),
            ("btn_4", "4"),
            ("btn_5", "5"),
            ("btn_6", "6"),
            ("btn_7", "7"),
            ("btn_8", "8"),
            ("btn_9", "9"),
        ]

        for button_name, value in numbers:
            button = getattr(self.ui, button_name)
            button.clicked.connect(lambda _, v=value: self.add_to_display(v))

        operators = [
            ("btn_add", "+"),
            ("btn_sub", "-"),
            ("btn_mul", "×"),
            ("btn_div", "÷"),
            ("btn_dot", "."),
        ]
        for button_name, value in operators:
            button = getattr(self.ui, button_name)
            button.clicked.connect(lambda _, v=value: self.add_to_display(v))

        # Actions
        self.ui.btn_clear.clicked.connect(self.clear_display)
        self.ui.btn_backspace.clicked.connect(self.backspace)
        self.ui.btn_equal.clicked.connect(self.calculate)
        self.ui.btn_square.clicked.connect(self.square)
        self.ui.btn_sqrt.clicked.connect(self.square_root)
        self.ui.btn_reciprocal.clicked.connect(self.reciprocal)
        self.ui.btn_sign.clicked.connect(self.change_sign)
        self.ui.btn_percent.clicked.connect(self.persent)
        self.ui.btn_ce.clicked.connect(self.clear_entry)

        # Memory
        self.ui.btn_mc.clicked.connect(self.memory_clear)
        self.ui.btn_mr.clicked.connect(self.memory_recall)
        self.ui.btn_mplus.clicked.connect(self.memory_add)
        self.ui.btn_mminus.clicked.connect(self.memory_subtract)
        self.ui.btn_ms.clicked.connect(self.memory_store)
        self.ui.btn_mdown.clicked.connect(self.show_memory)

        self.ui.memory_list.itemClicked.connect(self.recall_from_memory_list)
        self.ui.btn_clear_memory.clicked.connect(self.memory_clear)

        # Show history
        self.ui.btn_history.clicked.connect(self.show_history)

        # Show menu
        self.ui.btn_menu1.clicked.connect(self.show_menu)
        self.ui.btn_menu2.clicked.connect(self.show_menu)

        # Clear history
        self.ui.btn_clear_history.clicked.connect(self.clear_history)

    # =================================================================
    def show_error(self):
        """Show Error"""

        self.ui.display.setText("Error")


if __name__ == "__main__":
    app = QApplication([])

    window = CalculatorWindow()
    window.show()

    app.exec()
