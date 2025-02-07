"""
Gozde Baran - 101515982
Assignment1

"""

#b Defining variables

gym_member = "Hazel" #string
preferred_weight_kg = 20.5  #float
highest_reps = 25 #int
membership_active = True #boolean

# Print the gym member's details    
print(f"Gym member: {gym_member}")
print(f"Preferred weight: {preferred_weight_kg} kg")
print(f"Highest reps: {highest_reps}")
print(f"Membership active: {membership_active}")

#c Create dictionary for workout stats
workout_stats = {
    "Hazel": (30, 45, 20),  
    "Aybuke": (25, 35, 40),
    "Irem": (40, 50, 30)
} #dictionary ,data type is tuple

#d Calculate total workout minutes and add them to the dictionary
for friend, minutes in workout_stats.items():
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes

#e Create 2D list for workout minutes

workout_list = [list(minutes) for friend, minutes in workout_stats.items() if not friend.endswith("_Total")]

#f Extract and print yoga and running minutes for all friends
for row in workout_list:
    print(f"Yoga: {row[0]} min, Running: {row[1]} min")

#f Extract and print weightlifting minutes for the last two friends
for row in workout_list[-2:]:
    print(f"Weightlifting: {row[2]} min")

#g Check if any friend’s total workout minutes exceed or equal 120
for friend, minutes in workout_stats.items():
    if friend.endswith("_Total") and minutes >= 120:
        name = friend.replace("_Total", "")
        print(f"Great job staying active, {name}!")

#h Allow user input to check workout details for a friend
friend_name = input("Enter a friend's name: ")
if friend_name in workout_stats:
    activities = workout_stats[friend_name]
    total_minutes = workout_stats.get(f"{friend_name}_Total", 0)
    print(f"Workout details for {friend_name}:")
    print(f"Yoga: {activities[0]} min, Running: {activities[1]} min, Weightlifting: {activities[2]} min")
    print(f"Total workout minutes: {total_minutes}")
else:
    print(f"Friend {friend_name} not found in the records.")

#i Find the friend with the highest and lowest total workout minutes
friends_total = {friend: total for friend, total in workout_stats.items() if friend.endswith("_Total")}

highest_friend = ""
lowest_friend = ""
highest_minutes = -1
lowest_minutes = float('inf')

for friend, total in friends_total.items():
    if total > highest_minutes:
        highest_minutes = total
        highest_friend = friend.replace("_Total", "")
    if total < lowest_minutes:
        lowest_minutes = total
        lowest_friend = friend.replace("_Total", "")
lowest_friend = min(friends_total, key=friends_total.get).replace("_Total", "")

print(f"Friend with the highest workout minutes: {highest_friend}")
print(f"Friend with the lowest workout minutes: {lowest_friend}")
