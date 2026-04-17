import secrets

def generate_password(
    length: int = 12,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    avoid_ambiguous: bool = False,
   )-> str:

def richiesta_modello_password():
#chiede all’utente quale profilo vuole
  # — default o custom — e poi mostra la password o la salva su disco
  modello=input("inserire modello scelto: 1.Deafult o 2.Custom")
  if modello=="1":
      print(generate_password())


  elif modello=="2":






