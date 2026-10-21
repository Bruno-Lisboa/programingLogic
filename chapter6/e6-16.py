# the exercises 6.16 n' 6.17 were done here
# program 6.20
L = [7, 4, 3, 12, 8]          #1
fim = 5                       #2
while fim > 1:                #3
    trocou = False            #4
    x = 0                     #5
    while x < (fim - 1):      #6
        if L[x] > L[x + 1]:   #7
            trocou = True     #8
            temp = L[x]       #9
            L[x] = L[x + 1]   #10
            L[x + 1] = temp   #11
        x += 1                #12
    if not trocou:            #13
        break                 #14
    fim -= 1                  #15
for e in L:                   
    print(e)
# exercise 6.16 track the program 6.20 if the list was L = [1, 2, 3, 4, 5]
    # the line #7 would never be true because L[x] would always be minor than L[x + 1].
    # so the program would skip the condition L[x] > L[x + 1] and go straight to the line #12
    # where x += 1, so this loop would repeat until x = 4. after that the program would jump to
    # line #13 and the next line would be read because trocou never been True, so the loop would break

# exercise 6.17 track the program 6.20 if the list was L = [3, 3, 1, 5, 4]
    # the condition in line #7 would see that the first and sedcond elements era equal, so
    # the program would jump to the line #12, x is now 1, so repeat the process.
    # now L[x] = 3 and L[x + 1] = 1, so the condition is true and now trocou = True,
    # temp = 3, L[x] = 1 and L[x + 1] = 3. so the list is now L = [3, 1, 3, 5, 4] and x = 2.
    # back to the line #7 the condition would be false because L[x] = 3 and L[x + 1] = 5, so jump to line #12
    # and x is 3 now. the condition is True, so the process happen again. trocou = True, temp = 5, L[x] = 4,
    # L[x + 1] = 5. list: L = [3, 1, 3, 4, 5]. something interesting happens now because x = 4 at this point of the program.
    # so, with the x being 4, the line #6 can't be executed now because x insn't < (fim - 1), so the condition is false,
    # but we are still inside a loop, and next line of the loop is #13 where the variable 'trocou' will be verified.
    # the program didn't jump to the line #4, so the 'trocou' keeps True. that means that the line #14 will be ignored by the program
    # and execute the next line: fim -= 1. now fim = 4 and the main loop repeat going to the #3, and the list will be verified again.
    # at this point I wont explain every detail again because I already understand what is happening in the program and that's the idea
    # of the exercise, but to be fair I will summary the tracking.
    # L = [1, 3, 3, 4, 5], that's how the list will look at the end. 
    # the program will keep verifying until 'trocou' be false the line #14 be executed.
