count = 0
total = 0
print("Enter your scores: ")
scores = input()
while (scores != 'stop'):
    count = count + 1
    total = total + int(scores)
    scores = input()
mean = total / count
print('The mean of the numbers is: ' + str(mean))