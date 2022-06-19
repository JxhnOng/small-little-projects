import random 

#variables

secondary = str() #declares 'secondary' as a string variable
primary = str() #declares 'primary' as a string variable

secondary = ['Classic', 'Shorty', 'Frenzy', 'Ghost', 'Sheriff'] #assigns a list of strings to the variable 'secondary'
primary = ['Stinger', 'Spectre', 'Bucky', 'Judge', 'Bulldog', 'Guardian', 'Phantom', 'Vandal', 'Marshal', 'Operator', 'Ares', 'Odin'] #assigns a list of strings to the variable 'primary'

while True: #runs forever, until closed
    print("Primary gun: " + random.choice(primary)) #prints a random string from 'primary'
    input("Secondary gun: " + random.choice(secondary)) #prints a random string from 'secondary'
    print()