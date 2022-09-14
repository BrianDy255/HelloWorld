### Create a program to using a dictionary to allow a person to input a string that can provide information for muscles of the body ###
### Separate into body parts such as the head, torso, back, arms, legs. From there, can go further in and list the parts of the muscles ###
### Eventually can also include categories such as "flexors" of the body "extensors", "rotators". ###
### Eventually add innervations and origin and insertions
### Add muscle functions
### eventually add exercises to help strengthen those muscles
from art import logo
print(logo)

#muscles of the upper arm
upper_arm_muscles = ['biceps brachii', 'brachialis', 'coracobrachialis', 'triceps brachii']

#muscles of the forearm
superficial_forearm_muslces = ['flexor carpi ulnaris', 'palmaris longus', 'flexor carpi radialis',
                               'flexor digitorum superficialis','pronator teres']

print("Welcome to the Muscle Information App. Pick a part of the body to find the "
      "muscles associated with that body part.")

def parts_of_the_body():
    parts_of_the_body = ["head", 'torso', 'arms', 'legs', 'foot']

def muscles_of_the_arm():
    upper_arm_muscles = ['biceps brachii', 'brachialis', 'coracobrachialis',
                         'triceps brachii']
    for muscle in upper_arm_muscles:
        print(f'\t {muscle}')
    origins = input("Enter a muscle to learn about the origins and insertions.: ")
muscles_of_the_arm()