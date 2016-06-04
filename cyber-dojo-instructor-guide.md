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

