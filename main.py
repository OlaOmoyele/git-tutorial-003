import pathlib
import utilities

app_name: str = pathlib.Path(__file__).name
app_version: str = '1.3.0'

class Main():

    def __init__(self) -> None:
        print(f'Running {app_name} v{app_version}')
        utilities.welcome_msg()

    def quit(self) -> None:
        print()
        print('End of Script')
        print('-'*30)

if __name__ == '__main__':
    main = Main()
    main.quit()
