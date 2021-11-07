#Phone Number validation check

phone = input("Please enter the Phone Number: ")

if phone > "0000000000" and phone < "9999999999" and len(phone) == 10:
    print("Un-formatted Number =", phone)
    print("Formatted Number: ", "{}-{}-{}".format(phone[:3], phone[3:6], phone[6:]))
else:
    print("Invalid Phone Number!")



