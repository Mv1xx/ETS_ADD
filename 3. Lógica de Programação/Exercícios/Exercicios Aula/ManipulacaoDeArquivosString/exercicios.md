# STRING

### Atividade 1
    Cifra de César
    
    Avança 3 em cada caracter

    ord('a') -> 65
    chr(65) -> 'a'

### Atividade 2
    Validador de e-mail:

    ex: 
    "email.com" -> False
    "email@email" -> False

    "@email.com" -> False
    "email@." -> False
    "email@email.com" -> True

### Atividade 3
    Validador de data:
    Valide se o dia é coerente com o mês 
    ex:
    "12/12/2025" -> True
    "29/02/2024" -> True
    "29/12/2025" -> False    # CONSIDERE VALIDAR SE O ANO É BISSEXTO 
    "/02/2025" -> False
    "00/10/2025" -> False
    "00/-1/2025" -> False

# MANIPULAÇÃO DE ARQUIVOS

### Atividade 1 
    Faça o cadastro de uma pessoa com: Nome, Email e Senha
    Regras:
        Nome -> Quaisquer, contanto que não seja vazio
        Email -> Email
        Senha -> Criptografada com cifra de césar

    Salve cada aluno em um text no formato: 
    Fulano;fulano@email.com;senha123

    Ao inicializar o código deve ser carregado e apresentado os alunos já cadastrados, ou seja, os dados salvos no txt da seguinta forma:
    Fulano fulano@email.com senha123

### Atividade 2
#### ⚠️ SEM USAR O PANDAS ⚠️

    Leia o arquivo 'cat_breeds.csv' de modo que tenhamos uma variável estruturada da seguinte forma:

```python
arquivo = {
    "nome_da_coluna_1" : ["valor_da_linha_1_coluna_1", "valor_da_linha_2_coluna_1", ...] ,
    "nome_da_coluna_2" : ["valor_da_linha_1_coluna_2", "valor_da_linha_2_coluna_2", ...] ,
    "nome_da_coluna_3" : ["valor_da_linha_1_coluna_3", "valor_da_linha_2_coluna_3", ...] ,
}
```

    Ou seja aplicado no arquivo:
```python
arquivo = {
    "Breed" : ["Angora", "Angora", ...],
    "Age_in_years" : ["0.25", "0.33", ...],
    "Age_in_months" : ["3", "4", ...],
    ...
}
```

with open('./cat_breeds.csv', 'r') as anotacoes:
    lines = anotacoes.readlines()
    for line in lines:
        print(line)
