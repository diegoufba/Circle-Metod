n = int(input('n: '))

def schedule_function(t,r):
    if t == n:
        return r
    if t == r:
        return n
    equation = (2*r-t) % (n-1)
    if equation == 0:
        return n-1
    else:
        return equation

schedule = []

for t in range(1,n+1):
    schedule.append([schedule_function(t,r) for r in range(1,n)])

print(schedule)