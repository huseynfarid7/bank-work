# qeydler
# 2. sizin sifre 263743 dur
# 3. siz bankaya pul qoyduqdan sonra banka size 1 aydan sonra qoydugunuz meblege, meblegin 5 % i qeder elave edir



print('istediyiniz emeliyyati daxil edin: ')
print("1. dollari manata cevirmek ")
print("2. banka hesabiniza daxil olmaq ")
print("3. bankadan alacaginiz faizli geliri hesablayin ")
print("4. banka hesabi yaratmaq ")

emeliyyat = input()

if emeliyyat == '1':
   b=int(input("meblegi daxil edin:" ))
   a=b*1.70
   print(a)

if emeliyyat == '2':
    input("adinizi ve soyadinizi daxil edin: ")
    sifre=int(input("sifrenizi daxil edin: "))
    if sifre ==263743:
        print("xos gelmisiniz!")
    else:
        print("sifre yalnisdir")

if emeliyyat == '3':
    b=int(input('zehmet olmasa daxil edeceyiniz pul miqdarini qeyd edin: '))
    a=b*5/100 + int(b)
    if b>=1000:
        print("1 ay sonra gotureceyiniz mebleg " ,str(a) , "olacaq")
    elif b<1000:
        print("faizle gelir almaq ucun qoyacaginiz mebleg, minimal 1000 manat olmalidir")

if emeliyyat == '4':
    input("zehmet olmasa adinizi ve soyadinizi daxil edin: ")
    input("yasadiginiz unvani daxil edin: ")
    input("bir sifre daxil edin ve bu sifreni kimseyle paylasmayin: ")
    print("bu qeder tebrikler!")
