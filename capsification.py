from random import randrange
from pyforms            import start_app
from pyforms.controls   import ControlButton
from pyforms.controls   import ControlText
from pyforms.basewidget import BaseWidget


class Capsify(BaseWidget):

    def __init__(self, *args, **kwargs):
        super().__init__('Capsification Automator')

        self._input_string = ControlText('Sentence to Capsify')
        self._output_string = ControlText('Capsified Sentence')
        self._run_button = ControlButton('Perform Capsification')
        self._run_button.value = self.__runButtonAction

        self._formset = [
            '_input_string',
            '_run_button',
            '_output_string',
        ]

    def __runButtonAction(self):

        input_string = self._input_string.value
        output_list = []

        for i in input_string:
            if randrange(1,10,1) >= 5:
                output_list.append(i)
            else:
                output_list.append(i.swapcase())

        self._output_string.value = "".join(output_list)

if __name__ == '__main__':
    start_app(Capsify)
