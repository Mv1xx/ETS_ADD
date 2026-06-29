import time

#quantos segundos se passaram desde 1970
sec= time.time()
print(sec)

#possivel fazer operações
sec2 = time.time()
print(sec2)
print(sec2 - sec)

#
tempo = time.localtime(sec)
print(tempo)

tempo.tm_year
tempo.tm_mon
tempo.tm_mday
tempo.tm_hour
tempo.tm_min
tempo.tm_sec
