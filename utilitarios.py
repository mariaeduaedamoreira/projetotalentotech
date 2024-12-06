def obter_inteiro_valido(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, insira um número válido.")

def obter_string_nao_vazia(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("O valor não pode estar vazio.")
