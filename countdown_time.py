import time

user_time = int(input("Please Enter your Timer")) 
def countDown_timer(user_time):
    while user_time:
        mins , sec= divmod(user_time , 60)
        # second => 02d
        timer_def = '{:02d} : {:02d}'.format(mins , sec)
        print(timer_def , end="\r")
        time.sleep(1)
        user_time -=1
    print("time has up")
countDown_timer(user_time)