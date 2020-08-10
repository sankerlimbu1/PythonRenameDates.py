# Python3
# renameDates.py - Renames filesnames with American date format to Europian date

import os , shutil ,re

#create a regex that matches files with the American date format.

datePattern = re.compile(r"""^(.*?)         #all textbefore the date
         ((0|1)?\d)-                         #one or two digits for the month
         ((0|1|2|3)?\d)-                     #one or two digits for the day
         ((19|20)\d\d)                       # four digits for the year
         (.*?)$                              #all text after the date
        """, re.VERBOSE)

#Loop over the files in the working directory.
for amerFilename in os.listdir('/home/sanker/dates'):
    # print(amerFilename)
    mo = datePattern.search(amerFilename)
    # print(mo)
    #skip files without a date.
    if mo == None :
        continue
    #Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)


    #Form the European-style filename.  DD-MM-YYYY
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    #Get the full , absolute file paths.
    absWorkingDir =  os.path.abspath('/home/sanker/dates')
    amerFilename  =  os.path.join(absWorkingDir , amerFilename)
    euroFilename  =  os.path.join(absWorkingDir, euroFilename)

#Rename the files.

    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    shutil.move(amerFilename , euroFilename)

