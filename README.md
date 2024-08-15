# Validação de CPF e Criptografia de Senha

Este script Python realiza duas tarefas principais:

1. **Validação de CPF (Cadastro de Pessoa Física)**
2. **Criptografia e Descriptografia de Senhas**

## Funcionalidades

### 1. Validação de CPF

O script verifica se um CPF fornecido é válido. A validação considera CPFs conhecidos inválidos e utiliza um algoritmo de verificação com dígitos verificadores. A entrada é solicitada em formato `xxx.xxx.xxx-xx` e deve ter 14 caracteres.

#### Requisitos de CPF

- O CPF deve ter exatamente 14 caracteres, no formato `xxx.xxx.xxx-xx`.
- O CPF não pode ser um dos CPFs genéricos inválidos como `111.111.111-11`, `222.222.222-22`, etc.

### 2. Criptografia e Descriptografia de Senha

O script também verifica se a senha fornecida atende a certos requisitos e pode criptografar e descriptografar senhas.

#### Requisitos da Senha

- Deve conter pelo menos uma letra maiúscula.
- Deve conter pelo menos uma letra minúscula.
- Deve conter pelo menos um número.
- Deve ter entre 8 e 9 caracteres.

#### Funcionalidades

- **Criptografia**: Converte a senha para um formato criptografado.
- **Descriptografia**: Converte a senha criptografada de volta ao formato original.

## Como Executar

1. **Execute o Script**

   Execute o script usando o Python 3:

   ```bash
   python CPFeSenha.py
   ```

   Substitua `CPFeSenha.py` pelo nome do arquivo que contém o código.

## Exemplos de Uso

1. **Validação de CPF**

   - O script solicitará o CPF no formato `xxx.xxx.xxx-xx`.
   - Se o CPF for inválido ou não atender aos critérios, uma mensagem será exibida.

2. **Criptografia e Descriptografia de Senha**

   - O script solicitará uma senha.
   - A senha deve atender aos requisitos especificados.
   - Após validação, a senha será criptografada e você terá a opção de descriptografá-la.

## Código do Script

```python
def valido(cpf):
    # Função para validar o CPF
    ...

while True:
    # Loop principal para validação de CPF
    ...

def criptografia(senha):
    # Função para criptografar a senha
    ...

def descriptografia(senha2):
    # Função para descriptografar a senha
    ...

while True:
    # Loop principal para criptografia e descriptografia de senha
    ...
```

## Considerações

- O código utiliza alguns códigos de cor ANSI para colorir o texto. Isso pode não funcionar em todos os ambientes.
- A função de criptografia simples usada não é adequada para uso real em segurança.
