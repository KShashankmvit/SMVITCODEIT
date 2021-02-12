function=""
while function!="stop":
    function=input('>')
    if function=="start":
        print("car has started moving")
    elif function=="help":
        print("to start the vehlicle press start\n to stop vehicle press stop ") 
    elif function=="stop":
        print("Vehicle stops") 
        break;                 