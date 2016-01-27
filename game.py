import wikipedia        #importing python wiki package
while True:
    print "----------------"
    print "WHEN WAS HE BORN"
    print "----------------"
    name=raw_input("Enter a name of someone famous : ")
    summary=""
    try:
        summary=wikipedia.summary(name.title(), sentences=1)
    except:
        print "Please make sure you typed the correct spelling."
    if summary:
        print summary
        print summary[0:summary.find("(")] + summary[summary.find(")")+2:]      #To strip out the content inside the bracket
        print summary[summary.find("born")+5:summary.find(")")]                 #The find the birth date
    raw_input("Click enter to start again.")
