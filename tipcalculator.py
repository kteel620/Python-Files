import time


start0 = False
while(start0 == False):
    subtotal0 = input("Enter the total amount for the bill (numbers only). ")
    try:
        sub = float(subtotal0)
        start0 = True
    except ValueError:
        print("The input is not a number. ")
        continue

subtotal = float(subtotal0)

start1 = False
while(start1 == False):
    person0 = input("Enter the amount of people paying. ")
    if(person0.isdigit() == True):
        start1 = True
    else:
        print("Please enter a whole number that is not a decimal or zero and below. ")
        continue
person = int(person0)

#tax = 1.0+float(input("What is the tax rate? "))/100
#To avoid one redundant step I'll assume we're in NY so the tax rate is 8.75 percent
tax = 1.0875

start2 = False
while(start2 == False):
    tip0 = input("How much do you want to tip? ")
    try:

        tippy = float(tip0)
        if(tippy < 0):
            print("Please enter a number greater than 0!")
            continue

        if(tippy >= 0):
            start2 = True
    except ValueError:
        print("Please enter a number greater than 0. ")
        continue

tip = 1.0 +(float(tip0)/100)

total = (subtotal*(tax))*(tip)
print("The total bill is %.2f. " % total)
taxtip_total = total - subtotal


list_of_people = []

#Now for the interesting part. Collecting the data on how many people ate and how much each person paid.
start = False
while(start == False):
    for i in range(person):
        bills = float(input("How much did person "+str(int(i+1))+" buy? "))
        list_of_people.append(bills)
    if(int(sum(list_of_people)) != int(subtotal)):
        print("Wait. ")
        time.sleep(1.5)
        print("This doesn't add up properly")
        print("The subtotal was "+str(int(subtotal)) + ".")
        time.sleep(1)
        print("You entered "+str(int(sum(list_of_people))))
        time.sleep(1)
        exit = input("Let's try again. If you want to exit, press X. If not, press anything else. ")
        list_of_people = []
        if (exit.lower() == "x"):
            time.sleep(1)
            print("Ok.")
            exit()
        else:
            continue

    elif(int(sum(list_of_people)) == int(subtotal)):
        start = True

print(list_of_people)

portion = []
for a in list_of_people:
    div = (a/subtotal)
    portion.append(div)

print(portion)

total_per_person = []
for b in range(person):
    tot_per_peep = list_of_people[b] + (portion[b] * taxtip_total)
    total_per_person.append(tot_per_peep)


print(total_per_person)
print(sum(total_per_person))

for c in range(person):
    print("Person " + str(int(c+1))+" should pay: " + "%.2f" % total_per_person[c] )
