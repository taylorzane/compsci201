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
