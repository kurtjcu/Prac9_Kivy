__author__ = 'sam'
from kivy.app import App
from kivy.lang import Builder
import random


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        '''
        if random.randint(1, 10) <= 5:
            self.root.ids.my_label.text = "ouch!!"
        else:
            self.root.ids.my_label.text = "stop that!!"
        '''
        print('test')
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        self.root.ids.output_label.text = " "
        self.root.ids.input_name.text = " "

BoxLayoutDemo().run()

