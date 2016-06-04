# Instructor Guide to cyber-dojo.org

To use cyber-dojo.org to set up an exercise for students:

# Step 1: Which unit testing framework?

There are two baselinestarting point assumption for all usage of cyber-dojo.org:

* students will be working in a Test-Driven Development style of programming
* students will use one of the TDD frameworks supported by cyber-dojo.org

For Python, there are two supported frameworks: unittest and py.test, each with its pros and cons.

* For getting started, I recommend the py.test framework. 
* Later on we may (or may not) transition to the unittest framework.  
* Here is [more detail as to the pros/cons](py.test-vs-unittest.md)

* py.test
 - pros: 
  - Easy to understand for beginners.  Less syntax.
  - Does not require use of `class` construct
 - cons: 
  - code written using py.test will not compile utside of cyber-dojo.org without extra install (e.g. `pip install --user py.test`)
  
* unittest: 
 - pros: 
  - standard, built into Python 2.x and 3.x
  - code written using unittest will run directly in IDLE without any extra installs
 - cons:
  - more "syntax" and "cogntive overhead" for beginners
  - in particular, the `class` and `self` keywords are clutter that may get in the way
  



# Step 2: Decide whether you are going to use unittest or py.test as your unit testing framework.

