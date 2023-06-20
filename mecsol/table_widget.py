'''
    def criar_tabela(pontos):
        
        largura_colunas = [max(len(str(ponto[dado])) for ponto in pontos) for dado in range(5)]

        # Imprimir cabeçalho da tabela
        print('+{}+'.format('+'.join('-' * (largura + 2) for largura in largura_colunas)))
        cabecalho = ['ID do ponto', 'Posição X', 'Posição Y', 'Posição Z', 'Força']
        for i, elemento in enumerate(cabecalho):
            print('| {:{}}'.format(elemento, largura_colunas[i]), end=' ')
        print('|')
        print('+{}+'.format('+'.join('-' * (largura + 2) for largura in largura_colunas)))

        # Imprimir o conteúdo da tabela
        for ponto in pontos:
            for i, elemento in enumerate(ponto):
                print('| {:{}}'.format(elemento, largura_colunas[i]), end=' ')
            print('|')
            print('+{}+'.format('+'.join('-' * (largura + 2) for largura in largura_colunas)))
        # puxar numero de pontos
        num_pontos = int(input( ))

        pontos = []
        for i in range(num_pontos):
            id_ponto = input(getID(self).format(i + 1))
            pos_x = input(getXpositions(self).format(i + 1))
            pos_y = input(getYpositions(self).format(i + 1))
            pos_z = input(getZpositions(self).format(i + 1))
            forca = input("VALOR DA FORÇA".format(i + 1))
            pontos.append([id_ponto, pos_x, pos_y, pos_z, forca])

        criar_tabela(pontos)
        '''
        