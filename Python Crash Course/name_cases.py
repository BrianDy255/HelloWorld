name_person = "Brad"
print("Hello, {}.".format(name_person), "Would you like to learn some Python today?".title())

name_person_under = "brad"
name_person_upper = "jenny"
name_person_title = "ssleSlAm"

print(name_person_title.title())
print(name_person_under.lower(), name_person_upper.upper())

print('Albert Einstein once said, \n\t"A person who never made a mistake never tried anything new."')

famous_person = "Marcus Aereulious"
message = "It is not death that a man should fear, but he should fear never beginning to live."

print(famous_person, "once said,\n\t", message)

#stripping
name_strip = "     sssss      "
print(name_strip.lstrip())
print(name_strip.rstrip())
print(name_strip.strip())