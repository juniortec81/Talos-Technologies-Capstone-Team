import librtd
import time

while True:
    test = librtd.get(0,1)
    testres = librtd.getRes(0,1)
    Fer = (test*9/5)+32
    print('Tempemperature C {} Resistance {}'.format('%.4f' % test,'%.4f' % testres))
    time.sleep(1) 