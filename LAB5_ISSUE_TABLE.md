# Lab 5 — Static Code Analysis

**Student:** SHASHANK B JAIN
**SRN:** PES1UG24CS620
**Project:** Recruitment Tracker

## Issues identified and fixes

| No. | Original finding | Tool | Fix applied |
|---|---|---|---|
| 1 | SQL query constructed using an f-string | Bandit B608 | Replaced interpolated values with parameterized SQL. |
| 2 | Unsafe use of eval() | Pylint W0123, Bandit B307 | Replaced expression evaluation with a validated integer salary limit. |
| 3 | Broad exception caught and silently ignored | Pylint W0718, Bandit B110 | Removed silent exception suppression and allowed failures to be handled explicitly. |
| 4 | Missing module and function docstrings | Pylint C0114, C0116 | Added documentation to the module and functions. |
| 5 | Function names did not follow snake_case | Pylint C0103 | Renamed functions and updated their call sites. |
| 6 | Long lines, trailing whitespace, and inconsistent spacing | Pylint and Flake8 | Reformatted the code and removed trailing whitespace. |
| 7 | File opened without explicit encoding or managed cleanup | Pylint W1514, R1732 | Used a context manager and UTF-8 encoding for CSV output. |
| 8 | Unused local variable | Pylint W0612, Flake8 F841 | Removed the unused variable. |

## Final verification

- Pylint: 10.00/10
- Bandit: No issues identified
- Flake8: No violations reported
- Program execution: Expected sample output observed
- Git whitespace check: Passed

## Evidence

The before-and-after reports are saved in the `reports` directory.
