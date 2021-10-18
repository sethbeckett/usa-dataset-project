import time
import sys
from Report import Report


rpt = Report(year=2020)

def updateDataset(dataSet, wages, estabs, employees, areaTitle):
    '''
    Takes in an IndustryDataSet object as well as a row of data (in the form of a list) and updates the data set accordingly
    '''
    dataSet.num_areas += 1
    dataSet.total_annual_wages += wages
    dataSet.total_estab += estabs
    dataSet.total_empl += employees

    # if new max wage in area update rpt
    if wages > dataSet.max_annual_wage[1]:
        dataSet.max_annual_wage[1] = wages
        dataSet.max_annual_wage[0] = areaTitle

    # if new max establishment in area update report
    if estabs > dataSet.max_estab[1]:
        dataSet.max_estab[1] = estabs
        dataSet.max_estab[0] = areaTitle

    # if new max employment in area update report
    if employees > dataSet.max_empl[1]:
        dataSet.max_empl[1] = employees
        dataSet.max_empl[0] = areaTitle

if __name__ == '__main__':
    # print("TODO: if sys.argv[1] is not given, print a usage message and exit")  # DELETE ME
    #check that sys.argv[1] is given, no more and no less or exit
    if len(sys.argv) != 2:
        print("Usage: src/main.py DATA_DIRECTORY")
        sys.exit(2)

    print("Reading the databases...", file=sys.stderr)
    before = time.time()

    # print("TODO: if opening the file 'sys.argv[1]/area_titles.csv' fails, let your program crash here")  # DELETE ME
    # open the area titles file that should be in the directory given in sys.arv[1]
    if sys.argv[1].endswith("/"):
        areaTitleFile = open(sys.argv[1] + "area_titles.csv") #might have to use if statements to catch whether / is included
    else:
        areaTitleFile = open(sys.argv[1] + "/area_titles.csv")

    # print("TODO: Convert the file 'sys.argv[1]/area_titles.csv' into a dictionary")  # DELETE ME
    #make dictionary to add FIPS codes to the right area titles
    fipsDict = {}
    for line in areaTitleFile:
        splitLine = line.split(",", 1)
        areaCode = splitLine[0].strip("\"\n")
        areaTitle = splitLine[1].strip("\"\n")
        # print(splitLine)
        if areaCode.isnumeric() and not areaCode.endswith("000"):
            #only add valid fips codes to fipsDict
            fipsDict[areaCode] = areaTitle
    areaTitleFile.close()

    # print(fipsDict['11001'])

    # print("TODO: if opening the file 'sys.argv[1]/2020.annual.singlefile.csv' fails, let your program crash here")  # DELETE ME
    if sys.argv[1].endswith("/"):
        annualSingleFile2020 = open(sys.argv[1] + "2020.annual.singlefile.csv")
    else:
        annualSingleFile2020 = open(sys.argv[1] + "/2020.annual.singlefile.csv")

    # print("TODO: Collect information from 'sys.argv[1]/2020.annual.singlefile.csv', place into the Report object rpt")  # DELETE ME
    annualSingleFile2020.readline()
    for line in annualSingleFile2020: #need to double check line is a string
        singleFipsLine = line.split(",")
        # print(singleFipsLine)
        areaCode = singleFipsLine[0].strip("\"")
        industryCode = singleFipsLine[2].strip("\"")
        ownCode = singleFipsLine[1].strip("\"")
        # totalWages = int(singleFipsLine[10].strip("\" "))
        # totalEstablishments = int(singleFipsLine[8].strip("\" "))
        # totalEmployees = int(singleFipsLine[9].strip("\" "))
        # areaTitle = fipsDict[areaCode]
        # print(totalWages)
        # print(areaCode)
        # if areaCode in fipsDict: print("aread code was in dict")
        #check if valid fips code area and is for all_industries
        if (areaCode in fipsDict) and (industryCode == "10") and (ownCode == "0"):
            totalWages = int(singleFipsLine[10].strip("\" "))
            totalEstablishments = int(singleFipsLine[8].strip("\" "))
            totalEmployees = int(singleFipsLine[9].strip("\" "))
            areaTitle = fipsDict[areaCode]
            updateDataset(rpt.all, totalWages, totalEstablishments, totalEmployees, areaTitle)

        elif (areaCode in fipsDict) and (industryCode == "5112") and (ownCode == "5"):
            totalWages = int(singleFipsLine[10].strip("\" "))
            totalEstablishments = int(singleFipsLine[8].strip("\" "))
            totalEmployees = int(singleFipsLine[9].strip("\" "))
            areaTitle = fipsDict[areaCode]
            updateDataset(rpt.soft, totalWages, totalEstablishments, totalEmployees, areaTitle)

    annualSingleFile2020.close()

            # rpt.all.num_areas += 1
            # rpt.all.total_annual_wages += singleFipsLine[10]
            # rpt.all.total_estab += singleFipsLine[8]
            # rpt.all.total_empl += singleFipsLine[9]
            #
            # #if new max wage in area update rpt
            # if singleFipsLine[10] > rpt.all.max_annual_wage[1]:
            #     rpt.all.max_annual_wage[1] = singleFipsLine[10]
            #     rpt.all.max_annual_wage[0] = fipsDict[singleFipsLine[0]]
            #
            # #if new max establishment in area update report
            # if singleFipsLine[8] > rpt.all.max_estab[1]:
            #     rpt.all.max_estab[1] = singleFipsLine[8]
            #     rpt.all.max_estab[0] = fipsDict[singleFipsLine[0]]
            #
            # #if new max employment in area update report
            # if singleFipsLine[9] > rpt.all.max_empl[1]:
            #     rpt.all.max_empl[1] = singleFipsLine[9]
            #     rpt.all.max_empl[0] = fipsDict[singleFipsLine[0]]

        #check if it's specifically for the software section

    after = time.time()
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

    # Print the completed report
    print(rpt)

    print("\n\nTODO: did you delete all of these TODO messages?")  # DELETE ME#
