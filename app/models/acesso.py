import serial
def lercartao():
    comport = serial.Serial('/dev/ttyUSB0', 9600) 
    retorno = comport.read(8)
    comport.close()
    return(str(retorno).replace("'","").replace(" ","").replace("\r",""))
