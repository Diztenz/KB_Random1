import random

print('Choose number of exercises.')
num = input()

input = int

import time

rounds = input('Enter the number of intervals: ')
workout = input('Enter the time in seconds exercise: ')
rest = input('Enter the time in seconds to rest: ')

excerciseList = ['American Swing',
'Bicep Swings',
'Bob and Weave',
'Bottoms Up Clean'
'Bottoms Up Press',
'Bottom-Up Squat',
'Bridge Leg Spreaders',
'Catcher\'s Squat and Press',
'Clean, Squat and Press',
'Clean',
'Clean and Press',
'Clean and Push Press',
'Clean Ups',
'Curls',
'Deck Squat',
'Double Lunge',
'Farmers Carry',
'Figure 8\'s',
'Goblet Squat',
'Good Morning', 
'Half Get-ups',
'Half Kneeling Press',
'Halo', 
'Hamstring Curls',
'High Pulls',
'Hip Thrust',
'Lateral Swing (Side Swing)',
'Lunge and Press',
'Lunge with Rotation',
'Mason Twist',
'Monkey Grip Pushups',
'One Arm Around',
'One Legged Clean',
'Overhead Press',
'Overhead Reverse Lunge',
'Overhead Squat',
'Overhead Walking Lunge',
'Overhead Warm Up',
'Over the Head',
'Over the Shoulder'
'Pistol Squat',
'Push Press',
'Racked Reverse Lunge',
'Regular Row',
'Renegade Row',
'Side Bends',
'Side Grip Pushups',
'Side Lunge',
'Side Lunge and Clean',
'Side Stepping Swing',
'Single Arm Deadlift', 
'Single Handed Swing', 
'Single Leg Deadlift', 
'Sit and Press',
'Situps',
'Skull Crushers',
'Slingshot (Kettlebell Around the World)', 
'Snatch',
'Squat',
'Static Lunge and Press',
'Straight Arm Sit',
'Suitcase Row Exercise',
'Swing Changing Hands',
'Tactical Lunge',
'Tall Kneeling Press',
'Thruster (Squat and Press)',
'Tricep Extensions'
'Turkish Get Up',
'Turkish Press',
'Two Handed Squat and Press',
'Two Hand Swing', 
'Waiter\'s Squat',
'Windmill',
'Wood Choppers']


print("Your " + (num) + " exercises are...")
sampled_list = random.sample(excerciseList, input(num))
print ('\n'.join(sampled_list))



def countdown(count):
    time_left = count
    for i in range(count):
        print(str(time_left) + "...")
        time.sleep(1)
        time_left -= 1

for i in range(int(rounds)):
    print("Round " + str(i + 1) + ". Go!")
    time_left = int(workout)
    countdown(time_left)

    print("Rest!")
    time_left = int(rest)
    countdown(time_left)

print("Done!")
