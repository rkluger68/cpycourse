def even(n):
    print('generate even-numbers')
    for i in range(n):
        if i%2 == 0: yield i

def uneven(n):
    print('generate uneven-numbers')
    for i in range(n):
        if i%2 != 0: yield i

def main(n):
    ### 1. Using list compreheions
    # NOTE: Here we just get and print generator object
    #print('<<< 0 >>>')
    #[print(f'even: {number for number in range(n) if number%2 == 0}')]
    #[print(f'uneven: {number for number in range(n) if number%2 != 0}')]

    # NOTE: Here get and print the whole list at once
    print('<<< 1 >>>')
    print([f'even: {number}' for number in range(n) if number%2 == 0])
    print([f'uneven: {number}' for number in range(n) if number%2 != 0])

    # NOTE: Here get the list and print each individual element
    print('<<< 2 >>>')
    [print(f'even: {number}') for number in range(n) if number%2 == 0]
    [print(f'uneven: {number}') for number in range(n) if number%2 != 0]
  
    # NOTE: Here get the list and print each individual element - but as 2 steps
    print('<<< 3 >>>')
    _even = [number for number in range(n) if number%2 == 0]
    for i in _even: print(f'even: {i}')
    _uneven = [number for number in range(n) if number%2 != 0]
    for i in _uneven: print(f'uneven: {i}')


    ### 2. Using generator-functions
    # call even-generator function
    print('<<< 4 >>>')
    for i in even(n):
        print(f'even: {i}')

    # call uneven-generator function
    for i in uneven(n):
        print(f'uneven: {i}')
    

if __name__ == '__main__':
    main(n=10)