import pathlib
import utilities

software_name: str = pathlib.Path(__file__).name
software_version: str = '1.3.0'

class Main():

    def __init__(self) -> None:
        print(f'Running {software_name} v{software_version}')
        utilities.welcome_msg()

    def quit(self) -> None:
        print()
        print('End of Script')
        print('-'*30)

if __name__ == '__main__':
    main = Main()
    main.quit()
