import random

    # card selected
suma = 0
sumb = 0
sumc = 0
sumd = 0
# S = "global"
round_0f_game = int(input("Number of time u want to play : "))
i = 1

while i <= round_0f_game:
    # random & suffle
    list = [40, 60, 80, 100];
    random.shuffle(list)
    a = list[0]
    b = list[1]
    c = list[2]
    d = list[3]
    print(a,b,c,d)
    playerChoice = input('Press a for select card')
    # playerChoice = a = list[0]

    if (playerChoice.__eq__('a')):
        a = list[0]
        b = list[1]
        c = list[2]
        d = list[3]
        print('Your score', a, b, c, d)
    elif (playerChoice.__eq__('b')):
        sum = list[0] + list[1]
        a = sum - list[0]
        b = sum - list[1]
        c = list[2]
        d = list[3]
        print('Your score', a, b, c, d)
    # else:
    #     print('Garvage Value')
    elif (playerChoice.__eq__('c')):
        sum3 = list[0] + list[2]
        a = sum3 - list[0]
        b = list[1]
        c = sum3 - list[2]
        d = list[3]
        print('Your score', a, b, c, d)
    elif (playerChoice.__eq__('d')):
        sum4 = list[0] + list[3]
        a = sum4 - list[0]
        b = list[1]
        c = list[2]
        d = sum4 - list[3]
        print('Your score', a, b, c, d)
    else:
        print('G')



    def cardChoiceFunction():
        if (playerChoice.__eq__('a')):
            print('Your score', list[0])
        elif (playerChoice.__eq__('b')):
            print('Your score', list[1])
        elif (playerChoice.__eq__('c')):
            print('Your score', list[2])
        elif (playerChoice.__eq__('d')):
            print('Your score', list[3])


    cardChoiceFunction()
    # Babu identification
    babuIdentify = input('###Who is BABU ?')
    print(babuIdentify)


    # babuIdentify function
    def babuIdentifyFunction():
        if (playerChoice.__eq__('a') and a == 100 or playerChoice.__eq__('b') and b == 100 or
                playerChoice.__eq__('c') and c == 100 or playerChoice.__eq__('d') and d == 100):
            print('You are babu bro')
        else:
            if (a == 100):
                print('Player A is babu')
            elif (b == 100):
                print('Player B is babu')
            elif (c == 100):
                print('Player C is babu')
            elif (d == 100):
                print('Player D is babu')


    babuIdentifyFunction()
    # Police identification
    policeIdentify = input('###Who is POLICE?')


    def policeIdentifyFunction():
        if (playerChoice.__eq__('a') and a == 80 or playerChoice.__eq__('b') and b == 80 or
                playerChoice.__eq__('c') and c == 80 or playerChoice.__eq__('d') and d == 80):
            print('You are police bro')

        else:
            if (a == 80):
                print('Player A is police')
            elif (b == 80):
                print('Player B is police')
            elif (c == 80):
                print('Player C is police')
            elif (d == 80):
                print('Player D is police')


    policeIdentifyFunction()


    # calculation

    def calculation():
        global suma
        global sumb
        global sumc
        global sumd
        if (playerChoice.__eq__('a') and a == 80 or playerChoice.__eq__('b') and b == 80 or playerChoice.__eq__(
                'c') and c == 80 or playerChoice.__eq__('d') and d == 80):
            x = input('###find out who is theif')
            y = input('Is he theif or robber')
            if (x.__eq__('a') and y.__eq__('theif') and a == 40 or x.__eq__('a') and y.__eq__('robber') and a == 60):
                suma = suma + 0
                sumb = sumb + b
                sumc = sumc + c
                sumd = sumd + d
            elif (x.__eq__('b') and y.__eq__('theif') and b == 40 or x.__eq__('b') and y.__eq__('robber') and b == 60):
                suma = suma + a
                sumb = sumb + 0
                sumc = sumc + c
                sumd = sumd + d
            elif (x.__eq__('c') and y.__eq__('theif') and c == 40 or x.__eq__('c') and y.__eq__('robber') and c == 60):
                suma = suma + a
                sumb = sumb + b
                sumc = sumc + 0
                sumd = sumd + d
            elif (x.__eq__('d') and y.__eq__('theif') and d == 40 or x.__eq__('d') and y.__eq__('robber') and d == 60):
                suma = suma + a
                sumb = sumb + b
                sumc = sumc + c
                sumd = sumd + 0
                # for normal police
            else:
                if (playerChoice.__eq__('a') and a == 80):
                    suma = suma + 0
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + d
                elif (playerChoice.__eq__('b') and b == 80):
                    suma = suma + a
                    sumb = sumb + 0
                    sumc = sumc + c
                    sumd = sumd + d
                elif (playerChoice.__eq__('c') and c == 80):
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + 0
                    sumd = sumd + d
                elif (playerChoice.__eq__('d') and d == 80):
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + 0

        else:
            # m = input('find out who is theif a?b?c?d? ')
            if (a == 100 and b == 80):
                x = ['c', 'd']
                random.shuffle(x)
                if (x[0].__eq__('c') and c == 40):
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + 0
                    sumd = sumd + d
                elif (x[1].__eq__('d') and d == 40):
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + 0
                else:
                    suma = suma + a
                    sumb = sumb + 0
                    sumc = sumc + c
                    sumd = sumd + d
                # Condition 2

            elif (a == 100 and c == 80):
                x = ['b', 'd']
                random.shuffle(x)
                if (x[0].__eq__('b') and b == 40):
                    suma = suma + a
                    sumb = sumb + 0
                    sumc = sumc + c
                    sumd = sumd + d
                elif (x[1].__eq__('d') and d == 40):
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + 0
                else:
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + 0
                    sumd = sumd + d
                # Condition 3

            elif (a == 100 and d == 80):
                x = ['b', 'c']
                random.shuffle(x)
                if (x[0].__eq__('b') and b == 40):
                    suma = suma + a
                    sumb = sumb + 0
                    sumc = sumc + c
                    sumd = sumd + d
                elif (x[1].__eq__('c') and c == 40):
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + 0
                    sumd = sumd + d
                else:
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + 0
                # Condition 4
            if (b == 100 and a == 80):
                x = ['c', 'd']
                random.shuffle(x)
                if (x[0].__eq__('c') and c == 40):
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + 0
                    sumd = sumd + d
                elif (x[1].__eq__('d') and d == 40):
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + 0
                else:
                    suma = suma + 0
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + d
                # Condition 5

            if (b == 100 and c == 80):
                x = ['a', 'd']
                random.shuffle(x)
                if (x[0].__eq__('a') and a == 40):
                    suma = suma + 0
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + d
                elif (x[1].__eq__('d') and d == 40):
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + 0
                else:
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + 0
                    sumd = sumd + d
                # Condition 6
            elif (b == 100 and d == 80):
                x = ['a', 'c']
                random.shuffle(x)
                if (x[0].__eq__('a') and a == 40):
                    suma = suma + 0
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + d
                elif (x[0].__eq__('c') and c == 40):
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + 0
                    sumd = sumd + d
                else:
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + 0
                # Condition 7
            if (c == 100 and a == 80):
                x = ['b', 'd']
                random.shuffle(x)
                if (x[0].__eq__('b') and b == 40):
                    suma = suma + a
                    sumb = sumb + 0
                    sumc = sumc + c
                    sumd = sumd + d
                elif (x[1].__eq__('d') and d == 40):
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + 0
                else:
                    suma = suma + 0
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + d
                # Condition 8
            if (c == 100 and b == 80):
                x = ['a', 'd']
                random.shuffle(x)
                if (x[0].__eq__('a') and a == 40):
                    suma = suma + 0
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + d
                elif (x[1].__eq__('d') and d == 40):
                    suma = suma + a
                    sumb = sumb + 0
                    sumc = sumc + c
                    sumd = sumd + d
                else:
                    suma = suma + a
                    sumb = sumb + 0
                    sumc = sumc + c
                    sumd = sumd + d
                # Condition 9
            elif (c == 100 and d == 80):
                x = ['b', 'a']
                random.shuffle(x)
                if (x[0].__eq__('a') and a == 40):
                    suma = suma + 0
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + d
                elif (x[1].__eq__('b') and b == 40):
                    suma = suma + a
                    sumb = sumb + 0
                    sumc = sumc + c
                    sumd = sumd + d
                else:
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + 0
                # Condition 10
            if (d == 100 and a == 80):
                x = ['b', 'c']
                random.shuffle(x)
                if (x[0].__eq__('b') and b == 40):
                    suma = suma + a
                    sumb = sumb + 0
                    sumc = sumc + c
                    sumd = sumd + d
                elif (x[1].__eq__('c') and c == 40):
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + 0
                    sumd = sumd + d
                else:
                    suma = suma + 0
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + d
                # Condition 11
            if (d == 100 and b == 80):
                x = ['a', 'c']
                random.shuffle(x)
                if (x[0].__eq__('a') and a == 40):
                    suma = suma + 0
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + d
                elif (x[1].__eq__('c') and c == 40):
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + 0
                    sumd = sumd + d
                else:
                    suma = suma + a
                    sumb = sumb + 0
                    sumc = sumc + c
                    sumd = sumd + d
                # Condition 12
            elif (d == 100 and c == 80):
                x = ['a', 'b']
                random.shuffle(x)
                if (x[0].__eq__('a') and a == 40):
                    suma = suma + 0
                    sumb = sumb + b
                    sumc = sumc + c
                    sumd = sumd + d
                elif (x[1].__eq__('b') and b == 40):
                    suma = suma + a
                    sumb = sumb + 0
                    sumc = sumc + c
                    sumd = sumd + d
                else:
                    suma = suma + a
                    sumb = sumb + b
                    sumc = sumc + 0
                    sumd = sumd + d


    calculation()

    print(suma)
    print(sumb)
    print(sumc)
    print(sumd)

# print(suma)
# print(sumb)
# print(sumc)
# print(sumd)

