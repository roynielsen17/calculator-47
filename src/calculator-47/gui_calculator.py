"""Professional Calculator"""

import os
import math
import ast
import operator


class Calculator:
    """Professional Calculator"""

    def __init__(self):
        self.history = []
        self.load_history()

        self.variables = {}

        self.operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.FloorDiv: operator.floordiv,
            ast.Pow: operator.pow,
            ast.Mod: operator.mod,
        }

        self.unary_operators = {
            ast.UAdd: operator.pos,
            ast.USub: operator.neg,
        }

    def add(self, a, b):
        """add"""
        return a + b

    def subtract(self, a, b):
        """subtract"""
        return a - b

    def multiply(self, a, b):
        """multiply"""
        return a * b

    def divide(self, a, b):
        """divide"""
        return a / b

    def power(self, a, b):
        """Power"""
        return a ** b

    def square_root(self, a):
        """Square Root"""
        return math.sqrt(a)

    def remainder(self, a, b):
        """Remainder"""
        return a % b

    def floor_division(self, a, b):
        """Floor Division"""
        return a // b

    def sine(self, a):
        """Sine"""
        return math.sin(math.radians(a))

    def cosine(self, a):
        """Cos"""
        return math.cos(math.radians(a))

    def tangent(self, a):
        """Tangent"""
        return math.tan(math.radians(a))

    def factorial(self, a):
        """Factorial"""
        return math.factorial(a)

    def logarithm(self, a, log_base):
        """Logarithm"""
        return math.log(a, log_base)

    def logarithm10(self, a):
        """Logarithm base 10"""
        return math.log10(a)

    def absolute_value(self, a):
        """Absolute Value"""
        return abs(a)

    def ceil(self, a):
        """Ceil"""
        return math.ceil(a)

    def floor(self, a):
        """Floor"""
        return math.floor(a)

    def natural_log(self, a):
        """Natural_Log"""
        return math.log(a)

    def save_variables(self, expression):
        """Save Variables"""
        name, value = expression.split("=")

        name = name.strip()
        value = value.strip()

        result = self.calculate_expression(value)
        self.variables[name] = result

        print(f"Variable {name} saved = {result}")

    # ===== Evaluate =====
    def evaluate(self, node):
        """Evaluate AST nodes"""

        if isinstance(node, ast.Constant):
            return node.value

        elif isinstance(node, ast.Name):
            if node.id not in self.variables:
                raise NameError
            return self.variables[node.id]

        elif isinstance(node, ast.BinOp):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)

            operation = self.operators[type(node.op)]
            return operation(left, right)

        elif isinstance(node, ast.UnaryOp):
            value = self.evaluate(node.operand)

            operation = self.unary_operators[type(node.op)]
            return operation(value)

        elif isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("Invalid function")
            function_name = node.func.id

            arguments = []

            for arg in node.args:
                arguments.append(self.evaluate(arg))

            functions = {
                "sqrt": self.square_root,
                "sin": self.sine,
                "cos": self.cosine,
                "tan": self.tangent,
                "log": self.logarithm,
                "log10": self.logarithm10,
                "ln": self.natural_log,
                "factorial": self.factorial,
                "abs": self.absolute_value,
                "ceil": self.ceil,
                "floor": self.floor,
            }

            if function_name not in functions:
                raise NameError("Unknown function")
            return functions[function_name](*arguments)

        else:
            raise ValueError("Invalid expression")

    def calculate_expression(self, expression):
        """Calculate full expression"""
        expression = expression.replace("^", "**")
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")

        tree = ast.parse(expression, mode="eval")
        result = self.evaluate(tree.body)
        return result

    def save_history(self, text):
        """Save history to txt"""

        os.makedirs("data", exist_ok=True)
        with open("data/history.txt", "a", encoding="utf-8") as file:
            file.write(text + "\n")

    def load_history(self):
        """Load History"""
        try:
            with open("data/history.txt", "r", encoding="utf-8") as file:
                for line in file:
                    self.history.append(line.strip())
        except FileNotFoundError:
            pass

    def clear_history(self):
        """Clear History"""
        self.history.clear()
        with open("data/history.txt", "w", encoding="utf-8") as file:
            file.write("")

    def show_history(self):
        """Show History"""

        if not self.history:
            print("\nHistory is empty!")
        else:
            print("\n===== History =====")

            for item in self.history:
                print(item)

    def show_menu(self):
        """Display Calculator Menu"""
        print(
            """
            ======== Calculator ========

            Enter mathematical expression

            Examples:
            5 + 3 * 2
            sqrt(25)
            sin(90)
            log10(100)
            2^5

            Commands:
            history  -> Show history
            clear    -> Clear history
            0        -> Exit

            ============================
            """
        )

    def confirm_clear_history(self):
        """Clear_history_menu"""
        answer = input("Are you sure? (y/n): ").lower()
        if answer == "y":
            self.clear_history()
            print("History cleared successfully.")

    def run(self):
        """run"""
        while True:
            self.show_menu()

            expression = input(">>> ")

            if expression == "0":
                break
            elif expression == "history":
                self.show_history()
                continue
            elif expression == "clear":
                self.confirm_clear_history()
                print("History cleared successfully.")
                continue

            try:
                if "=" in expression:
                    self.save_variables(expression)
                    continue
                result = self.calculate_expression(expression)
                print(f"Answer: {result}")

                history_text = f"{expression} = {result}"
                self.history.append(history_text)
                self.save_history(history_text)

            except ZeroDivisionError:
                print("Cannot divide by zero!")

            except SyntaxError:
                print("Invalid syntax!")

            except NameError:
                print("Unknown variable!")

            except ValueError:
                print("Invalid value!")


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
