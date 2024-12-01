t = [0]

while True:
    try:
        line = input()
    except:
        break
    
    if line == "\r":
        t.append(0)
        continue
    
    t[-1] += int(line)

print(max(t))