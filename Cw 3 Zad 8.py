def usun_male(napis):

  wynik = ""


  for znak in napis:

    if znak.isupper():
      wynik += znak


  return wynik

print(usun_male("To jest przykładowy napis"))