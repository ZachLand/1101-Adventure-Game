#intro/setup
from time import sleep

print("Welcome to Dog Train")
print('\nYou are in a train with your dog')
print('Suddenly, everything goes dark as the train passes through a tunnel.')
print('Once the train exits the tunnel, you are able to see again.')
print('You see that your beloved dog is no longer next to you.')
print('As you start looking around, you hear a voice through the intercom.')
print(
    '"hahaha! You want your dog back? You\'ll have to reach the front of the train first!"'
)
print('"Good luck!"')

current_room = 'opening room'

def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.1)
    print() # go to new line



# game loop
while True:
    # display room contents
    print()
    if current_room == 'opening room':
        print('You get up from your current seat and look around.')
        print(
            'There\'s a bunch of luggage thrown about, no one seems to be here...'
        )
        print('You see a door, the path seems straight forward.')
        print('Will you go towards the door?')
        print('a. Yes')
        print('b. No')
        door = input('Please select from the options above: ')
        if door == 'a':
            print('You go to the door and open it, taking you to the next room.')
        elif door == 'b':
            print('You decide not to go towards the door.')
            print('...')
            print(
                'There is nothing else to do, so you decide to go to the door anyway.'
            )
            print(
                'You go to the door and open it, taking you to the next room.')

    elif current_room == 'empty room':
        print('You are in a small empty room.')
        print('There, stands a button in the middle...')
        print('Do you press it?')
        print('a. Yes')
        print('b. No')
        choice = input('Please select from the options above: ')
        if choice == 'a':
            print("Congradulations a new door has been opened!")
        elif choice == 'b':
            print("You're stuck forever")
            print_slow("Game Over.")
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
            print('You are engulfed in flames and have died.')
            print_slow('Game Over.')
            break
        elif choice == 'b':
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
            print(
                '\nYou start inching your way to the North, eventually reaching a door.'
            )
            print('You open the door, reaching the next room')
        elif direction == 'b':
            print('\nYou start inching your way East.')
            print(
                'While moving, you notice the floorboards under you have gotten loose.'
            )
            print('Suddenly, a board from under you has given way.')
            print('You fall off the train while it is moving at high speed.')
            print('You die instantly.')
            print_slow('Game Over.')
            break
        elif direction == 'c':
            print('\nYou start inching your way South.')
            print('You eventually start hearing bats.')
            print('You are swarmed by bats.')
            print('You start panicking and lose your footing.')
            print('You fall and break your neck.')
            print('You have died.')
            print_slow('Game Over.')
            break
        elif direction == 'd':
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
            print_slow('Game Over.')
            break

    elif current_room == 'fire room':
        print('this room is lit')
        print('There is fire everywhere.')
        print('There\'s fire blocking the way to the door.')
        print('What will you do?')
        print('a. Walk through the fire.')
        print('b. Throw your jacket on top of the fire to suffocate it.')
        print('c. Use your water bottle to pour water on the fire.')
        choice = input('Please select from the options above: ')
        if choice == 'a':
          print('lol you died.')
          print_slow('Game Over.')
          break
        elif choice == 'b':
          print('You throw your jacket on top of the fire.')
          print('The fire dies out from lack of oxygen.')
          print('The way is now clear, you make your way to the next room.')
        elif choice == 'c':
          print('You throw water on the fire.')
          print('Unfortunately it was an electrical fire.')
          print('The electricity travels up the water, shocking you.')
          print('You feel your heart give out from all the electricity.')
          print('You are dead.')
          slow_print('Game Over.')
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
            print('Snakes begin to surround you.')
            print("The snakes dig their fangs into you and you've died")
            print_slow('Game over.')
            break
        elif choice == 'b':
            print('The door slings open allowing you to exit')
        elif choice == 'c':
            print('Gas rushes through the door. \n The air becomes thick you lose concious')
            print_slow('Game over.')
            break

    elif current_room == 'victory room':
        print('You have stepped out of the train and stepped into a meadow.')
        print('bark... bark BARK!')
        print_slow("Congradulatios you've found your dog!")
        break
    # get user input
    command = input('\nContinue? (yes/quit): ').strip()
    # movement
    if command.lower() in ('y', 'yes'):
        if current_room == 'opening room':
            current_room = 'empty room'
        elif current_room == 'empty room':
            current_room = 'coal room'
        elif current_room == 'coal room':
            current_room = 'fire room'
        elif current_room == 'fire room':
            current_room = 'boss room'
        elif current_room == 'boss room':
            current_room = 'victory room'
    # quit game
    elif command.lower() in ('q', 'quit'):
        break
    # bad command
    else:
        print("I don't understand that command.")
