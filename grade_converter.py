# FILE NAME - grade_converter.py

# NAME: Ben Snider
# DATE: October 1, 2025
# BRIEF DESCRIPTION: Grade Converter 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
print('===== Grade Converter =====')
grade = int(input('Enter a numerical grade (1-100): '))
if grade > 100:
    print('A+')
elif 90 <= grade <= 100:
    print('A')
elif 80 <= grade <= 90:
    print('B')
elif 70 <= grade <= 80:
    print('C')
elif 65 <= grade <= 70:
    print('D')
elif grade < 65:
    print('F')
########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?
I think I would just tell a future student to read the notebook carefully and to watch all of the included videos.






'''
