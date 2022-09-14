#dictionaries are defined by the curly braces {}. Uses key values
alien_0 = {'color': 'green', 'points' :5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#adding to a dictionary
alien_0['x_position'] = 0
alien_0['y-position'] = 25
print(alien_0)

#buildling an empty dictionary

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#modifying a dictionary
print(f"The current alien ship color is {alien_0['color']}")

alien_0['color'] = 'yellow'

print(f"The new color for the alien ship is {alien_0['color']}")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'
           }
print(f"Original position: {alien_0['x_position']}")

#move the alien to the right
#determine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

print("")

#the new position is the old position plus the new position
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"The new position is {alien_0['x_position']}")

print("--" * 20)
print("")

#deleting a dictionary or key value pair
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

print("")
print("--" * 20)
#A list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("--" * 20)
############
#Make an empty list for storing aliens
aliens = []

#Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', "points": 5, 'speed': 'slow'}
    aliens.append(new_alien)

#how to for example change the color of the alien after a series of events
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = "medium"
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed']  = 'fast'

#show the first 5 aliens
for alien in aliens[0:5]:
    print(alien)

#Show how many aliens have been created
print(f"The total number of aliens:", {len(aliens)})

