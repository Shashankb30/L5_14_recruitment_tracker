# Lab 5 — Reflection

**Name:** SHASHANK B JAIN
**SRN:** PES1UG24CS620

## 1. What is static code analysis?

Static code analysis examines source code without executing it to identify potential quality, style, and security problems.

## 2. What are the roles of Pylint, Bandit, and Flake8?

Pylint identifies code-quality problems and checks programming conventions. Bandit detects common potential security vulnerabilities in Python code. Flake8 checks Python style and linting violations.

## 3. What problems were identified in the original program?

The original program contained SQL string interpolation, unsafe eval() usage, a broad exception handler that silently ignored errors, missing documentation, inconsistent function naming, long lines, trailing whitespace, and file-handling issues.

## 4. What changes were made?

SQL statements were parameterized, the salary limit was changed to a validated integer, exception suppression was removed, function names and documentation were improved, and CSV export was updated to use a context manager, UTF-8 encoding, and the csv module.

## 5. What were the final analysis results?

Pylint improved from 4.47/10 to 10.00/10. Bandit reported no issues, and Flake8 reported no violations. The sample program ran successfully and generated the CSV report.

## 6. What are the limitations of static analysis?

Static analysis cannot guarantee that a program is free of every functional or runtime defect. Findings must be reviewed in context, and functional testing is still necessary.

## 7. What did you learn?

I learned how to run multiple static analysis tools, interpret their findings, improve Python code quality, address potential security weaknesses, and compare reports before and after modifications.
