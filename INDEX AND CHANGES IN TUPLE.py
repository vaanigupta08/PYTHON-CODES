MyTuple = (52 , 41 , 300 , 10 , (85 , 58 , 32 ,) , (1200 , 789) , (741, 45,))
print('\n Index position:' , MyTuple[6][-1])

Friends = (85,20,1, ['Raima' , 'Jenifer' , 'Betty' , ['Tina' , 'Julia']])
print('\n My best friend:' , Friends[3][-1][0])

## MAKING MODIFICATIONS IN TUPLE THOUGH IT IS NON-CHANGEABLE

Mytuple = (52 , 780 , 96 , 420)
print('\n tuple to list con:' , list(Mytuple))
Newlist = list(Mytuple)
print('\n TUPLE TO LIST DATATYPE:' , type(Newlist))
Newlist.append(85)
print(Newlist)

print('\n LIST TO TUPLE CON AFTER MODIFICATION:' , tuple(Newlist))

Myname = 'VAANI GUPTA'
Myname.isalpha()
print('\n ALPHABETS:' , bool(Myname))
print('\n NUMBERS:' , Myname.isdigit())