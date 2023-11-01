# CPF Management System - Documentation

## Introduction

This Python program serves as a basic CPF (Cadastro de Pessoas Físicas - Brazilian Individual Taxpayer Registry) management system. It allows users to add new CPFs along with associated names and later view the added CPFs.

## How to Use

1. Run the program in your preferred Python environment.
2. The program will prompt you to choose between two options:
   a. **Adicionar novo CPF** (Add new CPF): This option allows you to input a name and a CPF, which will be added to the system.
   b. **Verificar CPF** (View CPF): This option displays the current list of names and corresponding CPFs in the system.

### Adding a New CPF

1. Select option 1 or enter "1".
2. Enter the "nome" (name) associated with the CPF.
3. Enter the "cpf" (CPF) itself.
4. The program will add the name and CPF to the system and display the updated list.

### Viewing the CPF List

1. Select option 2 or enter "2".
2. The program will display the current list of names and corresponding CPFs that were added.

## Program Logic

- The program consists of three functions:
  1. `menu()`: This function displays the main menu to the user and returns the selected option.
  2. `main()`: This is the main function that controls the flow of the program. It initializes an empty list `cpf` to store the CPFs and an empty tuple `nome` to store the names (although not used in the current code). The function calls `menu()` to get the user's choice and performs actions based on the selected option.
  3. The program uses a dictionary `lista` to store the user-inputted names and CPFs as key-value pairs.

## Example Usage

```
qual opção você deseja acessar?
1-Adicionar novo CPF.
2-Verificar CPF.
1
nome: João da Silva
cpf: 123.456.789-00
qual opção você deseja acessar?
1-Adicionar novo CPF.
2-Verificar CPF.
1
nome: Maria Souza
cpf: 987.654.321-00
qual opção você deseja acessar?
1-Adicionar novo CPF.
2-Verificar CPF.
2
{'João da Silva': '123.456.789-00', 'Maria Souza': '987.654.321-00'}
```

## Note

- The CPFs and names are stored as key-value pairs in a dictionary `lista`. In the current implementation, only one name-CPF pair can be stored in the dictionary at a time.
- The program does not include data validation for the CPF format or handle repeated CPFs/names. In a real-world application, data validation and handling of duplicate entries would be important considerations.
