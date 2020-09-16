import discord
from discord.ext import commands
import time
import random

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



@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def dictator(ctx, *, message):

    if doRun():
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
                        
            else:
                await ctx.send(f'{response}')
    elif allPossible('reboot', message):
        with open('doRespond.txt', 'w') as theFile:
          theFile.write('Work\n')
    
@client.command()
async def game(ctx, *, msg):
    if allPossible('countries', msg):
        await ctx.send('Working on this function!')

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
                time.sleep(1.5)
                await ctx.send(f"Heh, now it's my turn. I do {theHit} damage! You are left with {healthPlayer} health")
                if healthPlayer <= 0:
                    time.sleep(1.5)
                    await ctx.send('AHA! It appears that you have failed to kill me, and I have won. Good luck next time, but for now, I prevail!')
                    open('didHit.txt', 'w').close()
            
            else:
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

        


            
        
    
client.run('NzUzNzI1OTY2OTMyNzcwODk2.X1qYAg.411AoFazGkBFZbqU5pfMfekhGBk')
