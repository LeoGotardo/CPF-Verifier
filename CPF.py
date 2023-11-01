def menu():
    menu = input(f"qual opção você deseja acessar? \n 1-Adicionar novo CPF. \n 2-Verificar CPF. \n")
    return menu

def main():
  cpf = []
  nome = ()
  lista = {}
  
  menu()
  if ind == "1":
    lista = [{input(f"nome:"): input(f"cpf:")}]
    main()

  elif ind == "2":
    print(dict(lista))

  else:
    print("Numero invalido")
    menu()

menu()
