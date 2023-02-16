def porownaj_ilosci(napis):

  ilosc_malych = 0
  ilosc_duzych = 0
  for znak in napis:
    if znak.isupper():
      ilosc_duzych += 1
    elif znak.islower():
      ilosc_malych += 1


  if ilosc_malych > ilosc_duzych:
    return -1
  elif ilosc_malych < ilosc_duzych:
    return 1
  else:
    return 0

print(porownaj_ilosci("To jest przykładowy napis"))
