
import time
import os

def break_time(interval,no_breaks):
    break_count = 0

    print('Pogram Startd on ' + time.ctime())
    while break_count < no_breaks:
        time.sleep(interval)
        #webbrowser.open('https://google.com')
        os.startfile(r"C:\Users\yyy\Music\01 Julia Michaels Issues.mp3")
        break_count += 1

break_time(5*60,2)
