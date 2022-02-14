# write your code here
import random

print("Enter the number of friends joining (including you):")
guest_number = int(input())
print()

if guest_number <= 0:
    print("No one is joining for the party")
else:
    guest = []
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(guest_number):
        name = input()
        guest.append(name)
    print()

    print("Enter the total bill value:")
    bill = float(input())
    print()

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    input_lucky = input()
    print()
    if input_lucky == 'Yes':
        lucky_guest = random.choice(guest)
        print(lucky_guest, "is the lucky one!")
    else:
        print("No one is going to be lucky")
    print()

    if input_lucky == 'Yes':
        pay_per_person = int(round(bill / (len(guest) - 1), 2))
        bill_splitter = dict.fromkeys(guest, pay_per_person)
        bill_splitter[lucky_guest] = 0
    else:
        pay_per_person = int(round(bill / (len(guest)), 2))
        bill_splitter = dict.fromkeys(guest, pay_per_person)
    print(bill_splitter)
