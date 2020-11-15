import RPi.GPIO as GPIO #просто комментарий аоаоаоаоаоа
import time

bit_depth = 8
def bin_convert(number):
    N = bit_depth - 1
    p = 0
    X = []
    n = number
    while N > 0:
        p = int(n/2**N)
        if p == 1:
            X.append(1)
            n-=2**N
        else:
            X.append(0)
        N-=1
    X.append(n)
    return X

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

D=[26,19,13,6,5,11,9,10]



def num2dac(value):
    bin_convert(number)
    Y = bin_convert(number)
    l = 0
    for j in Y:
        if j == 1:
            GPIO.output(D[l], 1)
        if j == 0:
            GPIO.output(D[l], 0)
        l = l + 1

    
while True:
    print("Enter the number you want (press -1 + enter to exit)")
    number = int (input())
    if (number == -1):
        GPIO.output(D,0)
        break

    else:
        print(bin_convert(number))
        num2dac(number)
