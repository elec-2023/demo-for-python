import serial


ser = serial.Serial('/dev/ttyS0', 19200)
ser.write('xxxxx'.encode())