import time 
samay = time.strftime('%H:%M:%S')
print(samay)
samay = int(time.strftime('%H'))
samay1 = int(time.strftime('%M'))
samay2= int(time.strftime('%S'))
if(samay<12):
    print("GOOD MORNING")
elif(samay>12 and samay<19):
  print("GOOD AFTERNOON")
elif(samay>=19 and samay<21):
   print("GOOD EVENING")
else:
   print("GOOD NIGHT")