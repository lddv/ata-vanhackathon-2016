NUMBER_OF_PEOPLE = 41


def create_circle(number_of_people):
    return range(1, number_of_people + 1)


def has_even_length(a_list):
    return len(a_list) % 2 == 0


# when removed_last is True, we must start removing from the first position


def process_circle(a_circle):
    my_circle = list(a_circle)
    removed_last = None
    while len(my_circle) > 1:
        if has_even_length(my_circle):
            if removed_last == False:
                my_circle = my_circle[1::2]
            else:
                my_circle = my_circle[::2]
                removed_last = True
        else:
            if removed_last == False:
                last_number = my_circle[-1]
                my_circle = my_circle[1::2]
                if last_number not in my_circle:
                    removed_last = True
            else:
                my_circle = my_circle[::2]
                removed_last = False

        print("\n", my_circle, len(my_circle))

    return my_circle[0]


circle = create_circle(NUMBER_OF_PEOPLE)
print("initial circle: ", list(circle), len(circle))

process_circle(circle)
