nume = int(input("Entre com o tempo em segundos: "))

horas = nume // 3600
nume = nume % 3600
minutos = nume // 60
segundos = nume % 60

print('{}:{}:{}'.format(horas, minutos, segundos))