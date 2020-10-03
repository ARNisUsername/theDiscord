import discord
from discord.ext import commands
import time
import random
import fileinput
import sys
import matplotlib.pyplot as plt
import seaborn as sns

client = commands.Bot(command_prefix='?')

def getWords(fileStr):
    WordsFile = open(fileStr, 'r')
    WordsWords = [word.rstrip('\n') for word in WordsFile]
    Words = []
    for word in WordsWords:
        if len(word) > 1: Words.append(word)
    return Words

positiveW = getWords('positive.txt')
negativeW = getWords('negative.txt')

def countWords(msg):
    msgList = [word.lower() for word in msg.split(' ')]
    amountP = 0
    amountN = 0
    for word in msgList:
        if word in positiveW:
            amountP += 1
        elif word in negativeW:
            amountN += 1
    if amountP > amountN:
        return 'Thank you very much good boi!'
    elif amountP < amountN:
        return 'U suck loser >:((( screw u!!!'
    else:
        return 'Ok'

def allPossible(string, message):
    newString = string[0].upper() + string[1:]
    if string in message or newString in message:
        return True
    return False


def giveNames():
    listMembers = []
    with open('theGame.txt', 'r') as theFile:
        for line in theFile:
            listMembers.append(line.rstrip('\n'))
    return listMembers

def doTheLol(theNum):
    theString = ''
    for i in range(theNum):
        theString += 'lol\n'
    return theString

def doRun():
    with open('doRespond.txt', 'r') as theFile:
        for line in theFile:
            lineS = line.rstrip('\n')
            return (lineS == "Work")

def writeFile(msgList, theFile):
    file = open(theFile, 'a')
    msgString = ''
    for i in range(len(msgList)):
        msgString += msgList[i]
    file.write(msgString + '\n')

def replaceFile(msgList, theFile):
    file = open(theFile, 'w')
    file.writelines(msgList)

def readFile(theFile):
    outputList = []
    with open(theFile, 'r') as file:
        for line in file:
            outputList.append(line)
    return outputList

def calHappy(taxes, jobs, conditions, stability):
    if (taxes + jobs + conditions + stability)/4 < 50:
        return int((taxes + jobs + conditions + stability)/4.5)
    else:
        return int((taxes + jobs + conditions + stability)/4)

def getPlayers():
    countriesList = readFile('listCountries.txt')
    allInfo = []
    for i in range(len(countriesList)):
        countryId = countriesList[i].split(' ')
        allInfo.append(countryId)
    return allInfo

def getNames(theMention):
    if '667178065117315084' in theMention:
        return 'Arnav'
    elif '719059159949115402' in theMention:
        return 'Kern'
    elif '755960145271586897' in theMention:
        return 'Test'
    elif '629524459119837184' in theMention:
        return 'Ayush'
    else:
        return 'Ansh'

def convertNumStr(theNumber):
    return '{:,.2f}'.format(theNumber)[:-3]

def getFactors(name):
    theFile = readFile('listCountries.txt')
    totalList = []
    for x in range(len(theFile)):
        indiv = theFile[x].split(' ')
        if name == indiv[0]:
            for i in range(1, len(indiv)):
                totalList.append(int(indiv[i]))

    return totalList


def replaceAll(theFile, name, newStr, countNum):
    storedList = readFile(theFile)
    useableList = []
    for i in range(len(storedList)):
        if name in storedList[i]:
            useableList = storedList[i].split(' ')
            useableList[countNum-1] =  newStr
            useableList = ' '.join(useableList)
            storedList[i] = useableList
            break
    replaceFile(storedList, theFile)

def replaceLine(theFile, name, newLine):
     storedList = readFile(theFile)
     useableList = []
     for i in range(len(storedList)):
        if name in storedList[i]:
            storedList[i] = newLine
            break
     replaceFile(storedList, theFile)

def addMoney(name, newMoney):
    theData = readFile('discordData.txt')
    listData = []
    for line in theData:
        if name in line:
            listData = line.split()
    listData.append(newMoney)
    newLine = ' '.join(listData)
    newLine += '\n'
    replaceLine('discordData.txt', name, newLine)



                
#addMoney('Ansh', '150000000')
#replaceAll('listCountries.txt','Arnav1', '120000', 2)

