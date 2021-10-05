i = input('welke dag wil je zien')
startdag = ""

while i != startdag:

    print(startdag)
    if startdag == "maandag":
        startdag = "dinsdag"
    elif startdag == "dinsdag":
        startdag = "woensdag"
    elif startdag == "woensdag":
        startdag = "donderdag"
    elif startdag == "donderdag":
        startdag = "vrijdag"
    elif startdag == "vrijdag":
        startdag = "zaterdag"
    elif startdag == "zaterdag":
        startdag = "zondag"
    else:
        startdag = "maandag"

print(i)
    
