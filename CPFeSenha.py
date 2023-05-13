def valido(cpf):

  if cpf == '111.111.111-11' or cpf == '222.222.222-22' or cpf == '333.333.333-33' or cpf == '444.444.444-44' or cpf == '555.555.555-55' or cpf == '666.666.666-66' or cpf == '777.777.777-77' or cpf == '888.888.888-88' or cpf == '999.999.999-99':
    return 'Cadastro de Pessoa Física \033[1;31minválido\033[m'

  v1 = (int(cpf[0]) * 10) + (int(cpf[1]) * 9) + (int(cpf[2]) * 8) + (
    int(cpf[4]) * 7) + (int(cpf[5]) * 6) + (int(cpf[6]) * 5) + (
      int(cpf[8]) * 4) + (int(cpf[9]) * 3) + (int(cpf[10]) * 2)

  if (v1 % 11) < 2 and (int(cpf[11]) == 0):

    v3 = (int(cpf[0]) * 11) + (int(cpf[1]) * 10) + (int(cpf[2]) * 9) + (
      int(cpf[4]) * 8) + (int(cpf[5]) * 7) + (int(cpf[6]) * 6) + (
        int(cpf[8]) * 5) + (int(cpf[9]) * 4) + (int(cpf[10]) *
                                                3) + (int(cpf[12]) * 2)

    if (v3 % 11) < 2 and int(cpf[13]) == 0:
      return 'Cadastro de Pessoa Física \033[1;32mválido\033[m'
    elif (v3 % 11) < 2 and int(cpf[13]) != 0:
      return 'Cadastro de Pessoa Física \033[1;31minválido\033[m'

    elif (v3 % 11) >= 2 and 11 - (v3 % 11) == int(cpf[13]):
      return 'Cadastro de Pessoa Física \033[1;32mválido\033[m'
    elif (v3 % 11) >= 2 and 11 - (v3 % 11) != int(cpf[13]):
      return 'Cadastro de Pessoa Física \033[1;31minválido\033[m'

  elif (v1 % 11) >= 2 and 11 - (v1 % 11) == int(cpf[12]):

    v3 = (int(cpf[0]) * 11) + (int(cpf[1]) * 10) + (int(cpf[2]) * 9) + (
      int(cpf[4]) * 8) + (int(cpf[5]) * 7) + (int(cpf[6]) * 6) + (
        int(cpf[8]) * 5) + (int(cpf[9]) * 4) + (int(cpf[10]) *
                                                3) + (int(cpf[12]) * 2)

    if (v3 % 11) < 2 and int(cpf[13]) == 0:
      return 'Cadastro de Pessoa Física \033[1;32mválido\033[m'
    if (v3 % 11) < 2 and int(cpf[13]) != 0:
      return 'Cadastro de Pessoa Física \033[1;31minválido\033[m'

    elif (v3 % 11) > 2 and 11 - (v3 % 11) == int(cpf[13]):
      return 'Cadastro de Pessoa Física \033[1;32mválido\033[m'
    elif (v3 % 11) > 2 and 11 - (v3 % 11) != int(cpf[13]):
      return 'Cadastro de Pessoa Física \033[1;31minválido\033[m'
  else:
    return 'Cadastro de Pessoa Física \033[1;31minválido\033[m'


while True:
  print('\033[1;34mCadastro de Pessoa Física\033[m')
  cpf = str(input('CPF(xxx.xxx.xxx-xx): ')).strip()
  print()
  #123.456.789-12 é um cpf inválido.
  #Delimita a Quanidade de Digitos do CPF
  if len(cpf) > 14 or len(cpf) < 14:
    print('Cadastro de Pessoa Física \033[1;31minválido\033[m')
    print('\033[1;34mCadastro de Pessoa Física\033[m')
    cpf = str(input('CPF(xxx.xxx.xxx-xx): ')).strip()
    print()

  elif len(cpf) == 14:
    if valido(cpf) == 'Cadastro de Pessoa Física \033[1;31minválido\033[m':
      print('Cadastro de Pessoa Física \033[1;31minválido\033[m')
      print()
    elif valido(cpf) == 'Cadastro de Pessoa Física \033[1;32mválido\033[m':
      break
  #Testa se o CPF é válido
print(valido(cpf))
print()

print('\033[1;35mRegras da Senha:\033[m')
print()
print('Pelo menos uma \033[1;31mLetra Maiúscula\033[m')
print('Pelo menos um \033[1;31mNúmero\033[m')
print('Pelo menos uma \033[1;31mLetra Minúscula\033[m')
print('Deve conter\033[1;31m 8 Dígitos\033[m')


def criptografia(senha):
  global senha2
  senha2 = ''
  for char in senha:
    ascii = ord(char) + 3
    senha2 += chr(ascii)
  return senha2


def descriptografia(senha2):
  global senha3
  senha3 = ''
  for char in senha2:
    ascii = ord(char) - 3
    senha3 += chr(ascii)
  return senha3


while True:
  print()
  senha = str(input('Senha:')).strip()
  list(senha)
  if len(senha) <= 7:
    print('A senha é curta')
    print('Tente de novo,\033[1;31mA senha não atende aos requisitos\033[m.')
  elif len(senha) >= 9:
    print('A senha é longa')
    print('Tente de novo,\033[1;31mA senha não atende aos requisitos\033[m.')
  else:
    if not any(x.islower() for x in senha):
      print('Deve conter pelo menos uma letra minúscula.')
      print('Tente de novo,\033[1;31mA senha não atende aos requisitos\033[m.')
    elif not any(x.isupper() for x in senha):
      print('Deve conter pelo menos uma letra maiúscula.')
      print('Tente de novo,\033[1;31mA senha não atende aos requisitos\033[m.')

    elif not any(x.isnumeric() for x in senha):
      print('Deve conter pelo menos um número.')
      print('Tente de novo,\033[1;31mA senha não atende aos requisitos\033[m.')

    else:
      print()
      print('A Senha fornecida é \033[1;32mválida.\033[m')
      print()
      
      #Limpar a tela
      import os
      os.system('clear') or None
      
      print('\033[1;34mSeu CPF é \033[m\033[0;32m{}\033[m'.format(cpf))
      print()
      print('A sua senha \033[1;31mcriptografada\033[m é',
            (criptografia(senha)))
      print()
      print('\033[1;34mDigite 1 para descriptografar\033[m')
      print()
      while True:
        cripto = int(input('Descriptografar a senha:'))
        if cripto == 1:
          print()
          print('A sua senha \033[1;31mdescriptografada\033[m é',
                (descriptografia(senha2)))
          break
        else:
          cripto = int(input('Descriptografar a senha:'))
      break

#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#DEFGHIJKLMNOPQRSTUVWXYZABC
