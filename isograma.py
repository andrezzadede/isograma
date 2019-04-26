def is_isograma(iso):
    if type(iso) != str:
        print("Erro! Não é uma string")
    else:
        if len(iso) < 1:
            return(True)
        iso = iso.lower()

        for i in iso:
            if iso.count(i) > 1 or i not in "abcdefghijklmnopqrstuvwxyz":
                return (iso, False)
        return(iso, True)

print(is_isograma("Dermatoglyphics" ))
print(is_isograma("aba" ))     
print(is_isograma("mo0se" ))
