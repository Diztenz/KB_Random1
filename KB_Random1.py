import random

num = input('Choose number of exercises.\n')
exercise = input('Choose number of seconds per exercise.\n')
rest = input('Choose number of seconds per rest.\n')

import time


exerciseList = ['American Swing',
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
sampled_list = random.sample(exerciseList, int(num))
print ('\n'.join(sampled_list))
time.sleep(10)

for x in sampled_list:
    print(x)
    for i in range(int(exercise)):
        print(i)
        time.sleep(1)

    print("Rest") 
    for i in range(int(rest)):
        print(i)
        time.sleep(1) 

print("Congratulations, Workout Complete!")