import sys

sna_file = sys.argv[1]

file1 = open(sna_file, 'r')
lines = file1.readlines()

sna_cov = {}
for l in lines:
    l = l.strip()
    sp = l.split(' ')
    if len(l) < 3:
        continue
    sna_cov[(sp[0],sp[1])] = sp[2]
file1.close()

cnt = 0.0
for m,l in sna_cov:
    if sna_cov[(m,l)] == "True":
        cnt = cnt + 1

print(100*cnt/len(sna_cov))

