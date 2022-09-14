alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.') #the .get provides a default value if no key is present. In this case, since 'points' is not assigned to the original dictionary, if its called,
                                                                # it will produce an error. The get will assign the 'points with a default value that we picked. In this case the "no point value assigned.

print(point_value)