# Instructor Guide to cyber-dojo.org

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

In order to keep things simple while developing a problem, it is suggested that the instructor simply put the instructions in a multi-line string/comment at the top of the file `test_problem.py`.   For example, if the problem were *sum of the first n primes*, the instructor might start a new file called  `test_sum_of_the_first_n_primes.py`as follows:

```Python
'''
Given a positive integer n, compute the sum of the first n primes.

For example:
 when n is 3, return 10 (2+3+5)
 when n is 1, return 2
 when n is 6, return 34 (2+3+5+7+11+13) 

If n is not a positive integer, 
signal the error in some way appropriate to the language.
(e.g. in Python, throw the exception ValueError)
'''
```

Then, when transferring the problem to cyber-dojo.org, the instructor can just copy and paste the text into the `instructions` file in the sample problem.

### Step 2d: Write tests in the selected framework

These instructions assume py.test.  For unittest, consult: [Using unittest with cyber-dojo.org](cyber-dojo-unittest.md)

In the file `test_`_problem_`.py`, write unit tests for your problem. For example, in the file test_sum_of_the_first_n_primes.py, you might write:

```Python

import pytest
from sum_of_first_n_primes import sum_of_first_n_primes

def test_given_1_should_return_2():
  assert sum_of_first_n_primes(1)==2

def test_given_2_should_return_5():
  assert sum_of_first_n_primes(2)==5
  
def test_bad_param_negative():
    with pytest.raises(ValueError):
        x = sum_of_first_n_primes(-4)
        
def test_bad_param_string():
    with pytest.raises(ValueError):
        x = sum_of_first_n_primes("foo")
        
```

### Step 2e: Write stub for function

As you may know, in test driven development, a "stub" is a version of the function that is syntactically correct, but that deliberately returns the wrong answer, so as to *test the test framework*, i.e. ensure that when the implementation is wrong, that the test framework tells us that.

So the next step is to create a a stub for the function we are testing in the file _problem_`.py`.

For example, in the `sum_of_first_n_primes.py`, you may write a stub for your function as follows:

```
# sum_of_first_n_primes.py

def sum_of_first_n_primes(n):
  return "stub"

```

### Step 2f: Write stub for function

To test your program, you can do one of two things:

(1) At command line: run the command `python -m pytest test*.py`
(2) In IDLE: Add the following to your `test_sum_of_n_primes.py` file at the end, and then run that file:
```Python
if __name__ == '__main__':
    pytest.main()
```

At this point, you likely have a version that is suitable as a "starting point" for your students.  Save a version of the files in this state.

If you are developing in a private github repo, making a commit with an appropriate commit message, or even a version tag, is a good solution. Or you can just copy this to a particular subdirectory.

### Step 2g: Try solving the problem

Provided you have saved a separate copy of the "starting point files", it is probably a good idea to try solving the problem outside of cyber-dojo at this point in a *different* directory.   That way, you can make sure that you are satified with the description of the problem, the choices for names of functions, etc.     

Proceed, and then make any needed adjustments to the "starting point files" you saved earlier.

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

![cyber-dojo-enter-practice-session.png](/IMAGES/cyber-dojo-enter-practice-session.png)


