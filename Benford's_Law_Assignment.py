import csv
import os
import matplotlib.pyplot as plt

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
    totalSales = 0
    with open ("./sales.csv", 'r') as reportFile:
        reportReader = csv.reader(reportFile)
        next(reportFile)
        for row in reportReader:
            print(row[1])
            totalSales = totalSales + int(row[1])
        print()
        print("Total sales: " + str(totalSales))

def characterCounter():
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
                count4 = count4 + 1
            elif char1 == "5":
                count5 = count5 + 1
            elif char1 == "6":
                count6 = count6 + 1
            elif char1 == "7":
                count7 = count7 + 1
            elif char1 == "8":
                count8 = count8 + 1
            elif char1 == "9":
                count9 = count9 + 1

    rate1 = characterRate(count1)
    rate2 = characterRate(count2)
    rate3 = characterRate(count3)
    rate4 = characterRate(count4)
    rate5 = characterRate(count5)
    rate6 = characterRate(count6)
    rate7 = characterRate(count7)
    rate8 = characterRate(count8)
    rate9 = characterRate(count9)

    print()
    print("Distribution of first digits:")
    print()
    print("1: " + str(rate1) + "%")
    print("2: " + str(rate2) + "%")
    print("3: " + str(rate3) + "%")
    print("4: " + str(rate4) + "%")
    print("5: " + str(rate5) + "%")
    print("6: " + str(rate6) + "%")
    print("7: " + str(rate7) + "%")
    print("8: " + str(rate8) + "%")
    print("9: " + str(rate9) + "%")

    folder = os.getcwd()
    fileName = folder + "\\results.csv"
    file = open(fileName, "w")
    file.writelines("Number: Frequency(%)\n")
    file.close()
    file = open(fileName, "a")
    file.writelines("1: " + str(rate1) + "%\n")
    file.writelines("2: " + str(rate2) + "%\n")
    file.writelines("3: " + str(rate3) + "%\n")
    file.writelines("4: " + str(rate4) + "%\n")
    file.writelines("5: " + str(rate5) + "%\n")
    file.writelines("6: " + str(rate6) + "%\n")
    file.writelines("7: " + str(rate7) + "%\n")
    file.writelines("8: " + str(rate8) + "%\n")
    file.writelines("9: " + str(rate9) + "%")
    file.close()

    fig, ax = plt.subplots()
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    counts = [rate1, rate2, rate3, rate4, rate5, rate6, rate7, rate8, rate9]
    bar_labels = ['1 = ' + str(rate1) + "%", '2 = ' + str(rate2) + "%", '3 = ' + str(rate3) + "%", '4 = ' + str(rate4) + "%", '5 = ' + str(rate5) + "%", '6 = ' + str(rate6) + "%", '7 = ' + str(rate7) + "%", '8 = ' + str(rate8) + "%", '9 = ' + str(rate9) + "%"]
    bar_colors = ['tab:red', 'tab:orange', 'tab:green', 'tab:blue', 'tab:purple', 'tab:grey']
    ax.bar(numbers, counts, label=bar_labels, color=bar_colors)
    ax.set_ylabel('Frequency (%)')
    ax.set_xlabel('First digits')
    ax.set_title('Frequency of First Numbers in Sales Data')
    ax.legend(title='Fruit color')
    plt.show()

    print()
    print("1: " + "* "*int(rate1),)
    print("2: " + "* "*int(rate2),)
    print("3: " + "* "*int(rate3),)
    print("4: " + "* "*int(rate4),)
    print("5: " + "* "*int(rate5),)
    print("6: " + "* "*int(rate6),)
    print("7: " + "* "*int(rate7),)
    print("8: " + "* "*int(rate8),)
    print("9: " + "* "*int(rate9),)

    if (int(rate1) < 33 and int(rate1) > 28):
        print()
        print("No fraud detected.")
    else:
        print()
        print("Fraud detected.")

def characterRate(counters):
    rate = counters * 100 // 1620
    return rate

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
        characterCounter()
    
    elif userInput != "9":
        print()
        print("Please type in a valid option (3, 4, or 9).")

# Exit
print()
print("Program terminated.")
print()