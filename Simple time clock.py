import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print("Time=",t)
if(hour>0 and hour<12):
    print("Good mourning")
elif(hour>=12 and hour<=17):
    print("Good afternoon")
elif(hour>17 and hour<20):
    print("Good evening")
elif(hour>=20 and hour<=24):
    print("Good night")


