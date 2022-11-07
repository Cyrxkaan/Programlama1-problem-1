 #Klavyeden girilen 3 basamaklı sayının basamak değerlerini yazdıran program?
abc = int(input("3 basamaklı bir sayı giriniz : "))
if len(str(abc))!=3:
      print("""fazla basamaklı bir sayı girdiniz...
  lütfen 3 basamaklı bir sayı giriniz.""")
else :
      a=str(abc)[0]
      b=str(abc)[1]
      c=str(abc)[2]
      print("a nın basamak değeri=",int(a)*100)
      print("b nin basamak değeri=",int(b)*10)
      print("c nin basamak değeri=",int(c)*1)

