example = int(input('Enter example number '))

## Example: Review of Tuples
if example == 1:
    ##Tuples may have any type of element in them -
    ## strings, ints, floats, other tuples, other lists
    tupA = (1, 'apple', 6.00)
    tupB= (tupA, 'hot', [4,5])

    print('tuple A is ', tupA, 'with length : ', len(tupA))
    print('tuple B is ', tupB, 'with lenth : ', len(tupB))

    print("\nIndexing Operations")
    print("tupA[0] is ", tupA[0])
    print("tupA[2] is ", tupA[2])
    #print("tupA[3] is ", tupA[3]) #why error?
    print("tupB[0] is ", tupB[0])
    print("tupB[0][1] is ", tupB[0][1])
    print("tupB[-1] is ", tupB[-1])

    print("\nSlicing Operations")
    print("tupA[0:1] is ", tupA[0:1])
    print("tupA[0:100] is ", tupA[0:100])
    print("tupA[0:2] is ", tupA[0:2])
    print("tupA[1:] is ", tupA[1:])
    print("tupA[:] is ", tupA[:])
    print("tupB[-1:-3] is ", tupB[-1:-3])

    ##Iteration through tuples
    print("\nIteration through tupB")
    for item in tupB:
        print(item, "is of type", type(item))

    #this is equivalent to
    print("\nIteration through tupB")
    for i in range(len(tupB)):
        print(tupB[i], "is of type", type(tupB[i]))