@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def create(ctx):
    print(ctx.message.author.mention)
    theMention = ctx.message.author.mention
    fileList = readFile('listCountries.txt')
    hasBeen = False
    for i in range(len(fileList)):
        if getNames(theMention) in fileList[i]:
            await ctx.send('Oi, you are already in the list. No turning back now')
            hasBeen = True
            break
        
    if hasBeen == False:
        writeFile([getNames(theMention) + ' ' + '100000 ' + '1000000000 ' + '300000000 ' + '50 ' + '50 ' + '50 ' + '50 ' + '50'], 'listCountries.txt')
        await ctx.send(f'Congruatulations, {theMention}, your country has been created!')

@client.command()
async def ratings(ctx, *, message):
    theFile = readFile('listCountries.txt')
    allIn = ['Population: ', 'Reserve: ', 'Earnings per year: ', 'Citizen tax liking: ', 'Citizen liking of job market: ', 'Living Conditions: ', 'Stability: ', 'Happiness: ']
    totalString = ''
    mainFactors = []
    beginAddition = False
    for x in range(len(theFile)):
        indiv = theFile[x].split(' ')
        if message == indiv[0]:
            for i in range(1, len(indiv)):
                whichFactor = allIn[i-1]
                amount = convertNumStr(int(indiv[i]))
                if 'tax' in whichFactor:
                    beginAddition = True
                if 'Happiness' in whichFactor:
                    amount = calHappy(mainFactors[0],mainFactors[1],mainFactors[2],mainFactors[3])
                if beginAddition == True:
                    mainFactors.append(int(amount))
                totalString += '{}{}\n'.format(whichFactor, amount)
    await ctx.send(f'{totalString}')

@client.command()
async def graphMoney(ctx, *, message):
    
@client.command()
@commands.cooldown(1,18000, commands.BucketType.user)
async def taxes(ctx, *, howchange):
    theName = getNames(ctx.message.author.mention)
    changeTaxes = 100 - int(howchange)
    replaceAll('listCountries.txt', theName, str(changeTaxes), 5)
    theGDP = 6000000*int(howchange)
    print(theGDP)
    replaceAll('listCountries.txt', theName, str(theGDP), 4)
    await ctx.send(f'Sucessfully changed your tax rate to {howchange}')

@client.command()
async def give(ctx, *, message):
    name = getNames(ctx.message.author.mention)
    otherName = message.split()[0]
    theAmount = message.split()[1]
    amount = theAmount.split(',')
    theMoney = ''
    for num in amount:
        theMoney += num
    theMoney = int(theMoney)
    moneyName = int(getFactors(name)[1])
    moneyOther = int(getFactors(otherName)[1])
    if moneyName < theMoney:
        await ctx.send('You do not have this money to send!')
    elif theMoney < 0:
        await ctx.send('Nice try lmao')
    else:
        moneyOther += theMoney
        moneyName -= theMoney
        replaceAll('listCountries.txt', name, str(moneyName), 3)
        replaceAll('listCountries.txt', otherName, str(moneyOther), 3)
        strTheMoney = convertNumStr(theMoney)
        await ctx.send(f"Successfully transferred ${strTheMoney} from {name}'s reserve to {otherName}'s reserve!")

@client.command()
@commands.cooldown(1,43200, commands.BucketType.user)
async def collect(ctx):
    theName = getNames(ctx.message.author.mention)
    theGDP = int(getFactors(theName)[2])
    theMoney = int(getFactors(theName)[1])
    strGDP = convertNumStr(theGDP)
    await ctx.send(f'You have collected your daily ${strGDP}!')
    theMoney += theGDP
    replaceAll('listCountries.txt', theName, str(theMoney), 3)
    

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def borders(ctx):
    person = getNames(ctx.message.author.mention)
    MainFeatures = getFactors(person)[3:7]
    thePeople = getFactors(person)[0]
    totalHappiness = 0
    for num in MainFeatures:
        totalHappiness += num
    totalHappiness /= 4
    totalHappiness = int(totalHappiness)
    theRandom = random.randint(totalHappiness*250,30000)
    theRandom -= 20000
    thePeople += theRandom
    await ctx.send(f'Your population has changed by {theRandom}! Your new population size is {thePeople}!')
    replaceAll('listCountries.txt', person, str(thePeople), 2)
    

