till_num = int(input("Enter the specified number where you want to finish: "))

my_list =[]

for num in range(1, till_num+1):
    # result = ""
    if num % 3 == 0 and num % 5 != 0:
        # result = result + 'FIZZ'
        my_list.append('FIZZ')
    #     if num % 5 == 0:
    #         result = result + 'BUZZ'
    elif num % 5 == 0 and num % 3 != 0:
        # result = result + 'BUZZ'
        my_list.append('BUZZ')

    elif num % 3 == 0 and num % 5 == 0:
        my_list.append('FIZZBUZZ')
    else:
        my_list.append(num)
        # my_list.append(result)

print(my_list)

