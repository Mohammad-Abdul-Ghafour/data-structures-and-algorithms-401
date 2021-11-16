from python.stackQueueBrackets.stack_queue_brackets import stack_queue_brackets
import pytest

def test_stack_queue_brackets_1(brac_str):
    actual= stack_queue_brackets(brac_str[0])
    expected= True
    assert actual==expected

def test_stack_queue_brackets_2(brac_str):
    actual= stack_queue_brackets(brac_str[1])
    expected= True
    assert actual==expected

def test_stack_queue_brackets_3(brac_str):
    actual= stack_queue_brackets(brac_str[2])
    expected= True
    assert actual==expected

def test_stack_queue_brackets_4(brac_str):
    actual= stack_queue_brackets(brac_str[3])
    expected= True
    assert actual==expected

def test_stack_queue_brackets_5(brac_str):
    actual= stack_queue_brackets(brac_str[4])
    expected= True
    assert actual==expected

def test_stack_queue_brackets_6(brac_str):
    actual= stack_queue_brackets(brac_str[5])
    expected= False
    assert actual==expected

def test_stack_queue_brackets_7(brac_str):
    actual= stack_queue_brackets(brac_str[6])
    expected= False
    assert actual==expected

def test_stack_queue_brackets_8(brac_str):
    actual= stack_queue_brackets(brac_str[7])
    expected= False
    assert actual==expected

@pytest.fixture
def brac_str():
    brac_str = ['{}','{}(){}','()[[Extra Characters]]','(){}[[]]','{}{Code}[Fellows](())','[({}]','(](','{(})']
    return brac_str