@client.command()
async def jobs(ctx, *, message):
    newMessage = message.split(',')
    theMoney = ''
    for num in newMessage:
        theMoney += num
    theMoney = int(theMoney)
    loseGain = random.randint(int(theMoney/5000000),100)
    loseGain += int(theMoney/10000000)
    if theMoney < 50000000:
        loseGain = 48
    if loseGain >= 100:
        loss = random.randint(1,30)
        loseGain -= loss
        loseGain = 100
    person = getNames(ctx.message.author.mention)
    currentJobs = int(getFactors(person)[4])
    moneyHas = int(getFactors(person)[1])
    if moneyHas < theMoney:
        await ctx.send('Nah man u too broke')
    else:
        loseGain -= 40
        currentJobs += int(loseGain/100*currentJobs)
        currentJobs = int(currentJobs)
        moneyHas -= theMoney
        if currentJobs > 100:
            currentJobs = 100
        await ctx.send(f'Your job market has had a {loseGain}% change, and is now at {currentJobs}!')
        replaceAll('listCountries.txt',person,str(currentJobs), 6)
        replaceAll('listCountries.txt',person,str(moneyHas), 3)

    
    
    

@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def war(ctx, *, theMessage):
    personAgainst = theMessage
    personFor = getNames(ctx.message.author.mention)
    pAHappy = int(getFactors(personAgainst)[-2])
    pFHappy = int(getFactors(personFor)[-2])
    pAMoney  = int(getFactors(personAgainst)[1])
    pFMoney = int(getFactors(personFor)[1])
    pAPop = int(getFactors(personAgainst)[0])
    pFPop = int(getFactors(personFor)[0])
    soldiersAg = 3000
    soldiersFo = 3000
    originalAg = 3000
    originalFo = 3000
    await ctx.send(f'{personFor} has declared war on {personAgainst}!')
    time.sleep(0.5)
    await ctx.send(f"Before Battle:\n{personFor}'s solders: {soldiersFo}\n{personAgainst}'s soldiers: {soldiersAg}")
    if pAPop > pFPop:
        pAHappy += 5
    else:
        pFHappy += 5
    time.sleep(1)
    onWon = False
    counter = 1
    totalLostFo = 0
    totalLostAg = 0
    while onWon == False:
        solFoLost = int(soldiersFo/float(random.randint(3,10)))
        solAgLost = int(soldiersAg/float(random.randint(3,10)))
        if soldiersFo < soldiersAg:
            solFoLost /= 1.2
        elif soldiersAg < soldiersFo:
            solAgLost /= 1.2
        solFoLost = int(solFoLost)
        solAgLost = int(solAgLost)
        strSolFoLost = convertNumStr(solFoLost)
        strSolAgLost = convertNumStr(solAgLost)
        totalLostFo += solFoLost
        totalLostAg += solAgLost
        soldiersAg -= solAgLost
        soldiersFo -= solFoLost
        strSoldiersAg = convertNumStr(soldiersAg)
        strSoldiersFo = convertNumStr(soldiersFo)
        await ctx.send(f'Battle {counter}:\n{personFor} lost {strSolFoLost} soldiers and is left with {strSoldiersFo}!\n{personAgainst} lost {strSolAgLost} soldiers and is left with {strSoldiersAg}')
        time.sleep(2)
        if soldiersFo <= int(originalFo*0.2):
            moneyRandom = random.randint(5,12)
            moneyGet = int(pFMoney/moneyRandom)
            strMoneyGet = convertNumStr(moneyGet)
            await ctx.send(f'WINNER: {personAgainst}! Congruatulations {personAgainst}, you get {strMoneyGet} dollars from {personFor}!')
            pAMoney += moneyGet
            pFMoney -= moneyGet
            pAHappy += 5
            pFHappy -= 15
            if pFHappy < 10:
                pFHappy = 10
            elif pAHappy < 10:
                pAHappy = 10
            pAPop -= totalLostAg
            pFPop -= totalLostFo
            onWon = True
        elif soldiersAg <= int(originalAg*0.2):
            moneyRandom = random.randint(5,12)
            moneyGet = int(pFMoney/moneyRandom)
            strMoneyGet = convertNumStr(moneyGet)
            await ctx.send(f'WINNER: {personFor}! Congruatulations {personFor}, you get {strMoneyGet} dollars from {personAgainst}!')
            pFMoney += moneyGet
            pAMoney -= moneyGet
            pFHappy += 5
            pAHappy -= 5
            pAPop -= totalLostAg
            pFPop -= totalLostFo
            if pFHappy < 10:
                pFHappy = 10
            elif pAHappy < 10:
                pAHappy = 10
            onWon = True
        counter += 1
    replaceAll('listCountries.txt',personAgainst, str(pAMoney), 3)
    replaceAll('listCountries.txt',personFor, str(pFMoney), 3)
    replaceAll('listCountries.txt',personAgainst, str(pAHappy), 8)
    replaceAll('listCountries.txt',personFor, str(pFHappy), 8)
    replaceAll('listCountries.txt',personAgainst, str(pAPop), 2)
    replaceAll('listCountries.txt',personFor, str(pFPop), 2)
    addMoney(personAgainst, str(pAMoney))
    addMoney(personFor, str(pFMoney))

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def invest(ctx, *, message):
    name = getNames(ctx.message.author.mention)
    moneyPerson = int(getFactors(name)[1])
    if message != 'all':
        newMessage = message.split(',')
        theMoney = ''
        for num in newMessage:
            theMoney += num
        theMoney = int(theMoney)
    else:
        theMoney = moneyPerson
    if theMoney > moneyPerson:
        await ctx.send('U cannot invest money u dont have')
    else:
        moneyMade = random.randint(1,200)
        if theMoney > 2500000000:
            moneyMade = random.randint(50,145)
        newMoney = int(moneyMade/100 * theMoney)
        stringTheMoney = convertNumStr(theMoney)
        stringMoneyMade = convertNumStr(moneyMade)
        stringNewMoney =  convertNumStr(newMoney)
        await ctx.send(f"You invested ${stringTheMoney} into your country's bank corporations! You made {stringMoneyMade}% of that back and got ${stringNewMoney} back!")
        moneyPerson -= theMoney
        moneyPerson += newMoney
        replaceAll('listCountries.txt',name,str(moneyPerson), 3)
    addMoney(name, str(moneyPerson))



