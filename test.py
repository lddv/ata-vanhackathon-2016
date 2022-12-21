from unlock import process_circle, create_circle

def test_given_circle_with_2_result_should_be_1():
	assert process_circle(create_circle(2)) == 1

def test_given_circle_with_3_result_should_be_3():
	assert process_circle(create_circle(3)) == 3

def test_given_circle_with_4_result_should_be_1():
	assert process_circle(create_circle(4)) == 1

def test_given_circle_with_5_result_should_be_3():
	assert process_circle(create_circle(5)) == 3

def test_given_circle_with_6_result_should_be_5():
	assert process_circle(create_circle(6)) == 5

def test_given_circle_with_7_result_should_be_7():
	assert process_circle(create_circle(7)) == 7

def test_given_circle_with_8_result_should_be_1():
	assert process_circle(create_circle(8)) == 1

def test_given_circle_with_9_result_should_be_3():
	assert process_circle(create_circle(9)) == 3

def test_given_circle_with_10_result_should_be_5():
	assert process_circle(create_circle(10)) == 5

def test_given_circle_with_11_result_should_be_7():
	assert process_circle(create_circle(11)) == 7

def test_given_circle_with_12_result_should_be_9():
	assert process_circle(create_circle(12)) == 9

def test_given_circle_with_13_result_should_be_11():
	assert process_circle(create_circle(13)) == 11

def test_given_circle_with_14_result_should_be_13():
	assert process_circle(create_circle(14)) == 13

def test_given_circle_with_15_result_should_be_15():
	assert process_circle(create_circle(15)) == 15

def test_given_circle_with_41_result_should_be_19():
	assert process_circle(create_circle(41)) == 19
