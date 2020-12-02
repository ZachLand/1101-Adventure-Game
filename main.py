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

def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.05)
    print() # go to new line

def print_slower(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.1)
    print() # go to new line

# game loop
current_room = 'title room'
  # check point loop
while True:
  while True:
      if current_room == 'title room':
          clear()
          print("Welcome to Dog Train")
          name = print('\nPlease enter your name: ')
          name = input()
          clear()

          win = False
          print('\n'+name+ ', you are in a train with your dog.')
          print('Suddenly, everything goes dark as the train passes through a tunnel.')
          print('Once the train exits the tunnel, you are able to see again.')
          print('You see that your beloved dog is no longer next to you.')
          print('\nAs you start looking around, you hear a voice through the intercom.')
          print(
              '"hahaha! You want your dog back? You\'ll have to reach the front of the train first!"'
          )
          print('\n"Good luck!"')
          sleep(5)
          clear()

          current_room = 'opening room'
      # display room contents
      print()
      if current_room == 'opening room':
          clear()
          print('You get up from your current seat and look around.')
          print(
              'There\'s a bunch of luggage thrown about, no one seems to be here...'
          )
          print('You see a door, the path seems straight forward.')
          print('Will you go towards the door? (a/b)')
          print('a. Yes')
          print('b. No')
          door = input('Please select from the options above: ')
          if door == 'a':
              clear()
              print('You go to the door and open it, taking you to the next room.')
          elif door == 'b':
              clear()
              print('You decide not to go towards the door.')
              print('...')
              print(
                  'There is nothing else to do, so you decide to go to the door anyway.'
                )
              print(
                  'You go to the door and open it, taking you to the next room.')


      elif current_room == 'empty room':
          print('The door locks behind you.')
          print('You are in a small empty room.')
          print('There, stands a button in the middle...')
          print('Do you press it?')
          print('a. Yes')
          print('b. No')
          choice = input('Please select from the options above: ')
          if choice == 'a':
              clear()
              print("Congratulations a new door has been opened!")
          elif choice == 'b':
              clear()
              print("You're stuck forever")
              print("Game Over.")
              sleep(3)
              break

      elif current_room == 'coal room':
          print('You entered the coal room.')
          print('The room is extremely dark.')
          print('Theres a torch near the enterence...')
          print('Will you light it?')
          print('a. Yes')
          print('b. No')
          choice = input('Please select from the options above: ')
          if choice == 'a':
              clear()
              print('\nYou are engulfed in flames and have died.')
              print('Game Over.')
              sleep(3)
              break
          elif choice == 'b':
              clear()
              print('\nThe room continues to be extremely dark')

          print('\nYou hear your dog barking from the North.')
          print(
              'You realize you can feel your way towards the exit of the room.')
          print('Which direction will you start feeling your way towards?')
          print('a. North')
          print('b. East')
          print('c. South')
          print('d. West')
          direction = input('Please select from the options above: ')

          if direction == 'a':
              clear()
              print(
                  '\nYou start inching your way to the North, eventually reaching a door.'
              )
              print('You open the door, reaching the next room')
          elif direction == 'b':
              clear()
              print('\nYou start inching your way East.')
              print(
                  'While moving, you notice the floorboards under you have gotten loose.'
              )
              print('Suddenly, a board from under you has given way.')
              print('You fall off the train while it is moving at high speed.')
              print('You die instantly.')
              print('Game Over.')
              sleep(3)
              break
          elif direction == 'c':
              clear()
              print('\nYou start inching your way South.')
              print('You eventually start hearing bats.')
              print('You are swarmed by bats.')
              print('You start panicking and lose your footing.')
              print('You fall and break your neck.')
              print('You have died.')
              print('Game Over.')
              sleep(3)
              break
          elif direction == 'd':
              clear()
              print('\nYou start inching your way West.')
              print(
                  'As you reach out to move your hand to the next place on the wall, you feel something cut you.'
              )
              print(
                  'You think it is nothing as you look at your hand and just see a normal looking cut.'
              )
              print(
                  'However, you start noticing your vision start going a little crazy.'
              )
              print(
                  'The room is filled with bright colors and you start feeling dizzy.'
              )
              print('You lose your balance and fall.')
              print('You start foaming from the mouth.')
              print(
                  'You hear echoes of your dog barking as you close your eyes for the last time.'
              )
              print('You have died.')
              print('Game Over.')
              sleep(3)
              break

      elif current_room == 'fire room':
          print('You enter the room blinded by light.')
          print('There is fire everywhere.')
          print('There\'s fire blocking the way to the door.')
          print('What will you do?')
          print('a. Walk through the fire.')
          print('b. Throw your jacket on top of the fire to suffocate it.')
          print('c. Use your water bottle to pour water on the fire.')
          choice = input('\nPlease select from the options above: ')
          if choice == 'a':
            clear()
            print('\nlol you died.')
            print('Game Over.')
            sleep(3)
            break
          elif choice == 'b':
            clear()
            print('\nYou throw your jacket on top of the fire.')
            print('The fire dies out from lack of oxygen.')
            print('The way is now clear, you make your way to the next room.')
          elif choice == 'c':
            clear()
            print('\nYou throw water on the fire.')
            print('Unfortunately it was an electrical fire.')
            print('The electricity travels up the water, shocking you.')
            print('You feel your heart give out from all the electricity.')
            print('You are dead.')
            print('Game Over.')
            sleep(3)
            break

      elif current_room == 'boss room':
          print("Various doors surround you...")
          print('the sound of dogs barking are behind each door.')
          print('Choose correctly which door to approach.')
          print('Choose carfully...')
          print('a. Door #1')
          print('b. Door #2')
          print('c. Door #3')
          choice = input('Please select from the options above: ')
          if choice == 'a':
              clear()
              print('Snakes begin to surround you.')
              print("The snakes dig their fangs into you and you've died")
              print('Game over.')
              sleep(3)
              break
          elif choice == 'b':
              clear()
              print('You enter a room, The Conductor is sleeping...')
              print('You quietly walk toward the exit..')
              print('The door slings open and you escape')
          elif choice == 'c':
              clear()
              print('Gas rushes through the door. \n The air becomes thick you lose concious')
              print('Game over.')
              sleep(3)
              break

      elif current_room == 'victory room':
          print('\nYou have stepped out of the train and stepped into a meadow.')
          print('bark... bark BARK!')
          print("\nCongradulations, you've found your dog!")
          win = True
          break
      # get user input
      command = input('\nContinue? (yes/no): ').strip()
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
    print("\nWould you like to:\na. Play from beggining\nor\nb. End Game")
    again = input()
    if again == 'a':
      clear()
      current_room = 'title room'
      continue
    elif again == 'b':
      clear()
      print('\nThanks for Playing!')
      print("\nFinal for CSCI-1101-95L-Fall2020")
      print("\nby:")
      print("Henry Olvera\nAlan Lopez\nTyler Landgraf\nEduardo Cruz\nAlyssa Perez")
      break
  else:
    clear()
    again = input("\nWould you like to start over from the last room? (y/n): ")
    try:
      if again == "y":
        continue
      elif again == "n":
        print("\nWould you like to:\na. Play from beggining\nor\nb. End Game")
        again = input()
        if again == 'a':
          clear()
          current_room = 'title room'
          continue
        elif again == 'b':
            clear()
            print('Thanks for playing!')
            print("\nFinal for CSCI-1101-95L-Fall2020")
            print("\nby:")
            print("Henry Olvera\nAlan Lopez\nTyler Landgraf\nEduardo Cruz\nAlyssa Perez")
            break
    except:
      print("Error... quitting game")
  

