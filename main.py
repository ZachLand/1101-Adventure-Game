#intro/setup
from time import sleep
from os import system, name 

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear') 

# function for printing slow for more game-like
def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.05)
    print() # go to new line

# function for printing slower for more dramatic texts
def print_slower(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.1)
    print() # go to new line

# input validation for A/B selections
def getChoiceAB():
    while True:
        while True:
            try:
                choice = str(input())
                break
            except:
                print('ERROR: Please enter valid input option: ')
        if choice.lower() == 'a':
            choice = 'a'
            break
        elif choice.lower() == 'b':
            choice = 'b'
            break
        else:
            print('ERROR: Please enter valid input option: ')
            continue
    return choice

# input validation for A/B/C selections
def getChoiceABC():
    while True:
        while True:
            try:
                choice = str(input())
                break
            except:
                print('ERROR: Please enter valid input option: ')
        if choice.lower() == 'a':
            choice = 'a'
            break
        elif choice.lower() == 'b':
            choice = 'b'
            break
        elif choice.lower() == 'c':
            choice = 'c'
            break
        else:
            print('ERROR: Please enter valid input option: ')
            continue
    return choice

# input validation for A/B/C/D selections
def getChoiceABCD():
    while True:
        while True:
            try:
                choice = str(input())
                break
            except:
                print('ERROR: Please enter valid input option: ')
        if choice.lower() == 'a':
            choice = 'a'
            break
        elif choice.lower() == 'b':
            choice = 'b'
            break
        elif choice.lower() == 'c':
            choice = 'c'
            break
        elif choice.lower() == 'd':
            choice = 'd'
            break
        else:
            print('ERROR: Please enter valid input option: ')
            continue
    return choice

# input validation for Y/N selections
def getChoiceYN():
    while True:
        while True:
            try:
                choice = str(input())
                break
            except:
                print('ERROR: Please enter valid input option: ')
        if choice.lower() == 'y':
            choice = 'y'
            break
        elif choice.lower() == 'yes':
            choice = 'y'
            break
        elif choice.lower() == 'n':
            choice = 'n'
            break
        elif choice.lower() == 'no':
            choice = 'n'
            break
        else:
            print('ERROR: Please enter valid input option: ')
            continue
    return choice

# game loop
current_room = 'title room'
  # check point loop
