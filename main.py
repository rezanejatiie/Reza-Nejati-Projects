import STH20
import wicon
import time
i = 0

API_key = '******************'

while True:
    i = i +1
    wicon.connect()
    time.sleep(10)
    temp = STH20.readtemp() 
    #temp = 12
    temp = str(temp)  
    humid = STH20.readumid()
    #humid = 12
    humid = str(humid)
    wicon.thingspeak_post(API_key,temp,humid)
    time.sleep(20)
    print('')
    print('Reza')
    print(i)
    print('temp = ', temp)
    print('humid = ', humid)
    time.sleep(30)



