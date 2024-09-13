def main():
    import sys  # Importa o módulo sys para acesso à entrada padrão

    # Substitui a função input() para ler toda a entrada padrão de uma vez
    input = sys.stdin.read
    # Lê toda a entrada, remove espaços extras no início e no final, e divide em linhas
    dados = input().strip().split('\n')

    # Converte a primeira linha da entrada para o número de casos a serem processados
    casos = int(dados[0])

    # Itera sobre cada linha de dados (começando do índice 1, já que o índice 0 é o número de casos)
    for i in range(1, casos + 1):
        # Divide a linha atual em quatro partes: nome, stu, dob e cursos
        nome, stu, dob, cursos = dados[i].split()
        # Converte o valor de cursos para um número inteiro
        cursos = int(cursos)

        # Verifica as condições para determinar a elegibilidade
        if int(stu[:4]) >= 2010 or int(dob[:4]) >= 1991:
            resultado = "eligible"  # Se a condição for atendida, o resultado é "eligible"
        elif cursos > 40:
            resultado = "ineligible"  # Se cursos > 40, o resultado é "ineligible"
        else:
            resultado = "coach petitions"  # Caso contrário, o resultado é "coach petitions"

        # Imprime o nome seguido pelo resultado de elegibilidade
        print(f"{nome} {resultado}")

    # Verifica se o script está sendo executado diretamente e chama a função main


if __name__ == "__main__":
    main()