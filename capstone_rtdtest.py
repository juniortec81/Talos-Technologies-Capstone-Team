###Talos Tech Capstone Test###
##############################
import time
import datetime
import librtd
import csv

# start elapsed time timer
start = time.time()
print('Start of Test')
# to print the time that has passed variable at bottom
timeCounter = 0
t = 0
exit_program = ''
# field names
fields = ['Date', 'Local Time', 'Elapsed Time (s)','RTD1.100: R in ohms','Sensor1.100: Temp in C','RTD2.100: R in ohms', 'Sensor2.100: Temp in C']
# row names
rows = []


# name of csv file
filename = 'Capstone_SensorTest1.csv'

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    while True:
        # functions to use
        def get_date():
            date = datetime.date.today()
            date = str(date)
            return date
        
        def get_Localtime():
            current_time = time.localtime()
            localtime1 = time.strftime('%H:%M:%S', current_time)
            localtime1 = str(localtime1)
            rows.append(localtime1)
            return localtime1
 
        #def get_elapsedtime():
            #currenttime = time.localtime()
            #elapsedtime = currenttime - Start_time
            #return elapsedtime
        # get_Heater():
            #return heaterstatus
        def get_rtdResPT100():
            # get RTD current resistance value
            rtdRes100 = librtd.getRes(0, 3)
            rtdRes100 = '%.4f' % rtdRes100
            rtdRes100 = str(rtdRes100)
            return rtdRes100

        
        def get_SensorPT100():
            # get rtd current temp value in C
            rtdtemp100C = librtd.get(0, 3)
            rtdtemp100C = '%.4f' % rtdtemp100C
            rtdtemp100C = str(rtdtemp100C)
            return rtdtemp100C
        
        def get_rtdRes2PT100():
            # get RTD current resistance value
            rtdRes2100 = librtd.getRes(0, 6)
            rtdRes2100 = '%.4f' % rtdRes2100
            rtdRes2100 = str(rtdRes2100)
            return rtdRes2100

        
        def get_Sensor2PT100():
            # get rtd current temp value in C
            rtd2temp100C = librtd.get(0, 6)
            rtd2temp100C = '%.4f' % rtd2temp100C
            rtd2temp100C = str(rtd2temp100C)
            return rtd2temp100C

        # time elapsed section/formula
        elapsed_time = (time.time() - start) + 5
        elapsed_time = '%.2f' % elapsed_time
        elapsed_time = str(elapsed_time)
        
        # writing the data rows. temp. in C
        rows = [get_date(), get_Localtime(), elapsed_time, get_rtdResPT100(), get_SensorPT100(), get_rtdRes2PT100(), get_Sensor2PT100()] 
        csvwriter.writerow(rows)    # writing the fields
        rows = []    # clear previous data for new data reading
        
        csvfile.flush() # need! writes context of the buffer to the destination and makes the buffer empty for further data to store.
        time.sleep(1)    # wait for 1 second 
        print('Current time:{} | Elapsed time:{} sec. | Current Temp in C:{}'
              .format(get_Localtime(), elapsed_time, get_SensorPT100()))




