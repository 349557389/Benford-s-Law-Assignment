import csv

# Title
print()
print("Benford's Law Assignment")

# Functions
def printMenu():
    print('''
            Menu:
            3. Report on total Sales
            4. Check for fraud in sales data
            9. Quit
            ''')

def reportTotalSales():
    with open ("./sales.csv", 'r') as reportFile:
        reportReader = csv.reader(reportFile)
        for row in reportReader:
            print(row)

def checkSalesFraud():
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    with open ("./sales.csv", 'r') as checkFile:
        checkReader = csv.reader(checkFile)
        for row in checkReader:
            checkRow = row[1]
            char1 = checkRow[0]
            if char1 == "1":
                count1 = count1 + 1
            elif char1 == "2":
                count2 = count2 + 1
            elif char1 == "3":
                count3 = count3 + 1
            elif char1 == "4":
                count4 == count4 + 1
            elif char1 == "5":
                count5 = count5 + 1
            elif char1 == "6":
                count6 == count6 + 1
            elif char1 == "7":
                count7 = count7 + 1
            elif char1 == "8":
                count8 == count8 + 1
            elif char1 == "9":
                count9 == count9 + 1
    print(count1)
    print(count2)
    print(count3)
    print(count4)
    print(count5)
    print(count6)
    print(count7)
    print(count8)
    print(count9)

# Main Program
userInput = ""
reportSalesOption = "3"
checkFraudOption = "4"
exitCondition = "9"

while userInput != exitCondition:
    printMenu()
    userInput = input("Enter menu option (3, 4, or 9): ")

    if userInput == reportSalesOption:
        reportTotalSales()

    elif userInput == checkFraudOption:
        checkSalesFraud()
    
    elif userInput != "9":
        print()
        print("Please type in a valid option (3, 4, or 9).")

# Exit
print()
print("Program terminated.")
print()