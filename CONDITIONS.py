Happy = 30
Silly = 30

# USING THE CONDITION IF AND ELSE

if 50 > 30: 
    print('\n Happy is greater than Silly.')
else:
    print('\n Silly is greater.')

# USING THE CONDITION ELIF

if 30 != 30:
    print('\n Both are not equal.')
elif 30 < 30:
    print('\n Silly is more.')
elif 30 >= 30:
    print('\n Happy is greater than or equal to Silly.')
elif 30 == 30:
    print('\n Both are equal.')     
else:
    print('\n None of them are right.')  

first, second, third = 80, 60, 40

# CONDITIONS USING AND, OR, NOT

if (80 > 60) and (60 < 40):
    print('\n Sorry, I am wrong.')
elif (40 > 80) or (60 > 40):
    print('\n My condition is right.')
elif (60 > 40) and not (80 > 60):
    print('\n My separated condition is here.')

# condition using 'in'

Mymemory = ['Parks', 'Temples', 'Museums'] 
if 'Temples' in Mymemory:
    print('\n I love', Mymemory[1])

    memory = input('\n Kindly enter your place of visit:')

if bool(memory) == True:
    print('\n I enjoy a lot in ' , Mymemory[0])
else:
    print('\nPlease enter your place.') 

    