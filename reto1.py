antena_a = 54000
antena_b = 15
antena_c = 20
antena_d = 25
antena_e = 30
antena_instalada= 36900


def antena_instalada2 (antena_a, antena_b, antena_c, antena_d, antena_e):
    if antena_a == 0:
        antena_instalada = antena_b + antena_c + antena_d + antena_e
    elif antena_b == 0:
        antena_instalada = antena_a + antena_c + antena_d + antena_e
    elif antena_c == 0:
        antena_instalada = antena_a + antena_b + antena_d + antena_e
    elif antena_d == 0:
        antena_instalada = antena_a + antena_b + antena_c + antena_e
    elif antena_e == 0:
        antena_instalada = antena_a + antena_b + antena_c + antena_d
    else:
        antena_instalada = antena_a + antena_b + antena_c + antena_d + antena_e
    return antena_instalada
    