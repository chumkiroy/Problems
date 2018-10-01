def countWaysToClimb(steps, n):
    totalStepsTillHere = [0] * (n+1)
    totalStepsTillHere[0] = 1

    for i in range(1, n+1):
	for step in steps:
	    previousStep = i - step
	    if previousStep >= 0:
		totalStepsTillHere[i] += totalStepsTillHere[previousStep]
    return totalStepsTillHere[n]

n = 7 #no of stairs
steps = [2, 3] #can climb a certain number of steps together

print countWaysToClimb(steps, n)
