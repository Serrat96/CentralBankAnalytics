import os
import time

while True:
    start = input('Where are you?')
    final = input('Which file or directory would you like to reach?')

    relative_path = str(os.path.relpath(final, start))

    print('The relative path is: \n' + relative_path)

    control = input('Do you want to know another relative path? y/n: ')
    if control == 'y':
        continue
    else:
        print('Closing program...')
        time.sleep(0.5)
        break