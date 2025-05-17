from modelos.restaurante import Restaurante

restaurante_love = Restaurante('passion', 'canibal')
restaurante_love.receber_avaliacao('lay', 5)
restaurante_love.receber_avaliacao('ay', 0)
restaurante_love.receber_avaliacao('un', 1)

def main():
    Restaurante.listar_restaurantes()

if __name__=='__main__':
    main()