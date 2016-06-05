# UCSD CSE SPIS Instructor Guide to cyber-dojo.org

To use cyber-dojo.org to set up an exercise for students:

## Step 1: Which unit testing framework?

There are two baseline starting point assumption for all usage of cyber-dojo.org:

* students will be working in a Test-Driven Development style of programming
* students will use one of the TDD frameworks supported by cyber-dojo.org

For Python, there are two supported frameworks: unittest and py.test, each with its pros and cons.

* For getting started, I recommend the py.test framework. 
* Later on we may (or may not) transition to the unittest framework.  
* Here is [more detail as to the pros/cons](py.test-vs-unittest.md)

## Step 2: Setting up your problem.  (Outside of cyber-dojo.org)

When first getting used to cyber-dojo.org, it may be best to start by setting up an initial set of test cases and solutions outside of cyber-dojo.org, and then migrating them into cyber-dojo.org.    Here is a guide to doing just that.

### Step 2a: Install py.test

First, if you are using py.test, you need to install py.test so that it is available in your Python environment.

The command is `pip install pytest`

That looks like this:

```
Phillips-Mac-mini:~ pconrad$ pip install --user pytest
Collecting pytest
  Downloading pytest-2.9.2-py2.py3-none-any.whl (162kB)
    100% |████████████████████████████████| 163kB 2.4MB/s 
Requirement already satisfied (use --upgrade to upgrade): py>=1.4.29 in ./Library/Python/2.7/lib/python/site-packages (from pytest)
Installing collected packages: pytest
Successfully installed pytest-2.9.2
Phillips-Mac-mini:~ pconrad$ 
```

### Step 2b: Check whether py.test works in your environment:

Next, at the Python prompt, type "import pytest".  If you get no error, you are in good shape:

```
Phillips-Mac-mini:~ pconrad$ python
Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 12:54:16) 
...
>>> import pytest
>>> 
```
If instead, you get this:

```
>>> import pytest
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named pytest
>>> 
```

then return to step 2a to install py.test

### Step 2c: Write a description of your problem

In cyber-dojo.org, the convention is to have a collection of files such as the following:

