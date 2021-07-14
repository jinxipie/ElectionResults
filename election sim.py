import numpy

numpp = int(input("Please type the number of political parties you have, then press ENTER "))
parties = {}

for num in range(numpp):
    antry = input("Please type party number "+str(num+1)+"\'s name in, then press ENTER ").lower()
    parties[antry] = float(input("Please type typical party vote share in percentage points, then press ENTER ").replace("%",""))

coalea = input("Who is the leader of the incumbent coalition? ").lower()
apprrating = float(input("What is the government's approval rating? "))
supply = input("Name other coalition members, with commas separating entries. ").lower().split(", ")

numdists = int(input("How many election districts/ridings are there? "))

addlqs = input("Would you like to answer additional questions to improve accuracy, YES or NO? ").lower()
addlqslist = []
aqlcount = 0
if addlqs == "yes":
    addlqslist.append(bool(input("True or False, the government lost seats in the most recent election ")))
    addlqslist.append(bool(input("True or False, the current leader of parliament is seeking re-election ")))
    addlqslist.append(bool(input("True or False, there is not an ongoing recession ")))
    addlqslist.append(bool(input("True or False, the current administration has made significant policy changes ")))
    addlqslist.append(bool(input("True or False, there is *no* social unrest ")))
    addlqslist.append(bool(input("True or False, there has been *no* major scandal with the administration ")))
    addlqslist.append(bool(input("True or False, the military has been successful this administration ")))
    addlqslist.append(bool(input("True or False, the incumbent is significantly more charismatic than their challenger ")))
    aqlcount = 0
    for entry in addlqslist:
        if entry == True:
            aqlcount += 1
else:
    aqlcount = 4

#parties = {'ouro':69.3,'boros':30.7}
#ranked = True


partyseatsdict = {}
listforprint = [["District"]]
for entry in parties:
    partyseatsdict[entry] = 0
    listforprint[0].append(entry)
listforprint[0].append("Winner")

whichdistis = 1
for distr in range(numdists):
    listforprint.append([])
    totseats = 0
    
    partyvotesdict = {}
    pvt = 0
    for entry in parties:
        randnum = numpy.random.normal(loc=0.0,scale=5.0,size=None)
        if entry == coalea:
            tally = (.5*parties[entry]+(apprrating)*parties[entry]/100)+randnum+(aqlcount-4)
        elif entry in supply:
            tally = (.5*parties[entry]+(apprrating)*parties[entry]/100)+randnum+(aqlcount-4)
        else:
            tally = (.5*parties[entry]+(100-apprrating)*parties[entry]/100)+randnum+(aqlcount-4)*-1
        if tally < 0:
            tally = 0
            print("tally less than 0")
        partyvotesdict[entry] = tally
        pvt += tally
        if pvt == 0:
            pvt = 1
    print("Votes for district "+str(whichdistis)+" below")
    listforprint[whichdistis].append("District "+str(whichdistis))
    for entry in partyvotesdict:
        partyvotesdict[entry] /= pvt
        listforprint[whichdistis].append(partyvotesdict[entry])
    print(partyvotesdict)
    
    for entry in partyvotesdict:
        if partyvotesdict[entry] > .5:
            totseats +=1
            partyseatsdict[entry] += 1
            listforprint[whichdistis].append(entry)
            print("winner: "+entry)
            
    if totseats == 0:
        alist = [[],[]]
        for entree in partyvotesdict:
            alist[0].append(entree)
            alist[1].append(partyvotesdict[entree])
        maxi = max(alist[1])
        desind = alist[1].index(maxi)
        savedent = alist[0][desind]
        partyseatsdict[savedent] += 1
        listforprint[whichdistis].append(savedent)
        print("winner: "+savedent)
        totseats += 1
    whichdistis += 1

print("Results:")
print(partyseatsdict)

savetofile = input("Calculations Complete! Save to CSV File (Yes or No)? ").lower()
    
if savetofile == "yes":
    with open('electionresults.csv', 'w') as electionresults:
        for sublist in listforprint:
            for entary in sublist:
                electionresults.write(str(entary)+",")
            electionresults.write("\n")
