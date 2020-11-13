from funkcetah_hrace import tah_hrace
from funkcetahpocitace import tah_pocitace
from funkcevyhodnot import vyhodnot


def podminka(herni_pole):
  hodnoceni = vyhodnot(herni_pole)
  if hodnoceni == "-":
    print(f"Hra pokracuje")
  elif hodnoceni == "x" or hodnoceni == "o":
    hra_bezi = False
    print(herni_pole)
    print(f"Vyhrava {hodnoceni}")
    return False
  else:
    hra_bezi = False
    print("Remiza")
    return False 


def piskvorky_1d():
  herni_pole = '-' * 20
  print(herni_pole)
  hra_bezi = True
  while hra_bezi:
    herni_pole = tah_hrace(herni_pole)
    if podminka(herni_pole) == False:
      hra_bezi = False
      continue
    herni_pole = tah_pocitace(herni_pole)
    hodnoceni = vyhodnot(herni_pole)
    print(herni_pole)
    if podminka(herni_pole) == False: 
      hra_bezi = False
      
