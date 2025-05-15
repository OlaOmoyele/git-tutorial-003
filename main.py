import pathlib
import utilities

program_name: str = pathlib.Path(__file__).name
program_version: str = '1.2.0'

class Main():

    def __init__(self) -> None:
        print(f'Running {program_name} v{program_version}')
        utilities.welcome_msg()

    def quit(self) -> None:
        print()
        print('End of Script')
        print('-'*30)

if __name__ == '__main__':
    main = Main()
    main.quit()
