
from funzionigeometriche import * 
choose=""
while(choose.upper() != "E"):
 choose=input("Scegli cosa vuoi calcolare: Q) Perimetro quadrato C) Circonferenza cerchio R) Perimetro rettangolo E) Esci\n ==>")

 match choose.upper():
	 case "Q":
	  try:
	   l=float(input("Inserisci il valore del lato :"))
	  except:
	   print("Errore input.")
	   continue
	  pQuadrato(l)
	 case "C":
	  try:
	   r=float(input("Inserisci il valore del raggio :"))
	  except:
	   print("Errore input.")
	   continue
	  cCerchio(r)
	 case "R":
	  try:
	   b=float(input("Inserisci il valore della base :"))
	  except:
	   print("Errore input.")
	   continue
	  try:
	   a=float(input("Inserisci il valore dell'altezza :"))
	  except:
	   print("Errore input.")
	   continue
	  pRettangolo(b,a)
	 case "E":
	  print("Ciao!")
	 case _:
	  print("Input non valido")