@client.command()
async def getid(ctx):
    print(ctx.message.author.mention)
    await ctx.send('Thank you for this information')

@client.command()
async def buy(ctx, *, message):
    name = getNames(ctx.message.author.mention)
    moneyPerson = int(getFactors(name)[1])
    if 'nuke' in message or 'Nuke' in message:
        if moneyPerson < 3000000000:
            await ctx.send('You need 3 billion for this, kiddo')
        else:
            currentNukes = 0
            nukesFile = readFile('nukes.txt')
            print(nukesFile)
            for line in nukesFile:
                if name in line:
                    currentNukes = int(line.split()[1])
            currentNukes += 1
            moneyPerson -= 3000000000
            replaceAll('nukes.txt', name, str(currentNukes) + '\n', 2)
            replaceAll('listCountries.txt',name,str(moneyPerson), 3)
            await ctx.send(f'Succesfully bought one nuke for {name}!')
    addMoney(name, str(moneyPerson))

@client.command()
async def usenuke(ctx, *, message):
    name = getNames(ctx.message.author.mention)
    otherName = message
    theFactors = getFactors(otherName)[:]
    newFactors = [otherName]
    for num in theFactors:
        newNum = int(num / random.randint(6,20))
        newFactors.append(str(newNum))
    nukesFile = readFile('nukes.txt')
    for line in nukesFile:
        if name in line:
             currentNukes = int(line.split()[1])
    if currentNukes < 1:
        await ctx.send('Bru u have no nukes')
    else:
        currentNukes -= 1
        replaceAll('nukes.txt', name, str(currentNukes) + '\n', 2)
        theString = ' '.join(newFactors)
        print(theString)
        replaceLine('listCountries.txt', otherName, theString + '\n')
        await ctx.send(f'OOOOF! {otherName} was NUKED by {name}, resulting in a total CATASTROPHE in the nation of {otherName}!')
    addMoney(otherName, str(newFactors[1]))

