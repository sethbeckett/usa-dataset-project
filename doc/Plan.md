# Software Development Plan

## Phase 0: Requirements Specification 

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


## Phase 1: System Analysis 

* Unique input is a directory name
  * Directory contains area_titles.csv, as well as the CSV file from which data is extracted

* Outputs the statistics listed in the Requirements section, formatted so that it tells
the user which statistics it is listing

* The only formulas/algorithms that will be used are simple addition (for when a FIPS code should be used
and data should be added to the report), and the max function (to find the max value in the list) which is already
implemented


* List all of the data that is used by the program, making note of where it comes from.
* Explain what form the output will take.
* Describe what algorithms and formulae will be used (but don't write them yet).


## Phase 2: Design 

* Check that an argument was put in and if not print usage message
  * exit

* Open area_titles.csv file (let it crash if not a valid file or directory)
* Create myFipsDict to store valid FIPS codes and titles
* Read through each line
  * check if FIPS has letters (isnumeric/isdigit?) //this block is what determines whether or not
    * check if last three digits aren't 000          the fips code is to be excluded or included
      * codeAndArea = split the line with comma, maxsplit delimiter of one
      * myFipsDict key = codeAndArea[0], value is second element
* CLOSE FIPS FILE

* make function updateReport(report rpt, array fipsRow, ) //ask how to implement this but just do it the long way

* Open singlefile csv
  * loop through lines
    * singleFipsRow = split by commas
    * make outer if conditional to check if FIPS code is valid, can probs skip other ifs
    * if first element is in myFipsDict
      * if industry_code isNumeric and int() is 10 //singleFipsRow[2]
      * //can move this section into own function, possibly reuse with other
        * if own_code isNumeric and is 0 // singleFipsRow[1], need to update all data set
          * rpt all num_areas += 1
          * rpt all totalwages += singleFipsRow[10]
          * if singleFipsRow[10] > rpt.all.max_annual_wage[1]
            * rpt.all.max_annual_wage[1] = singleFipsRow[10] 
            * rpt.all.max_annual_wage[0] = myFipsDict[singleFipsRow[0]] //gets area title
          * rpt all number of establishments += singleFipsRow[8]
          * if singleFipsRow[8] > rpt.all.max_estab[1]
            * rpt.all.max_estab[1] = singleFipsRow[8]
            * rpt.all.max_estab[0] = myFipsDict[singleFipsRow[0]]
          * rpt all total employment += fipsRow[9]
          * if fipsRow[9] > rpt.all.maxEmployment[1]
            * rpt.all.maxEmployment[1] = fipsRow[9]
            * update max employment area name too
      
        * if industry code isNumeric and is 5112
          * if own_code isNumeric and is 5 //pertinent to software publishing industry
            * do the same thing as done with all industries but for the software publishing industry
* CLOSE SINGLEFILE CSV


## Phase 3: Implementation 

The implementation phase was interesting, as I found that I had not adequately accounted for how the data was processed.
I needed to strip it down a bit more than I thought by removing the quote marks, and I also had to convert some fields of 
data into integers, depending how the report object used them.

One bigger thing that I ended up doing is just creating variables for the different data fields in each line, so that my code was a lot more readable.
I also implemented the code differently so that I could use a function rather than hardcoding everything each time that I updated the report.

I used https://devdocs.io/python~3.9/ to look into string methods, which was extremely helpful and in a nice, user-friendly format


## Phase 4: Testing & Debugging 

The first test that I ran was on the DC_all_industries directory. By doing this and having the report print out straight 0's for each
category, I found that my initial dictionary wasn't being setup right. I fixed this by stripping down each part of the line to get rid
of quotation marks.

I then ran it again and found that I needed to do that for the part of my code that processes the 2020.annual.singlefile.csv data.

Once I got that to work, I tried it on the UT_combined directory, and after that ran smoothly I tried it on the UT_reversed. Upon both of those successes,
tried it out with the USA full directory.

If one was to test out my code, they would first navigate to the instructions directory, open the README file, and install the full USA csv data by
following the instructions under the "Preparation" section. Then they navigate to any of the directories in the data directory, and follow the README's instructions on how to create that 
state's 2020.annual.singlefile.csv file. They would then change directories to make sure that they are in the projects parent directory and run "python3 src/main.py"
followed by their test directory's relative path. The program would then output the stats, which could be compared with the output.txt file in that same test directory
to verify the functionality.


## Phase 5: Deployment 

For this phase I cloned it from my gitLab repo and ran my tests from that temporary location


## Phase 6: Maintenance
The parts of my program that might be hardest to decipher is the actual implementation section of the plan compared to the code.
I feel that the code is actually cleaner and reads better than the implementation section, but I didn't want to rewrite the implementation 
when the actual code felt readable.

The vast majority of my time was spent rereading instructions and pounding out the overrall logic in the implementation section. Once that was good, I was able to code it fairly
quickly. Therefore I think that a bug would be relatively simple to track down.

Documentation will hopefully make sense to other people, I tried to keep it as general as possible. If one takes the time to read through all of the different README's it should 
be especially understandable.

This program should be fairly modular, and the only issue I could see is if one is running it through window's command prompt, where \ is used instead of /.
