input = open("d1q1.txt", "r")
entries = input.readlines()
sum = 0

for entry in entries:
    entry = entry.replace("twone", "21")
    entry = entry.replace("eightwo", "82")
    entry = entry.replace("oneight", "18")
    entry = entry.replace("one", "1")
    entry = entry.replace("two", "2")
    entry = entry.replace("three", "3")
    entry = entry.replace("four", "4")
    entry = entry.replace("five", "5")
    entry = entry.replace("six", "6")
    entry = entry.replace("seven", "7")
    entry = entry.replace("eight", "8")
    entry = entry.replace("nine", "9")
    digits = ''.join(filter(str.isdigit, entry))
    digits = digits[0] + digits[len(digits)-1]
    print(digits)
    sum = sum + int(digits)
    print(entry)
    

print("Sum: ", sum)