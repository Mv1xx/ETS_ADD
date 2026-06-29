from datetime import datetime

#imprime a data + horario de hoje
dat = datetime.now() 
print(dat)

dat.year
dat.month
dat.day
dat.hour
dat.minute
dat.second
dat.datmicrosecond

timestr = dat.strftime("%d-%b-%y (%H:%M:%S.%f)")
print(timestr)
