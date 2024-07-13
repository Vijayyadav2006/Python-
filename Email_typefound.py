email = input("Enter you're email:")
if email.endswith(('.com','.org','.edu','.in')):
    print("Valid Emali entered",email)
else:
    print("Invalid")