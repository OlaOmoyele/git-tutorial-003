import pathlib
import utilities

program_name: str = pathlib.Path(__file__).name
program_version: str = '1.1.0'

if __name__ == '__main__':
    print(f'Running {program_name} v{program_version}')
    utilities.welcome_msg()

    print()
    print('End of Script')
    print('-'*30)
