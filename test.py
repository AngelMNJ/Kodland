meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }
while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        # ¿Qué debemos hacer si se encuentra la palabra?
        print(meme_dict[str(word)])
    else:
        # ¿Qué hacer si no se encuentra la palabra?
        print('Revisa si esta bien escrita la palabra.')
    Si_o_no = input('Quieres seguir?')
    if Si_o_no == 'no':
        break
