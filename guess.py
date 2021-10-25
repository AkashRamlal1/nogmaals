import random

nummer = random.randint(1, 1000)
answer = int(input('raad het getal '))
kansen = 6



while  answer != nummer:
    print(nummer)
    if answer == nummer:
        print("correct!")
    elif answer < nummer:
        print("hoger")
        answer = int(input('raad het getal'))
        if answer == nummer:
            print("correct!")
        elif answer < nummer:
            print("hoger")
            kansen = kansen - 1
            print("je hebt nog ", kansen, " kansen")
            if kansen < 1:
                break
            elif (answer - nummer) <= 50:
                print("warm")
            elif (answer - nummer) >= 100:
                print("koud")

        elif answer > nummer:
            print("lager")
            kansen = kansen - 1
            print("je hebt nog ", kansen, " kansen")
            if kansen < 1:
                break
    elif answer > nummer:
        print("lager")
        answer = int(input('raad het getal'))
        if answer == nummer:
            print("correct!")
            kansen = kansen - 1
            print("je hebt nog ", kansen, " kansen")
            if kansen < 1:
                break
        elif answer < nummer:
            print("hoger")
        elif answer > nummer:
            print("lager")
            kansen = kansen - 1
            print("je hebt nog ", kansen, " kansen")
            if kansen < 1:
                break
        
    