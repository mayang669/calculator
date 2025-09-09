from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import math

class CalculatorApp(App):
    def build(self):
        self.icon = "calc.png"
        self.operators = ['+', '-', '*', '/', '%']
        self.last_was_operator = False
        self.last_button = None
        self.equal_count = 0  

       
        Window.clearcolor = (0.1, 0.1, 0.1, 1)

        main_layout = BoxLayout(orientation="vertical", padding=12, spacing=12)

        # Display
        self.solution = TextInput(
            readonly=True,
            multiline=False,
            halign="right",
            font_size=48,
            background_color=(0.05, 0.05, 0.05, 1),
            foreground_color=(1, 0.6, 0.2, 1),  # light orange text
            cursor_color=(1, 0.6, 0.2, 1),
            size_hint=(1, 0.25),
        )
        main_layout.add_widget(self.solution)

        # Button grid
        buttons = [
            ['C', 'DEL', '√', '%'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'x²', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=12, size_hint=(1, 0.15))
            for label in row:
              
                if label in ['C', 'DEL']:
                    bg_color = (1, 0.3, 0.1, 1) 
                elif label in self.operators or label in ['√', 'x²']:
                    bg_color = (1, 0.5, 0.2, 1) 
                else:
                    bg_color = (0.2, 0.2, 0.2, 1) 

                button = Button(
                    text=label,
                    font_size=28,
                    background_normal='',
                    background_color=bg_color,
                    color=(1, 1, 1, 1),
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

     
        equals_button = Button(
            text="=",
            font_size=34,
            background_normal='',
            background_color=(1, 0.6, 0.2, 1), 
            color=(0, 0, 0, 1),
            size_hint=(1, 0.2),
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

       
        self.equal_count = 0

        if button_text == 'C':
            self.solution.text = ''
        elif button_text == 'DEL':
            self.solution.text = current[:-1]
        elif button_text == 'x²':
            if current:
                try:
                    self.solution.text = str(eval(current) ** 2)
                except:
                    self.solution.text = "Error"
        elif button_text == '√':
            if current:
                try:
                    self.solution.text = str(math.sqrt(eval(current)))
                except:
                    self.solution.text = "Error"
        elif button_text in self.operators:
            if current and self.last_was_operator:
                return
            elif current == '' and button_text in self.operators:
                return
            else:
                self.solution.text = current + button_text
        else:
            self.solution.text = current + button_text

        self.last_button = button_text
        self.last_was_operator = button_text in self.operators

    def on_solution(self, instance):
        self.equal_count += 1  

        if self.equal_count == 3: 
            self.solution.text = "The developer name is Atraya "
            self.equal_count = 0
            return

        text = self.solution.text
        if text:
            try:
                solution = str(eval(text))
                self.solution.text = solution
            except ZeroDivisionError:
                self.solution.text = "Can't divide by zero!"
            except Exception:
                self.solution.text = "Error"

        self.last_was_operator = False
        self.last_button = None


if __name__ == '__main__':
    CalculatorApp().run()

