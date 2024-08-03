def reverse_number(number):
 reverse = 0 
 while(number > 0):
     reminder = number %10
     reverse = (reverse *10) + reminder
     number = number //10
 print("Reverse number is ", reverse)
reverse_number(1546)
