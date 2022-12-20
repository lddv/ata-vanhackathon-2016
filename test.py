from unlock import process_circle

def test_given_circle_with_2_result_should_be_1():
	number_of_people = 2
	assert process_circle(range(1, number_of_people+1)) == 1

def test_given_circle_with_3_result_should_be_3():
	number_of_people = 3
	assert process_circle(range(1, number_of_people+1)) == 3

def test_given_circle_with_4_result_should_be_1():
	number_of_people = 4
	assert process_circle(range(1, number_of_people+1)) == 1

def test_given_circle_with_5_result_should_be_3():
	number_of_people = 5
	assert process_circle(range(1, number_of_people+1)) == 3

def test_given_circle_with_6_result_should_be_5():
	number_of_people = 6
	assert process_circle(range(1, number_of_people+1)) == 5

def test_given_circle_with_7_result_should_be_7():
	number_of_people = 7
	assert process_circle(range(1, number_of_people+1)) == 7

def test_given_circle_with_8_result_should_be_1():
	number_of_people = 8
	assert process_circle(range(1, number_of_people+1)) == 1

def test_given_circle_with_9_result_should_be_3():
	number_of_people = 9
	assert process_circle(range(1, number_of_people+1)) == 3

def test_given_circle_with_10_result_should_be_5():
	number_of_people = 10
	assert process_circle(range(1, number_of_people+1)) == 5

def test_given_circle_with_11_result_should_be_7():
	number_of_people = 11
	assert process_circle(range(1, number_of_people+1)) == 7

def test_given_circle_with_12_result_should_be_9():
	number_of_people = 12
	assert process_circle(range(1, number_of_people+1)) == 9

def test_given_circle_with_13_result_should_be_11():
	number_of_people = 13
	assert process_circle(range(1, number_of_people+1)) == 11

def test_given_circle_with_14_result_should_be_13():
	number_of_people = 14
	assert process_circle(range(1, number_of_people+1)) == 13

def test_given_circle_with_15_result_should_be_15():
	number_of_people = 15
	assert process_circle(range(1, number_of_people+1)) == 15

def test_given_circle_with_41_result_should_be_19():
	number_of_people = 41
	assert process_circle(range(1, number_of_people+1)) == 19