| filename | purpose | what student does  |
|----------|---------|--------------------|
| `instructions` | brief description of the problem to be solved | student reads this to understand the problem |
| `test_hiker.py` | tests for solution to problem (assuming problem is called `hiker` | Student writes tests.  Instrucctor might or might not provide a few initial tests to get the student started.
| `hiker.py` |  solution to the problem (assuming problem is called `hiker` | Student writes solutions to get tests to pass. |
| `output` | This file is where the output of the tests can be seen  | Student can review the output of the tests.  This file is typically "read-only". |
| `cyber-dojo.sh` | This file is normally not edited; it contains the command that runs the tests. |  Student normally will ignore this file. It can be examined, though, if a deeper understanding of what is "under the hood" is desired. |

The instructor's first task in designing a problem for cyber-dojo.org is to create the instructions file.

As an example, for the *100 doors* problem, the `instructions` file looks like this:

```
100 doors in a row are all initially closed. You make
100 passes by the doors. The first time through, you
visit every door and toggle the door (if the door is
closed, you open it; if it is open, you close it).
The second time you only visit every 2nd door (door
#2, #4, #6, ...). The third time, every 3rd door
(door #3, #6, #9, ...), etc, until you only visit
the 100th door.

Question: What state are the doors in after the last
pass? Which are open, which are closed?

[Source http://rosettacode.org]
```

In order to keep things simple while developing a problem, it is suggested that the instructor simply put the instructions in a multi-line string/comment at the top of the file `test_problem.py`.   

For example, if the problem were *test whether a number is prime or not* the instructor might start a new file called `test_is_prime.py` with the following instructions in a multi-line string/comment at the top of the file:

```Python
# test_is_prime.py
'''
Write a function is_prime, that given a positive integer n, 
returns True if n is prime, and False if it is not prime.

Examples:

isPrime(1) returns False
isPrime(2) returns True
isPrime(7) returns True
isPrime(9) returns False
isPrime(2251) returns True
isPrime(2253) returns False

As a bonus, if the parameter is not a positive integer, indicate an exception
in some way appropriate to the language.  For example, in Python, throw a ValueError
'''
```

Another example appears here [examples/sum_1st_n_primes/instructions](examples/sum_1st_n_primes/instructions).

Then, when transferring the problem to cyber-dojo.org, the instructor can just copy and paste the text into the `instructions` file in the sample problem.

### Step 2d: Write tests in the selected framework

These instructions assume py.test.  For unittest, consult: [Using unittest with cyber-dojo.org](cyber-dojo-unittest.md)

In the file `test_`_problem_`.py`, after the instructions, write unit tests for your problem. For example, in the file test_is_prime.py, you might write:

```Python
# test_is_prime.py
'''
  ... instructions may temporarily appear here ...
'''
import pytest
from is_prime import isPrime

def test_is_prime_1():
  assert isPrime(1) == False

def test_is_prime_2():
  assert isPrime(2) == True

def test_is_prime_2251():
  assert isPrime(2251) == True
  
def test_is_prime_2253():
  assert isPrime(2253) == False


# Note to students: continue writing additional tests
# following the model above.
```

If you want to show models of testing for exception conditions as well, you can include the following:

```Python
def test_bad_param_negative():
    with pytest.raises(ValueError):
        x = isPrime(-42)
        
def test_bad_param_string():
    with pytest.raises(ValueError):
        x = isPrime("foo")
```

Another example appears here [examples/sum_1st_n_primes/test_sum_1st_n_primes.py](examples/sum_1st_n_primes/test_sum_1st_n_primes.py).

### Step 2e: Write stub for function

As you may know, in test driven development, a "stub" is a version of the function that is syntactically correct, but that deliberately returns the wrong answer, so as to *test the test framework*, i.e. ensure that when the implementation is wrong, that the test framework tells us that.

So the next step is to create a a stub for the function we are testing in the file _problem_`.py`.

For example, in the `is_prime.py`, you may write a stub for your function as follows:

```Python
# is_prime.py

def isPrime(n):
  return "stub"

```

If some part of the problem involves a new piece of syntax, or a trick, and you want to give a hint, you may like to include
that in a comment in the stub.  For example, the following stub shows a hint for raising a `ValueError` when the 
parameter is not an int

```Python
# is_prime.py

def isPrime(n):
  # if not isinstance(n, int):
  #   raise ValueError("n should be an int")
  return "stub"
```

### Step 2f: Test your program (at command line or in IDLE)

At this point, you likely have a version that is suitable as a "starting point" for your students, in that it:
* has clear instructions
* has example tests (that fail)
* has a stub for the function that compiles, but is incorrect.

But to be sure, you should test your program to make sure that the syntax is correct, and the stub fails the tests.

You can do this either at the command line, or in IDLE:

1. At command line: run the command `python -m pytest test*.py`.  This method has the advantage of color output (red for failed tests, green for passed tests).

2. In IDLE: Add the following to your `test_is_prime.py` file at the end, and then run that file:
```Python
if __name__ == '__main__':
    pytest.main("--color=no")
```

The `"--color=no"` is used to surpress the ANSI Escape sequences for color, since these seem not to be supported in IDLE. If you just use `pytest.main()`, you may get the following ugly output:

```
=================================== FAILURES ===================================
[1m[31m_______________________________ test_is_prime_1 ________________________________[0m

[1m    def test_is_prime_1():[0m
[1m>     assert isPrime(1) == False[0m
[1m[31mE     assert 'stub' == False[0m
[1m[31mE      +  where 'stub' = isPrime(1)[0m

test_is_prime.py:27: AssertionError
```

Instead of: 

```
_______________________________ test_is_prime_1 ________________________________

    def test_is_prime_1():
>     assert isPrime(1) == False
E     assert 'stub' == False
E      +  where 'stub' = isPrime(1)

test_is_prime.py:27: AssertionError
```

Once you are satisfied with the results, i.e. you have a clear problem statement, reasonable stub, and good starter tests,  save a version of the files in this state.  This is the version you will set up for the students.

If you are developing in a private github repo, making a commit with an appropriate commit message, or even a version tag, is a good solution. Or you can just copy this to a particular subdirectory.

### Step 2g: Try solving the problem

Provided you have saved a separate copy of the "starting point files", it is may be a good idea to try solving the problem outside of cyber-dojo at this point in a *different* directory.   That way, you can make sure that you are satified with the description of the problem, the choices for names of functions, before setting up the final version in cyber-dojo.org. 
Proceed, and then make any needed adjustments to the "starting point files" you saved earlier.

When all the tests pass, it will look something like this in IDLE:

```
============= RESTART: /Users/pconrad/Documents/test_is_prime.py =============
============================= test session starts ==============================
platform darwin -- Python 2.7.11, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: /Users/pconrad/Documents, inifile: 

collecting 0 items
collecting 6 items
collected 6 items 

test_is_prime.py ......

=========================== 6 passed in 0.66 seconds ===========================
```

You are now ready to set up the problem in cyber-dojo.org

# Step 3: Set up your problem in cyber-dojo.org

## Step 3a: Create practice session

Go to the https://cyber-dojo.org main page, and click to "Create a practice session":

![cyber-dojo-click-create-a-practice-session.png](/IMAGES/cyber-dojo-click-create-a-practice-session.png)

## Step 3b: Select language and test framework

Select Python and py.test and click next and shown below:

![cyber-dojo-select-Python-py.test-next.png](/IMAGES/cyber-dojo-select-Python-py.test-next.png)

## Step 3c: Select an exercise (any exercise)

The next step offers a series of exercises.  It doesn't really matter which one you select, since the only difference among them is
the initial contents of the instructinos file, which you are going to over write anyway.  

The default is `verbal`, in which the instructions basically say "your instructor will tell you what to do".   This is also a way to use cyber dojo "on the fly" without having done any set up in advance (provided your students already understand the basics of the environment, and/or how to write Python functions and test cases.)    Just select `verbal` or for that matter, any of the other problems, and then click next, as shown below:

![cyber-dojo-org-create-select-verbal-exercise.png](/IMAGES/cyber-dojo-org-create-select-verbal-exercise.png)

## Step 3d: Record the hex id of your exercise

At the next step, you will be given a hexadecimal number that is the id of your exercise, as shown below. **You should record this number**. It is difficult (and sometimes impossible) to retrieve this number later if you misplace it.  You'll just have to start over and create a new exercise.   *After you click "next", stay in the same browser window for the next step*.

![cyber-dojo-your-new-id-is-260CD9.png](/IMAGES/cyber-dojo-your-new-id-is-260CD9.png)

## Step 3e: In same browser, click "enter a practice session".

In the same browser where you did step 3d, click **enter a practice session* as shown below.  This will keep you in the context of the same exercise you are in the process of creating.

![cyber-dojo-enter-a-practice-session.png](/IMAGES/cyber-dojo-enter-a-practice-session.png)


TODO: Continue with examples of pasting in the code, then clicking on the icon for the animal avatar, then clicking on "create a practice session from gorilla nn" where nn is the number of the iteration of the tests...
 
