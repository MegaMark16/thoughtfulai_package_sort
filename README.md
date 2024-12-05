# Package Sorter

A simple Python library with a function to sort packages based on their status as STANDARD, SPECIAL, or REJECTED.

## Usage

Code usage:

```
from package_sorter import sort

width = 50		# 50cm wide
height = 100	# 100cm tall
length = 75		# 75cm long
weight = 10		# 10kg

status = sort(width, height, length, weight)
print(status)	# will print "STANDARD" in this example
```

Command line usage:

```
python -m package_sorter.py 50 100 75 10

STANDARD
```

