# multiple variables: middle, start, end and step
# recursion or while loop
# increase the steps each time a split is done
# conditions to track target position

# a function that takes a list and a target parameter
def binary_search(lst, element):
    middle = 0
    start = 0
    end = len(lst)
    steps = 0

    while start <= end:
        print(f'Step {steps + 1} : {str(lst[start:end + 1])}')

        steps += 1
        middle = (start + end) // 2

        if element == lst[middle]:
            return middle
        if element < lst[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return - 1

my_list = list(map(int, input('Enter your list of numbers, each separated by a single space: ').split()))
target = int(input('Enter your target number: '))
binary_search(my_list, target)
