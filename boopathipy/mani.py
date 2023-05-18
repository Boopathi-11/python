"""count=0
a=int(input())
while a>0:
    n= a%10
    count=count+1
    print(n)
    a=a//10
print(count)"""
"""def print_pattern(rows, cols):
    for i in range(rows):
        for j in range(1, cols + 1):
            print(j, end=' ')
        print()

# Example usage: print_pattern(2, 3)
print_pattern(3, 3)"""

"""a=int(input())
sum=0
while a>0:
    n=a%10
    sum+=n
    a//=10
print(sum)"""
num = int(input("Enter an integer: "))
digit_sum = 0

while num > 0:
    digit = num % 10
    digit_sum += digit
    num //= 10

print("Sum of digits:", digit_sum)