while True:
  while True:
      if current_room == 'title room':
          clear()
          print_slow("Welcome to Dog Train")
          print_slow('\nPlease enter your name: ')
          name = input()
          clear()

          win = False
          print_slow('\n'+name+ ', you are in a train with your dog.')
          print_slow('Suddenly, everything goes dark as the train passes through a tunnel.')
          print_slow('Once the train exits the tunnel, you are able to see again.')
          print_slow('You see that your beloved dog is no longer next to you.')
          print_slow('\nAs you start looking around, you hear a voice through the intercom.')
          print_slow(
              '"hahaha! You want your dog back? You\'ll have to reach the front of the train first!"'
          )
          print_slower('\n"Good luck, '+name+ '!"')
          sleep(5) #pauses screen for 5 seconds
          clear() #clears screen

          current_room = 'opening room'
      # display room contents
      print()
      if current_room == 'opening room':
          clear()
          print_slow('You get up from your current seat and look around.')
          print_slow(
              'There\'s a bunch of luggage thrown about, no one seems to be here...'
          )
          print_slow('You see a door, the path seems straight forward.')
          print_slow('Will you go towards the door? (a/b)')
          print_slow('a. Yes')
          print_slow('b. No')
          print_slow('Please select from the options above: ')
          door = getChoiceAB()
          if door == 'a':
              clear()
              print_slow('You go to the door and open it, taking you to the next room.')
          elif door == 'b':
              clear()
              print_slow('You decide not to go towards the door.')
              print_slower('...')
              print_slow(
                  'There is nothing else to do, so you decide to go to the door anyway.'
                )
              print_slow(
                  'You go to the door and open it, taking you to the next room.')


      elif current_room == 'empty room':
          print_slow('The door locks behind you.')
          print_slow('You are in a small empty room.')
          print_slow('There, stands a button in the middle...')
          print_slow('Do you press it?')
          print_slow('a. Yes')
          print_slow('b. No')
          print_slow('Please select from the options above: ')
          choice = getChoiceAB()
          if choice == 'a':
              clear()
              print_slow("Congratulations a new door has been opened!")
          elif choice == 'b':
              clear()
              print_slow("You're stuck forever "+name+ ".")
              print_slower("Game Over.")
              sleep(3)
              break

      elif current_room == 'coal room':
          print_slow('You entered the coal room.')
          print_slow('The room is extremely dark.')
          print_slow('Theres a torch near the enterence...')
          print_slow('Will you light it?')
          print_slow('a. Yes')
          print_slow('b. No')
          print_slow('Please select from the options above: ')
          choice = getChoiceAB()
          if choice == 'a':
              clear()
              print_slow('\n'+name+ '... You are engulfed in flames and have died.')
              print_slower('Game Over.')
              sleep(3)
              break
          elif choice == 'b':
              clear()
              print_slow('\nThe room continues to be extremely dark')

          print_slow('\nYou hear your dog barking from the North.')
          print_slow(
              'You realize you can feel your way towards the exit of the room.')
          print_slow('Which direction will you start feeling your way towards?')
          print_slow('a. North')
          print_slow('b. East')
          print_slow('c. South')
          print_slow('d. West')
          print_slow('Please select from the options above: ')
          direction = getChoiceABCD()

          if direction == 'a':
              clear()
              print_slow(
                  '\nYou start inching your way to the North, eventually reaching a door.'
              )
              print_slow('You open the door, reaching the next room')
          elif direction == 'b':
              clear()
              print_slow('\nYou start inching your way East.')
              print_slow(
                  'While moving, you notice the floorboards under you have gotten loose.'
              )
              print_slow('Suddenly, a board from under you has given way.')
              print_slow('You fall off the train while it is moving at high speed.')
              print_slow('You die instantly.')
              print_slower('Game Over, '+name+ '.')
              sleep(3)
              break
          elif direction == 'c':
              clear()
              print_slow('\nYou start inching your way South.')
              print_slow('You eventually start hearing bats.')
              print_slow('You are swarmed by bats.')
              print_slow('You start panicking and lose your footing.')
              print_slow('You fall and break your neck.')
              print_slow('You have died.')
              print_slower('Game Over, '+name+ '.')
              sleep(5)
              break
          elif direction == 'd':
              clear()
              print_slow('\nYou start inching your way West.')
              print_slow(
                  'As you reach out to move your hand to the next place on the wall, you feel something cut you.'
              )
              print_slow(
                  'You think it is nothing as you look at your hand and just see a normal looking cut.'
              )
              print_slow(
                  'However, you start noticing your vision start going a little crazy.'
              )
              print_slow(
                  'The room is filled with bright colors and you start feeling dizzy.'
              )
              print_slow('You lose your balance and fall.')
              print_slow('You start foaming from the mouth.')
              print_slow(
                  'You hear echoes of your dog barking as you close your eyes for the last time.'
              )
              print_slow(name +' died.')
              print_slower('Game Over.')
              sleep(6)
              break

      elif current_room == 'fire room':
          print_slow('You enter the room blinded by light.')
          print_slow('There is fire everywhere.')
          print_slow('There\'s fire blocking the way to the door.')
          print_slow('What will you do?')
          print_slow('a. Walk through the fire.')
          print_slow('b. Throw your jacket on top of the fire to suffocate it.')
          print_slow('c. Use your water bottle to pour water on the fire.')
          print_slow('Please select from the options above: ')
          choice = getChoiceABC()
          if choice == 'a':
            clear()
            print_slow('\nlol you died, '+name+ '.')
            print_slower('Game Over.')
            sleep(3)
            break
          elif choice == 'b':
            clear()
            print_slow('\nYou throw your jacket on top of the fire.')
            print_slow('The fire dies out from lack of oxygen.')
            print_slow('The way is now clear, you make your way to the next room.')
          elif choice == 'c':
            clear()
            print_slow('\nYou throw water on the fire.')
            print_slow('Unfortunately it was an electrical fire.')
            print_slow('The electricity travels up the water, shocking you.')
            print_slow('You feel your heart give out from all the electricity.')
            print_slow('You are dead, '+name+ '.')
            print_slower('Game Over.')
            sleep(3)
            break

      elif current_room == 'boss room':
          print_slow("Various doors surround you...")
          print_slow('the sound of dogs barking are behind each door.')
          print_slow('Choose correctly which door to approach.')
          print_slow('Choose carfully...')
          print_slow('a. Door #1')
          print_slow('b. Door #2')
          print_slow('c. Door #3')
          print_slow('Please select from the options above: ')
          choice = getChoiceABC()
          if choice == 'a':
              clear()
              print_slow('Snakes begin to surround you.')
              print_slow("The snakes dig their fangs into you and you've died")
              print_slower('Game over, '+name+ '.')
              sleep(3)
              break
          elif choice == 'b':
              clear()
              print_slow('You enter a room, The Conductor is sleeping...')
              print_slow('You quietly walk toward the exit..')
              print_slow('The door slings open and you escape')
          elif choice == 'c':
              clear()
              print_slow('Gas rushes through the door. \n The air becomes thick you lose concious')
              print_slower('Game over, '+name+ '.')
              sleep(3)
              break

      elif current_room == 'victory room':
          print_slow('\nYou have stepped out of the train and stepped into a meadow.')
          print_slow('bark... bark BARK!')
          print_slow("\nCongradulations, you've found your dog!")
          win = True
          break
      # get user input
      print_slow('\nContinue? (yes/no): ')
      command = getChoiceYN()
      # movement
      if command.lower() in ('y', 'yes'):
          if current_room == 'title room':
              current_room = 'opening room'
              clear()
          elif current_room == 'opening room':
              current_room = 'empty room'
              clear()
          elif current_room == 'empty room':
              current_room = 'coal room'
              clear()
          elif current_room == 'coal room':
              current_room = 'fire room'
              clear()
          elif current_room == 'fire room':
              current_room = 'boss room'
              clear()
          elif current_room == 'boss room':
              current_room = 'victory room'
              clear()
          elif current_room == 'victory room':
              current_room = 'title room'
              clear()
      # quit game
      elif command.lower() in ('n', 'no'):
          clear()
          break
      # bad command
      else:
          print_slow("I don't understand that command.")
          sleep(1)
          clear()
  
  
  if win:
    print_slow("\nWould you like to:\na. Play from beggining\nor\nb. End Game")
    again = getChoiceAB()
    if again == 'a':
      clear()
      current_room = 'title room'
      continue
    elif again == 'b':
      clear()
      print_slower('\nThanks for Playing, '+name+ '!')
      print("\nFinal for CSCI-1101-95L-Fall2020")
      print("\nby:")
      print("Henry Olvera\nAlan Lopez\nTyler Landgraf\nEduardo Cruz\nAlyssa Perez")
      break
  else:
    clear()
    print_slow("\nWould you like to start over from the last room? (y/n): ")
    again = getChoiceYN()
    try:
      if again == "y":
        clear()
        continue
      elif again == "n":
        print_slow("\nWould you like to:\na. Play from beggining\nor\nb. End Game")
        again = getChoiceAB()
        if again == 'a':
          clear()
          current_room = 'title room'
          continue
        elif again == 'b':
            clear()
            print_slower('Thanks for playing, '+name+ '!')
            print("\nFinal for CSCI-1101-95L-Fall2020")
            print("\nby:")
            print("Henry Olvera\nAlan Lopez\nTyler Landgraf\nEduardo Cruz\nAlyssa Perez")
            break
    except:
      print_slow("Error... quitting game")