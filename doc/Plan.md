# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

This Program will aim to allow a user to input a directory containing a CSV file that
holds industry statistics based on FIPS codes, as well as the related area titles that 
correlate to those FIPS codes. The program will then keep track of the pertinent statistics
and print them out to the user. The statistics include: Number of FIPS areas in report, Total annual wages, 
Area with maximum annual wages, Maximum reported wage, Total number of establishments, Area with most 
establishments, Maximum # of establishments, Total annual employment level, Area with maximum employment, and 
Maximum reported employment level. It will report these stats for all the industries combined, as well as 
specifically the software publishing industry.


Currently I know how to read a file line by line to gather information from it, as  well how to use basic string
methods to do some useful things (like splitting and checking if something is in a string). I haven't really used
dictionaries before, but to me it seems like it shouldn't be too bad, as they seem similar to lists in the sense
that instead of an index used to access each value, each value has a key that can be any immutable data type.

I still need to reread through the instructions more times to understand exactly the format this is wanted to be
put in, but it looks like reading through the starter code gives very useful insight. I will likely need to focus
on checking the FIPS codes, putting the valid ones in a set or dictionary, and then going through the CSV, checking
the first data field(FIPS code) and adding that data to the corresponding section of the report if it's valid.


## Phase 1: System Analysis *(10%)*

**Deliver:**

*   List all of the data that is used by the program, making note of where it comes from.
*   Explain what form the output will take.
*   Describe what algorithms and formulae will be used (but don't write them yet).


## Phase 2: Design *(30%)*

**Deliver:**
* Check that an argument was put in and if not print usage message

* Open area_titles.csv file
* Read through each line, check if the FIPS code is valid


## Phase 3: Implementation *(15%)*

**Deliver:**

*   (More or less) working Python code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.


## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Review the project to ensure that all required files are present and in correct locations.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
    *   Run through your test cases to avoid nasty surprises.


## Phase 6: Maintenance

**Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to
        *   anybody besides yourself?
        *   yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading
        *   your computer's hardware?
        *   the operating system?
        *   to the next version of Python?
