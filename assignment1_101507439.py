"""
Author: Mina Fahim
Assignment: #1
"""

# Step b: Create 4 variables

# string variable
gym_member = "Alex Alliton"

# float variable
preferred_weight_kg = 20.5

# integer variable
highest_reps = 25

# boolean variable
membership_active = True


# Step c: Create a dictionary named workout_stats

# dictionary with tuple values 3 workout minutes
# each tuple has 3 workout minutes. yoga, running and weightlifting
workout_stats = {
    "Alex": (45, 40, 50),   # Total = 135
    "Mina": (30, 35, 25),  # Total = 90
    "Mobina": (40, 45, 30)     # Total = 115
}

# Step d: Calculate total workout minutes using a loop and add to dictionary

# save original names
friends = list(workout_stats.keys())

# loop calculate total minutes
# add new key with "_Total"
for friend in friends:
    total_minutes = sum(workout_stats[friend])
    workout_stats[friend + "_Total"] = total_minutes

workout_stats


# Step e: Create a 2D nested list called workout_list

# create a 2D list
# each row = one friend
workout_list = []

# extract workout minutes
# append as nested list
for friend in friends:
    workout_list.append([
        workout_stats[friend][0],
        workout_stats[friend][1],
        workout_stats[friend][2]
    ])

workout_list


# Step f: Slice the workout_list

# get yoga and running for all
# slice columns 0 and 1
print("Yoga and Running minutes:")
for row in workout_list:
    print(row[:2])

# get weightlifting for last two
# slice last 2 rows, column 2
print("\nWeightlifting minutes of last two friends :")
for row in workout_list[-2:]:
    print(row[2])


# Step g: Check if any friend's total >= 120

# check total workout time
# and print message if >= 120
for friend in friends:
    if workout_stats[friend + "_Total"] >= 120:
        print("Amazing work,", friend + "! Keep staying active!")



# Step h: User input to look up a friend

# ask user for friend name
# and check if name exists
name = input("Enter a friend's name: ")

# check if the name exists and is not a total key
if name in workout_stats and not name.endswith("_Total"):
    print("Yoga:", workout_stats[name][0])
    print("Running:", workout_stats[name][1])
    print("Weightlifting:", workout_stats[name][2])
    print("Total:", workout_stats[name + "_Total"])
else:
    print("Friend", name, "not found in the records.")


# Step i: Friend with highest and lowest total workout minutes

# create dictionary of totals only
# easier to find max and min
totals = {friend: workout_stats[friend + "_Total"] for friend in friends}

# find highest and lowest
highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print("Friend with the highest total workout minutes:", highest_friend, totals[highest_friend])
print("Friend with the lowest total workout minutes:", lowest_friend, totals[lowest_friend])