@client.command()
async def displaynukes(ctx):
    theFile = readFile('nukes.txt')
    theStr = ''
    for line in theFile:
        newLine = line.rstrip('\n')
        if 'Test' not in line:
            theStr += newLine
            theStr += '\n'
    await ctx.send(f'{theStr}')
            

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def safeinvest(ctx):
    theMoney = random.randint(20,150) * 1000000
    name = getNames(ctx.message.author.mention)
    moneyPerson = int(getFactors(name)[1])
    if random.randint(1,200) == 1:
        await ctx.send('The dictator gods have blessed you with $10 billion dollars! Very lucky boi!')
        theMoney = 10000000000
    strMoney = convertNumStr(theMoney)
    await ctx.send(f'You made ${strMoney} off of your safe invest!')
    moneyPerson += theMoney
    replaceAll('listCountries.txt',name,str(moneyPerson), 3)
    addMoney(name, str(moneyPerson))
    
    

@client.command()
async def dictator(ctx, *, message):

    if doRun() :
        if 'help' in message:
            await ctx.send("I am currently being changed in programming to add a game feauture!")
        elif 'game' not in message:
            response = countWords(message)
            if allPossible('arnav', message):
                await ctx.send('Thanks, Arnav is a great person!')
            elif message == 'SOUUP':
                await ctx.send(file=discord.File('soup_eating.png'))
            elif allPossible('spam', message):
                splitMsg = message.split(' ')
                amountTimes = int(splitMsg[1])
                if amountTimes > 15:
                    await ctx.send('Sorry! 15 is my limits!')
                else:
                    lolStr = doTheLol(amountTimes)
                    await ctx.send(f'{lolStr}')
            elif allPossible('die', message):
                await ctx.send("So... you want to kill me huh? Well, I'm sorry to say, but it will take a little harder than that")
                time.sleep(1)
                await ctx.send("In order to win, you must defeat me in a battle of LUCK DUELS! Do ?hit in order to hit me(100 is max damage). Each of us has 250 health. ")
                with open('didHit.txt', 'w') as theFile:
                    theFile.write('True\n')
                    theFile.write('250\n')
                    theFile.write('250')
            elif allPossible('referee', message):
                mainMention = ctx.message.author.mention
                msgList = message.split(' ')
                otherMention = msgList[1]
                writeFile([str(mainMention) + '\n', '0\n', str(otherMention)], 'playersFighting.txt')
                writeFile(['250\n', '250'], 'punchHealth.txt')
                await ctx.send('Ok! Two players will fight against each other, each with 250 health! Please use the command ?punch to hit each other!')
            elif allPossible('Dora', message):
                messageSplit = message.split(' ')
                lastNum = int(messageSplit[-1])
                if lastNum > 1000000:
                    await ctx.send('Bro do u want this bot to crash?????')
                else:
                    for i in range(lastNum):
                        theFile = readFile('doContinue.txt')
                        if 'continue' not in theFile:
                            break
                        else:
                            await ctx.send(file=discord.File('doraepic.png'))
                            time.sleep(0.01)
            elif allPossible('ping', message):
                message = message.split(' ')
                theMention = message[1]
                theTimes = int(message[-1])
                whoSent = ctx.message.author.mention
                print(whoSent)
                if theMention == '<@!667178065117315084>':
                    await ctx.send('Sorry, I am not allowed to ping that guy')
                elif whoSent == '<@!719059159949115402>':
                    await ctx.send('Sorry loser, who are not allowed to ping anybody since ur untrustworthy lmao')
                else:
                    for i in range(theTimes):
                        await ctx.send(f'{theMention}')
                        theRan = random.randint(1,10)
                        newRan = float(theRan/10)
                        time.sleep(newRan)
                        
            else:
                await ctx.send(f'{response}')
    elif allPossible('reboot', message):
        with open('doRespond.txt', 'w') as theFile:
          theFile.write('Work\n')
        await ctx.send('Succesfully Rebooted')

