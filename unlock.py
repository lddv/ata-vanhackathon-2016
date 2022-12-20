NUMBER_OF_PEOPLE = 11
# NUMBER_OF_PEOPLE = 3
# STEP = 2

def has_even_length(a_list):
    return len(a_list) % 2 == 0

# when removed_last is True, we must start removing from the first position

def process_circle(a_circle):
    my_circle = list(a_circle)
    current_length = len(my_circle)
    removed_last = None
    while current_length > 1:
        if has_even_length(my_circle):
            if removed_last == False:
                my_circle = filter(lambda x: my_circle.index(x) % 2 == 1, my_circle)
                current_length = len(my_circle)
            else:
                my_circle = filter(lambda x: my_circle.index(x) % 2 == 0, my_circle)
                current_length = len(my_circle)
                removed_last = True
        else:
            # odd length
            if removed_last == False:
                last_number = my_circle[-1]
                my_circle = filter(lambda x: my_circle.index(x) % 2 == 1, my_circle)
                current_length = len(my_circle)
                if last_number not in my_circle:
                    removed_last = True
            else:
                my_circle = filter(lambda x: my_circle.index(x) % 2 == 0, my_circle)
                current_length = len(my_circle)
                removed_last = False

        print(my_circle, current_length)
    
    return my_circle[0]


circle = range(1, NUMBER_OF_PEOPLE+1)
print('initial circle: %r' % circle)

process_circle(circle)


