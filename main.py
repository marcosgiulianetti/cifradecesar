Criptografa = 1
Descriptografa = 0

def CifraCesar(mensagem, key, modo):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    nova_mensagem = ''
    for c in mensagem:
        index = alfabeto.find(c)
        if index == -1:
            nova_mensagem += c
        else:
            new_index = index + key if modo == Criptografa else index - key
            new_index = new_index % len(alfabeto)
            nova_mensagem += alfabeto[new_index:new_index+1]
    return nova_mensagem

if __name__ == '__main__':

    op = int(1)

    while(op != 3):
        op = int(input("Informe o que você deseja fazer:\n\n1) Criptografar\n2) Descriptografar\n3) Sair\n\nOpção: "))

        if(op == 1):
            mensagem = input("Informe a sua mensagem: ")
            key = int(input("Informe a sua chave: "))
            print(CifraCesar(mensagem, key, 1))
        if(op == 2):
            mensagem = input("Informe a sua mensagem: ")
            key = int(input("Informe a sua chave: "))
            print(CifraCesar(mensagem, key, 0))