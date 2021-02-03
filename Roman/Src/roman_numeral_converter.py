#create a class that handles the roman number conversion 
class RomanDecimalConversion(object):
    #define function to handle the conversion process
    def conversionFunc(self, number):
        romanNum = ""
        
        if (number >= (10 - 1)):
            if (number < 10):
                romanNum = "I"
                number = number + 1
            romanNum = romanNum + "X"
            number = number - 10

        if (number >= (5 - 1)):
            if (number < 5):
                romanNum = romanNum + "I"
                number = number + 1
            romanNum = romanNum + "V"
            number = number -  5

        romanNum = romanNum + (number * "I")
        
        return romanNum
