import pytest

temperature = 10
def print_temperature():
    print(temperature)
    
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'


def subtract(a, b):
    return a - b

def test_subtract():
    assert subtract(2, 3) == -1

## Excrcise 4, write test scripts
# All answers can be found: https://coderefinery.github.io/testing/test-design/
#1
def factorial(n):
    """
    Computes the factorial of n.
    """
    if n < 0:
        raise ValueError('received negative input')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test_factorial():
    assert factorial(0) == 1
    assert factorial(4) == 24
    with pytest.raises(ValueError):
        assert factorial(-1)
    # Important to test multiple situations
    
        

# 2
def count_word_occurrence_in_string(text, word):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function returns 2
    """
    words = text.split()
    return words.count(word)

def test_count_word_occurrence_in_string():
    assert count_word_occurrence_in_string("Hello world Hello", "Hello") == 2
    # Think of 'edge cases'.

# 3
def count_word_occurrence_in_file(file_name, word):
    """
    Counts how often word appears in file file_name.
    Example: if file contains "one two one two three four"
             and word is "one", then this function returns 2
    """
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()
            count += words.count(word)
    return count

def test_def_count_word_occurrence_in_file(tmpdir):
    file_name = tmpdir.join("test_file.txt")
    file_name.write("hallo world hello")
    assert count_word_occurrence_in_file(r"tmpdir/test_file.txt", "Hello") == 5
    

# 4
def check_reactor_temperature(temperature_celsius):
    """
    Checks whether temperature is above max_temperature
    and returns a status.
    """
    from reactor import max_temperature
    if temperature_celsius > max_temperature:
        status = 1
    else:
        status = 0
    return status

#def test_check_reactor_temperature():
#    assert check_reactor_temperature(1) == 0
#    assert check_reactor_temperature(101) == 1

# 5
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
    def go_for_a_walk(self):  # <-- how would you test this function?
        self.hunger += 1
        
#def test_go_for_a_walk(self):
#    P = Pet("Sven")
#    P.go_for_a_walk()
#    assert(self.hunger) == 1