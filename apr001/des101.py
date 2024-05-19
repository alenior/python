def voto(nas: int):
    """
    -> Calcula a condição da pessoa.
    :param int nas: Ano de nascimento da pessoa para a análise.
    :return: Condição da pessoa para voto.
    """

    from datetime import date
    idade = date.today().year - nas
    if idade > 65 or idade == 16 or idade == 17:
        return f'Com {idade} anos, o voto é opcional.'
    elif idade < 16:
        return f'Com {idade} anos, o voto é proibido.'
    else:
        return f'Com {idade} anos, o voto é obrigatório.'


nas = int(input('Informe o ano de nascimento: '))
print(voto(nas))

help(voto)
