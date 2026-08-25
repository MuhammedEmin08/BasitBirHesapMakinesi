first_number = float(input("İlk Sayınızı giriniz : "))
second_number = float(input("İkinci Sayınızı giriniz : "))
which_procces  = input("toplama(+),çıkarma(-),çarpma(*),bölme(/) :")
if which_procces == "+":
    def toplama(x,y):
        print(x + y)
    toplama(first_number,second_number)
elif which_procces == "-":
    def çıkarma(x,y):
        print(x - y)
    çıkarma(first_number,second_number)
elif which_procces == "*":
    def çarpma(x,y):
        print(x * y)
    çarpma(first_number,second_number)
elif which_procces == "/":
    def bölme(x,y):
        print(x / y)
    bölme(first_number,second_number)
else:
    print("Lütfen belirtilmiş olan işlemleri seçin!")



