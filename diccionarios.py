def run():
    # mi_dicionario = {
    #     'llave1': 1,
    #     'llave2': 2,
    #     'llave3': 3,        
    # }
    # print(mi_dicionario['llave1'])
    # print(mi_dicionario['llave2'])
    # print(mi_dicionario['llave3'])
    poblacion_paises = {
        'Argentina': 44838712,
        'Brazi': 210147125,
        'Colombia': 5047244,
        
    }
    # print(poblacion_paises['Argentina'])

    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais in poblacion_paises.values():
    #     print(pais)
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene '+ str(poblacion) + ' habitantes')


if __name__ == '__main__':
    run()