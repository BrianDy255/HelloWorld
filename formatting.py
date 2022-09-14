for i in range(1,13):
    #print("No. {0} squared is {1} and cubed is {2}".format(i, i **2, i **3))


    ## For proper formatting when using indexing, you can add values after the {}. For example, if you write {0:2}, the 2 indicates how many "spaces" it should be moved over in terms of width. This follows "right side alignment"
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i **2, i **3))



## If you want to force "left side alignment, you use the "<" symbol after the colon
print()
for i in range(1,13):
    print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i **2, i **3))

    ## If you want to force "center alignment, you use the "^" symbol after the colon
print()
for i in range(1,13):
    print("No. {0:<2} squared is {1:^3} and cubed is {2:^4}".format(i, i **2, i **3))

print()

#Precision after decimal point.
print("Pi is approximately {0:12}".format(22/7))   #the 12 is the floating point precision
print("Pi is approximately {0:12f}".format(22/7)) #adding the f produces only a preciosion number of only 6 numbers after the decimal point.
print("Pi is approximately {0:12.50f}".format(22/7)) #the 50f produces 50 floating point numbers precision after the decimal.
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.57f}".format(22/7))  ##pytyhon has difficulty producing precision numbers that are more than 50 digits. As a result you see the "0000" after the last digit.