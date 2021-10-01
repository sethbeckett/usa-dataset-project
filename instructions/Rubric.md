# CS 1440 Assignment 2 Rubric

| Points | Criteria
|:------:|--------------------------------------------------------------------------------
| 10     | Software Development Plan is comprehensive and well-written<br/>DuckieCorp project conventions are followed<br/>Other required documentation is filled out as well
| 10     | User interface/CLI meets customer's requirements
| 25     | `area_titles.csv` is processed according to requirements<br/>The file is read one line at a time<br/>FIPS areas are included/excluded appropriately<br/>A built-in data structure is used to hold information about valid FIPS areas
| 35     | `2020.annual.singlefile.csv` is processed according to requirements<br/>The file is read and processed one line at a time<br/>Only one line of the file is kept in memory at once<br/>Lines are skipped appropriately based on FIPS, industry and ownership codes<br/>Proper data conversion functions are employed
| 15     | Report output meets customer's requirements<br/>Program output matches provided examples<br/>Information is placed into the correct sections of the report<br/>Correct counts and totals are provided<br/>FIPS areas are displayed as "County, State" and not as FIPS codes

**Total points: 95**


## Penalties

Refer to the 'How to Submit Assignments" page in the DuckieCorp Employee Handbook to ensure your project is submitted properly.

*   If your program unexpectedly crashes due to a serious flaw on your part, the highest score you can possibly receive is 50% of the total points.
*   Other crashes may receive a lesser penalty, if your program otherwise runs correctly.
Additionally, this assignment is subject to the following penalties:

0.  **10 point penalty** submitted project is not a clone of the starter code repository.
1.  **10 point penalty** a module fails to import due to misspelling or incorrect capitalization.
2.  **10 point penalty** program attempts to import a module from the `src.` package; this is the result of a PyCharm misconfiguration.
3.  **10 point penalty** program contains hard-coded paths or otherwise does not function when run from *any* CWD.  (Note: names of modules in `import` statements do not count as "hard-coded").
4.  **10 point penalty** Your program *must* hard-code the filenames `area_titles.csv` and `2020.annual.singlefile.csv` exactly as given.  Do not rename these files on your computer or in your code as this will cause your program to fail when we grade it.
5.  **10 point penalty** if `eval()` or a similar function is used by your program.  You should use `int()` instead.
6.  **10 point penalty** program interactively prompts user for input.  All input to this program comes from command-line arguments or from files.
7.  **10 point penalty** if any files are not closed after being processed in _ordinary_ situations.  In the event of an error your program will display an error message and immediately exit; in such cases you do not need to take special measures to close files because they are automatically closed as your program exits.
8.  **95 point penalty** if your program uses external programs to do any work (including programs you wrote yourself).  This program is a pure-Python solution, not a shell script that relies on an external program.
9.  **95 point penalty** if your program imports any modules **except**:
    *   `sys`
    *   `time`
    *   `Report`
    *   or modules you wrote yourself
    *   This assignment is about the experience of solving this puzzle for yourself without leaning on code written by others, no matter how "real-world" it would be to do so.
10. **1 point penalty** per megabyte of CSV or ZIP files in your repository (`area_titles.csv` excepted).  If you accidentally commit a huge CSV file, ask the instructor for help.
11. **2 point penalty** per line of output on `sys.stdout` that is not due to printing the `Report` object.  Extra output to `sys.stderr` is permitted.


### What about Python's standard `csv` module?

To expand upon point #9, there exists a Python module named `csv` for
processing CSV data.  **You cannot use it to complete this assignment.**

For one thing, `csv` provides no essential capabilities that you can't
trivially achieve with Python's built-in `str` class.

More importantly, the point of this assignment is to teach you how to process
data generally.  The `csv` module won't teach you how to solve problems when
your data comes in a different format than CSV.  Put another way, CSV is a
subset of plain text data.  If you know how to deal with plain text you can
deal with CSV, but the converse isn't necessarily true.  You limit yourself if
you are only able to solve problems when somebody has already written a module.
Aim higher: become the kind of programmer who *makes* the modules.
