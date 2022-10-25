import serial
print ('Serial Iniciada...\n')
while True:
    comport = serial.Serial('/dev/ttyUSB0', 9600) 

    retorno = comport.read(8)
    print(retorno)
    comport.close()