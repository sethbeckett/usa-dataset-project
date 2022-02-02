class IndustryDataSet():
    """
    Contains statistics for an industry

    Note that some of these attributes are integers while some are lists
    pairing a string with an integer.
    """
    def __init__(self):
        self.num_areas          = 0

        self.total_annual_wages = 0
        self.max_annual_wage    = ["", 0]

        self.total_estab        = 0
        self.max_estab          = ["", 0]

        self.total_empl         = 0
        self.max_empl           = ["", 0]


class Report():
    """
    Collect statistics across multiple industries.

    Provide a ToString method (__str__) so that everybody's report will be
    formatted identically.  Create an instance of the Report class and print it
    out.
    """
    def __init__(self, year=1999):
        self.all  = IndustryDataSet()
        self.soft = IndustryDataSet()
        self.year = year


    def __str__(self):
        """
        Python's ToString method
        """
        return f"""
[============]
[Final Report]
[============]

Statistics over all industries in {self.year}:
=========================================================
Number of FIPS areas in report       {self.all.num_areas:,}

Total annual wages                   ${self.all.total_annual_wages:,}
Area with maximum annual wages       {self.all.max_annual_wage[0]}
Maximum reported wage                ${self.all.max_annual_wage[1]:,}

Total number of establishments       {self.all.total_estab:,}
Area with most establishments        {self.all.max_estab[0]}
Maximum # of establishments          {self.all.max_estab[1]:,}

Total annual employment level        {self.all.total_empl:,}
Area with maximum employment         {self.all.max_empl[0]}
Maximum reported employment level    {self.all.max_empl[1]:,}


Statistics over the software publishing industry in {self.year}:
=========================================================
Number of FIPS areas in report       {self.soft.num_areas:,}

Total annual wages                   ${self.soft.total_annual_wages:,}
Area with maximum annual wages       {self.soft.max_annual_wage[0]}
Maximum reported wage                ${self.soft.max_annual_wage[1]:,}

Total number of establishments       {self.soft.total_estab:,}
Area with most establishments        {self.soft.max_estab[0]}
Maximum # of establishments          {self.soft.max_estab[1]:,}

Total annual employment level        {self.soft.total_empl:,}
Area with maximum employment         {self.soft.max_empl[0]}
Maximum reported employment level    {self.soft.max_empl[1]:,}
"""


    def __repr__(self):
        """
        Idem, but for the REPL and debugger.
        Simply does the same thing as __str__()
        """
        return self.__str__()
