n = int(input("n = "))
diff = n-1
for i in range(1,n):
  n *= diff
  diff -= 1

power = n
for i in range(1,n):
  power = n**power

print(power)