@client.command()
async def punch(ctx):
    if len(readFile('playersFighting.txt')) > 0:
        theList = readFile('playersFighting.txt')
        print(theList)
        theNum = int(theList[1].rstrip('\n'))
        numFrom = 0
        if theNum % 2 != 0:
            numFrom = 1
        thisMention = str(theList[numFrom].rstrip('\n'))
        otherMention = theList[2]
        In = False
        for line in theList:
            if thisMention in line:
                In = True
        if In == False and theNum % 2 != 0:
            await ctx.send('Bruh u have to be the OG player')
        elif In == True and theNum % 2 == 0:
            await ctx.send('Nooo u have to be other player')
        else:
            healthList = readFile('punchHealth.txt')
            OgHealth = int(healthList[0].rstrip('\n'))
            otherHealth = int(healthList[1])
            randomHit = random.randint(1,100)
            theNum += 1
            if theNum % 2 != 0:
                otherHealth -= randomHit
                await ctx.send(f'Oof! {thisMention} did {randomHit} damage to {otherMention}. {otherMention} now has {otherHealth} health left!')
                writeFile([str(OgHealth) + '\n', str(otherHealth) + '\n', str(theNum)], 'punchHealth.txt')
            else:
                OgHealth -= randomHit
                await ctx.send(f'Oof! {otherMention} did {randomHit} damage to {thisMention}. {thisMention} now has {OgHealth} health left!')
                writeFile([str(OgHealth) + '\n', str(otherHealth) + '\n', str(theNum)], 'punchHealth.txt')
            
    else:
        await ctx.send('What?')

@client.command()
async def hit(ctx):
    if doRun():
        didHit = False
        healthBot = 0
        healthPlayer = 0
        with open('didHit.txt', 'r') as theFile:
            for line in theFile:
                if "True" in line:
                    didHit = True
        if didHit == False:
            await ctx.send('What?')
        else:
            with open('didHit.txt', 'r') as theFile:
                counter = 0
                for line in theFile:
                    if "True" not in line:
                        lineS = line.rstrip('\n')
                        if counter == 0:
                            healthBot = int(lineS)
                        else:
                            healthPlayer = int(lineS)
                        counter += 1
            if healthPlayer > 0:
                theHit = random.randint(1,100)
                healthBot -= theHit
                if healthBot < 0:
                    healthBot = 0
                await ctx.send(f'AGGHH! You did {theHit} damage! I am left with {healthBot} health')
            if healthBot > 0 and healthPlayer > 0:
                theHit = random.randint(20,100)
                healthPlayer -= theHit
                if healthPlayer < 0:
                    healthPlayer = 0
                time.sleep(0.35)
                await ctx.send(f"Heh, now it's my turn. I do {theHit} damage! You are left with {healthPlayer} health")
                if healthPlayer <= 0:
                    time.sleep(0.5)
                    await ctx.send('AHA! It appears that you have failed to kill me, and I have won. Good luck next time, but for now, I prevail!')
                    healthBot += 100
                    open('didHit.txt', 'w').close()
                    with open('didHit.txt', 'w') as theFile:
                        theFile.write('True\n')
                        theFile.write(f'{healthBot}\n')
                        theFile.write(f'{healthPlayer}\n')
            if healthBot > 0 and healthPlayer > 0 and random.randint(1,4) == 1:
                time.sleep(0.1)
                healthRandom = random.randint(1,50)
                if random.randint(1,10) == 1:
                    healthRandom += random.randint(50,100)
                healthBot += healthRandom
                await ctx.send(f"Ooh! It appears I've been lucky to myself! Due to me being a dictator, I have granted myself {healthRandom}, so now I am at {healthBot} health!")
            
            elif healthBot <= 0:
                time.sleep(1.5)
                await ctx.send('...')
                time.sleep(1.5)
                await ctx.send('H-how')
                time.sleep(1.5)
                await ctx.send('...')
                open('didHit.txt', 'w').close()
                open('doRespond.txt', 'w').close()
            if healthBot > 0 and healthPlayer > 0:
                open('didHit.txt', 'w').close()
                with open('didHit.txt', 'w') as theFile:
                    theFile.write('True\n')
                    theFile.write(f'{healthBot}\n')
                    theFile.write(f'{healthPlayer}\n')


        


            
        
    
client.run('NzUzNzI1OTY2OTMyNzcwODk2.X1qYAg.QI3nGzs-7SMRbMOxC5UORophTHU')
