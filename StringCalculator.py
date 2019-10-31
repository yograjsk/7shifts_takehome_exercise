'''
take-home excersice pointers
String Calculator Requirements (SCR):
1. Create a simple String calculator with a method: int Add(string numbers)
2. Change the Add method to handle new lines in the input format
3. Support a custom delimiter
4. Calling add with a negative number should throw an exception: “Negatives not allowed”.
The exception should list the number(s) that caused the exception

Bonus:
1. Numbers larger than 1000 should be ignored.
2. Delimiters can be arbitrary length
3. Allow for multiple delimiters
4. Combine 2 and 3 bonus questions. Allow multiple delimiters of arbitrary length
'''

class StringCalculator:

    def __init__(self,stringToCalculate):
        self.stringToCalculate = stringToCalculate


    def Add(self):
        # this will split the delimiter part and the calculaiton string part for further logic
        delimiters = self.stringToCalculate.splitlines()[0].replace("//", "")

        # creating the group of delimiters here as there could be multiple of them as mentioned in Bonus 3, also support custom delimiters of arbitrary length

        delimiterGroup = list(delimiters.split(","))

        numStr = self.stringToCalculate.splitlines()[1]
        for i in delimiterGroup:
            numStr = numStr.replace(i, delimiterGroup[0])
        delimiters = delimiterGroup[0]
        result = 0

        # creating the exception list for negative values as mentnioned in SCR 4. Raising exception below for negative number
        exceptionList = []
        nums = list(numStr.split(delimiters, len(numStr)))
        # filtering the non blank strings
        nums = list(filter(lambda x: len(x.strip()) > 0, nums))
        nums = [int(i) for i in nums]
        for i in nums:
            try:
                if i < 0:
                    exceptionList.append(i)
                    raise ValueError("Negatives not allowed")
                elif i>1000:
                    i=0
                result += int(i)
            except:
                result += 0
        #         returning final result and the exception list of negative numbers
        return result, exceptionList

# Creating the object to pass the string for calculation
sc = StringCalculator("//xyz,abcd\nxyz1abcd2xyz1001abcd-22xyz20")
# Calling the Add method created for String Calculations
print(sc.Add())

