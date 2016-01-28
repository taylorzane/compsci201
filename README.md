# Duke Computer Science 201 - Spring 2016

### Getting Started

Clone the repository, change directory into the repository, and check that a recent version of Python is installed.

```bash
git clone https://github.com/adelyte-chris/compsci201.git
cd compsci201
python --version # Should be 2.7 or greater
```

Run the unit tests.

```bash
python SandwichBarTest.py # Returns one pass and one failure
```

Run the benchmark.

```bash
python SandwichBarTimer.py # Returns the number of seconds to execute 1,000,000 times
```

Check for incomplete tasks.

```bash
grep -R 'TODO' . # Prints a list of instances of 'TODO' in all files
```

Finish those tasks. Run the unit tests again. If all tests pass, run the benchmark.

Stage your changes, commit your changes with a meaningful commit message, and push (publish) them.

```bash
git status # Prints files that have changed
git add -A .
git commit -m "" # Write a meaningful commit message in the quotes
git push
```

### Resources

#### Python
  - [An Informal Introduction to Python](https://docs.python.org/2/tutorial/introduction.html)
  - [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

#### Stack Overflow

Stack Overflow is usually the top Google result for any specific code question. For example:

  - "python list difference" yields [Python, compute list difference](https://stackoverflow.com/questions/6486450/python-compute-list-difference)
  - "python for loop index" yields [Accessing the index in Python for loops](https://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops)

> It is absolutely not cheating to search for specific answers to specific questions, especially when the questions are about syntax or best practices. With syntax questions, you know what you want to do, but you do not know how to express it. With best practices, you do not have the experience to know which approach might be best.
