def average(marks):
    print("Avg:", sum(marks) / len(marks))

def high_low(marks):
    print("Highest:", max(marks), "and Lowest:", min(marks))

def absent(marks):
    absents = marks.count(-1)
    print("Number of absent students:", absents)

def pass_fail(marks):
    passed = sum(1 for mark in marks if mark >= 33)
    total = len(marks)
    print("Passed %:", (passed / total) * 100)
    print("Failed %:", ((total - passed) / total) * 100)

def highest_frequency(marks):
    frequency = {}
    for mark in marks:
        frequency[mark] = frequency.get(mark, 0) + 1
    highest_freq = max(frequency.values())
    most_common_marks = [mark for mark, freq in frequency.items() if freq == highest_freq]
    print("Highest frequency marks:", most_common_marks)

n = int(input("Total number of students: "))
marks = [int(input(f"Enter marks of roll no {i + 1}: ")) for i in range(n)]

print()
average(marks)
high_low(marks)
absent(marks)
pass_fail(marks)
highest_frequency(marks)
