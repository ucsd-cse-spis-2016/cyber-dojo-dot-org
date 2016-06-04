For Python, cyber-dojo.org supports two test frameworks: unittest and py.test, each with its pros and cons.

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
  
