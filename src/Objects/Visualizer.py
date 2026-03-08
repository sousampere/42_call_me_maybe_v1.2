
import time
from typing import Any, List

from src import PromptProcessor


class Visualizer():
    screen_x = 10
    screen_y = 7

    @staticmethod
    def visualize() -> None:
        """ Prints a nice visualization """
        print('\033[2J\033[1;1H')
        print("""
\033[1;30m
\033[1;30m
\033[1;30m      ooooooooooooooooooooooooooooooooooooo   """
              """                  \033[1;33m      ____      _ _
\033[1;30m      8                                .d88   """
              """                  \033[1;33m     / ___|"""
              """__ _| | |  _ __ ___   ___
\033[1;30m      8  oooooooooooooooooooooooooooood8888   """
              """                  \033[1;33m    | |   /"""
              """ _` | | | | '_ ` _ \\ / _ \\
\033[1;30m      8  8888888888888888888888888P"   8888   """
              """ oooooooooooooooo \033[1;33m    | |__| """
              """(_| | | | | | | | | |  __/
\033[1;30m      8  8888888888888888888888P"      8888   """
              """ 8              8 \033[1;33m     \\____"""
              """\\__,_|_|_| |_| |_| |_|"""
              """\\___|\033[0;36m           ___
\033[1;30m      8  8888888888888888888P"         8888   """
              """ 8             d8 \033[0;36m           """
              """  _ __ ___   _"""
              """_ _ _   _| |__   ___  |__ \\
\033[1;30m      8  8888888888888888P"            8888   """
              """ 8            d88 \033[0;36m           """
              """ | '_ ` _ \\ /"""
              """ _` | | | | '_ \\ / _ \\   / /
\033[1;30m      8  8888888888888P"               8888   """
              """ 8           d888 \033[0;36m     _ _ _ """
              """ | | | | | | ("""
              """_| | |_| | |_) |  __/  |_|
\033[1;30m      8  8888888888P"                  8888   """
              """ 8          d8888 \033[0;36m    (_|_|_)"""
              """ |_| |_| |_|\\"""
              """__,_|\\__, |_.__/ \\___|  (_)
\033[1;30m      8  8888888P"                     8888   """
              """ 8         d88888 \033[0;36m           """
              """                  |___/    (please don't)
\033[1;30m      8  8888P"                        8888   """
              """ 8        d888888
\033[1;30m      8  8888oooooooooooooooooooooocgmm8888   """
              """ 8       d8888888
\033[1;30m      8 .od88888888888888888888888888888888   """
              """ 8      d88888888
\033[1;30m      8888888888888888888888888888888888888   """
              """ 8     d888888888
\033[1;30m                                              """
              """ 8    d8888888888
\033[1;30m         ooooooooooooooooooooooooooooooo      """
              """ 8   d88888888888
        d                       ...oood8b      8  d88888"""
              """8888888
       d              ...oood888888888888b     8 d888888"""
              """8888888
      d     ...oood88888888888888888888888b    8d8888888"""
              """8888888
     dood8888888888888888888888888888888888b
\033[0;0m
""")

        print('\033[1000;1000H')

    @staticmethod
    def apply_face(name: str) -> None:
        """ Get an ascii face depending
         on the input 'name' """
        searching = [
            '\033[1;37m                              ',
            '          ██         ██       ',
            '        ████       ████       ',
            '                              ',
            "                              ",
            '                              ',
            '                   ████       ',
            '           █████████          ',
            '                              '
            ]
        found = [
            '\033[1;37m                          ███ ',
            '        ████       ████   ███ ',
            '        █  █       █  █   ███ ',
            '        ████       ████       ',
            "                          ███ ",
            '          █████████           ',
            '          ██    ███           ',
            '           ██████             ',
            '                              '
            ]
        happy_face = [
            '\033[1;37m                              ',
            '        ████       ████       ',
            '        ████       ████       ',
            '                              ',
            "                              ",
            '       ████        ████       ',
            '       ████        ████       ',
            '           ████████           ',
            '                              '
            ]
        screen_x = Visualizer.screen_x
        screen_y = Visualizer.screen_y
        match name:
            case 'searching':
                face = searching
            case 'found':
                face = found
            case _:
                face = happy_face
        for line in face:
            print(f'\033[{screen_y};{screen_x}H{line}')
            screen_y += 1

    def process(self, processor: PromptProcessor) -> List[Any]:
        """ Use the given processor to process its data,
         and visualize it in the process. """
        screen_x = 70
        screen_y = 15
        processed = 1
        output = []
        for prompt in processor.get_prompts():
            self.visualize()
            print(f'\033[1;37m\033[{screen_y + 5};{screen_x}HProgressio' +
                  f'n: {((processed / processor.nb_prompts) * 100):.2f}%')
            print(f'\033[1;37m\033[{screen_y + 6};{screen_x}HMade' +
                  ' with ♥ by gtourdia')
            for state in processor.yield_process(prompt):
                self.apply_face('searching')
                print(f'\033[0;32m\033[{screen_y};{screen_x}H=== ' +
                      f'State: {state['current_state']} ===')
                print(f'\033[0;32m\033[{screen_y + 1};{screen_x}HPrompt: ' +
                      f' {state['prompt']}')
                if (state['name']):
                    self.apply_face('found')
                    print(f'\033[0;32m\033[{screen_y + 2};{screen_x}HFun' +
                          f'ction name: {state['name']}')
                if (state['parameters']):
                    self.apply_face('happy')
                    print(f'\033[0;32m\033[{screen_y + 3};{screen_x}HParam' +
                          'eters: processing...')
                    time.sleep(2)
                    prompt_output = state
                    del state['current_state']
            output.append(prompt_output)
            processed += 1
            print('\033[1000;1000H')
        return output


if __name__ == '__main__':
    v = Visualizer()
    v.visualize()
