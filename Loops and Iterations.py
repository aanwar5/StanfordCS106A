n = 5
while n > 0:
    print(n)
    n=n-1
print("Blastoffff")

while True:
    line = input('>')
    if line =="done":
        break
    print(line)
print("Done")

for i in [2,1,5]:
    print(i)
#checks smallest number
smallest = None
print("Before:", smallest)
for num in [4, 41, 12, 9, 74, 15]:
    if smallest is None or num < smallest:
        smallest = num
    print("Loop:", num, smallest)
    break
print("Smallest:", smallest)