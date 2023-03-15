# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print("Done!")

# secret_number = 9
# attempts = 3
# while int(input("Try! ")) != secret_number:
#     attempts -= 1
#     if attempts == 0:
#         print("Looser !!!")
#         break

# ====================================== secret_number!
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess! "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else: # this else for while loop!
#     print("You loose!")

# ====================================== car game!
command = ""
isStarted = False
isStopped = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if isStarted:
            print("Car already started!")
            continue
        print("Car started...")
        isStarted = True
        isStopped = False
    elif command == 'stop':
        if isStopped:
            print("Car already stopped!")
            continue
        print("Car stop.")
        isStopped = True
        isStarted = False
    elif command == 'quit':
        break
    elif command == 'help':
        print("""
start - to start
stop - to stop
quit - to quit
        """)
    else:
        print(f"I do not understand [{command}]")
