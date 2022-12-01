lines = []
with open('input.txt') as f:
    lines = f.readlines()
crn_sum = 0
sums = []
for ln in lines:
    if ln != '\n':
        crn_sum += int(ln.replace('\n', ''))
    else:
        sums.append(crn_sum)
        crn_sum = 0
sums.sort(reverse=True)
print(max(sums))
print(sum(sums[0:3]))