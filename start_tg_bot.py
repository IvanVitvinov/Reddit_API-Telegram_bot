import subprocess
import schedule
import time


def run_python_file(filename):
    subprocess.run(['python', filename])


def run_files():
    file1 = 'get_data.py'
    file2 = 'telegram_bot.py'

    # Run file1.py
    print(f'Started collecting information')
    run_python_file(file1)
    print(f'Finished collecting information')

    # Run file2.py
    print(f'Started sending message')
    run_python_file(file2)
    print(f'Finished sending message')


def main():

    # Run files for the first time
    run_files()

    # Run files every 6 hours
    schedule.every(30).minutes.do(run_files)

    while True:
        schedule.run_pending()
        time.sleep(3)


if __name__ == '__main__':
    main()
