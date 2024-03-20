timer = int(input("Enter the time in number of seconds: "))
print(timer)
while timer > 0 :
    min = int(timer/60)
    sec = int(timer % 60)
    message = f'{min} : {sec}'
    print(message)
    timer = timer - 1

print("Time is finished")