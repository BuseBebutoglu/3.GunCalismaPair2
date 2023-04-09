#1.bölüm: Fibonacci serisini oluşturma
fibonacciSeri = [1, 1] 
a= int(input("Bir değer giriniz: ")) 
while len(fibonacciSeri) < a:  
    next_number = fibonacciSeri[-1] + fibonacciSeri[-2]  
    fibonacciSeri.append(next_number)  
print("Fibonacci:",fibonacciSeri)


# 2. Bölüm: Mükemmel sayıyı gösterme

num = int(input("Bir sayı giriniz: ")) 
divisors = []  

for i in range(1, num):  
    if num % i == 0:  
        divisors.append(i)  

if sum(divisors) == num:  20
    print(num, "mükemmel bir sayıdır.")
else:
    print(num, "mükemmel bir sayı değildir.")