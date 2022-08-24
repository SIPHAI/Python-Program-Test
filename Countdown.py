import time
def countdown(t):
    while t:
        mins, secs, = divmod(t,60)
        timer = '{:02d}:{:0d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        t -= 1
    print('Fire in the hole !!')

t = input("Enter the time in ssecond: ")
countdown(int(t))