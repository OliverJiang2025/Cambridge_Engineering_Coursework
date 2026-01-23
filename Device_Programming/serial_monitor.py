import serial

ser = serial.Serial('COM3',9600,timeout=1)

try:
    while True:
        if ser.in_waiting > 0:
            
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
except KeyboardInterrupt:
    print("interrupted")
finally:
    ser.close()