from time import sleep

def countdown(second):

    while second:
        print(f'{second} SECOND(S)!')
        second -= 1

    print('HAPPY NEW YEAR!')

def countdown_with_sleep(second):

    while second:
        print(f'{second} SECOND(S)!')
        second -= 1
        sleep(1)

    print('HAPPY NEW YEAR!')