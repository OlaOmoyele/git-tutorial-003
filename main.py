import pathlib
import utilities
import time

script_name: str = pathlib.Path(__file__).name
script_version: str = '1.3.0'

class Main():

    def __init__(self) -> None:
        print(f'Running {script_name} v{script_version}')
        utilities.welcome_msg()

    def quit(self) -> None:
        print()
        print('End of Script')
        print('-'*30)

if __name__ == '__main__':
    main = Main()
    time.sleep(2)
    main.quit()
