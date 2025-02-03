from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('cotacao.html')

@app.route('/cotacao', methods=['POST'])
def cotar():
    idades_str = request.form['idade']
    idades = [int(age.strip()) for age in idades_str.split(',')]
    plano = request.form['plano'].strip()

    valores = {}
    total_valor = 0

    for idade in idades:
        valor = 0

        if plano == 'ambulatorial (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 121.36
            elif idade <= 23:
                valor = 159.36
            elif idade <= 28:
                valor = 181.46
            elif idade <= 33:
                valor = 202.26
            elif idade <= 38:
                valor = 212.78
            elif idade <= 43:
                valor = 238.70
            elif idade <= 48:
                valor = 291.57
            elif idade <= 53:
                valor = 403.84
            elif idade <= 58:
                valor = 543.89
            else:
                valor = 705.94
        elif plano == 'ambulatorial (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 101.79
            elif idade <= 23:
                valor = 133.47
            elif idade <= 28:
                valor = 151.90
            elif idade <= 33:
                valor = 169.24
            elif idade <= 38:
                valor = 178.01
            elif idade <= 43:
                valor = 199.62
            elif idade <= 48:
                valor = 243.70
            elif idade <= 53:
                valor = 337.30
            elif idade <= 58:
                valor = 454.06
            else:
                valor = 589.17
        elif plano == 'enfermaria (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 210.32
            elif idade <= 23:
                valor = 276.44
            elif idade <= 28:
                valor = 317.35
            elif idade <= 33:
                valor = 354.99
            elif idade <= 38:
                valor = 372.55
            elif idade <= 43:
                valor = 420.50
            elif idade <= 48:
                valor = 512.19
            elif idade <= 53:
                valor = 705.41
            elif idade <= 58:
                valor = 951.01
            else:
                valor = 1235.20
        elif plano == 'enfermaria (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 175.98
            elif idade <= 23:
                valor = 231.11
            elif idade <= 28:
                valor = 265.22
            elif idade <= 33:
                valor = 296.60
            elif idade <= 38:
                valor = 311.24
            elif idade <= 43:
                valor = 351.22
            elif idade <= 48:
                valor = 427.67
            elif idade <= 53:
                valor = 588.77
            elif idade <= 58:
                valor = 793.54
            else:
                valor = 1030.49
        elif plano == 'nosso medico enfermaria (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 141.91
            elif idade <= 23:
                valor = 186.13
            elif idade <= 28:
                valor = 213.49
            elif idade <= 33:
                valor = 238.66
            elif idade <= 38:
                valor = 250.41
            elif idade <= 43:
                valor = 282.48
            elif idade <= 48:
                valor = 343.81
            elif idade <= 53:
                valor = 473.05
            elif idade <= 58:
                valor = 637.32
            else:
                valor = 827.40
        elif plano == 'nosso medico enfermaria (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 118.94
            elif idade <= 23:
                valor = 155.81
            elif idade <= 28:
                valor = 178.63
            elif idade <= 33:
                valor = 199.62
            elif idade <= 38:
                valor = 209.42
            elif idade <= 43:
                valor = 236.16
            elif idade <= 48:
                valor = 287.30
            elif idade <= 53:
                valor = 395.06
            elif idade <= 58:
                valor = 532.03
            else:
                valor = 690.53
        elif plano == 'apartamento (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 237.57
            elif idade <= 23:
                valor = 312.41
            elif idade <= 28:
                valor = 358.72
            elif idade <= 33:
                valor = 401.32
            elif idade <= 38:
                valor = 421.20
            elif idade <= 43:
                valor = 475.47
            elif idade <= 48:
                valor = 579.26
            elif idade <= 53:
                valor = 797.97
            elif idade <= 58:
                valor = 1075.96
            else:
                valor = 1397.64
        elif plano == 'apartamento (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 198.70
            elif idade <= 23:
                valor = 261.10
            elif idade <= 28:
                valor = 299.71
            elif idade <= 33:
                valor = 335.23
            elif idade <= 38:
                valor = 351.81
            elif idade <= 43:
                valor = 397.06
            elif idade <= 48:
                valor = 483.60
            elif idade <= 53:
                valor = 665.96
            elif idade <= 58:
                valor = 897.75
            else:
                valor = 1165.96
        elif plano == 'nosso medico apartamento (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 183.38
            elif idade <= 23:
                valor = 240.87
            elif idade <= 28:
                valor = 276.44
            elif idade <= 33:
                valor = 309.17
            elif idade <= 38:
                valor = 324.44
            elif idade <= 43:
                valor = 366.13
            elif idade <= 48:
                valor = 445.86
            elif idade <= 53:
                valor = 613.88
            elif idade <= 58:
                valor = 827.44
            else:
                valor = 1074.56
        elif plano == 'nosso medico apartamento (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 153.52
            elif idade <= 23:
                valor = 201.46
            elif idade <= 28:
                valor = 231.12
            elif idade <= 33:
                valor = 258.41
            elif idade <= 38:
                valor = 271.15
            elif idade <= 43:
                valor = 305.92
            elif idade <= 48:
                valor = 372.41
            elif idade <= 53:
                valor = 512.52
            elif idade <= 58:
                valor = 690.60
            else:
                valor = 896.67
        elif plano == 'ambulatorial (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 109.45
            elif idade <= 23:
                valor = 122.58
            elif idade <= 28:
                valor = 137.29
            elif idade <= 33:
                valor = 157.88
            elif idade <= 38:
                valor = 181.56
            elif idade <= 43:
                valor = 216.06
            elif idade <= 48:
                valor = 270.08
            elif idade <= 53:
                valor = 337.60
            elif idade <= 58:
                valor = 573.92
            else:
                valor = 642.79
        elif plano == 'ambulatorial (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 88.45
            elif idade <= 23:
                valor = 99.06
            elif idade <= 28:
                valor = 110.95
            elif idade <= 33:
                valor = 127.59
            elif idade <= 38:
                valor = 146.73
            elif idade <= 43:
                valor = 174.61
            elif idade <= 48:
                valor = 218.26
            elif idade <= 53:
                valor = 272.83
            elif idade <= 58:
                valor = 463.81
            else:
                valor = 519.47
        elif plano == 'enfermaria (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 133.14
            elif idade <= 23:
                valor = 149.12
            elif idade <= 28:
                valor = 167.01
            elif idade <= 33:
                valor = 192.06
            elif idade <= 38:
                valor = 220.87
            elif idade <= 43:
                valor = 262.84
            elif idade <= 48:
                valor = 328.55
            elif idade <= 53:
                valor = 410.69
            elif idade <= 58:
                valor = 698.17
            else:
                valor = 781.95
        elif plano == 'enfermaria (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 107.53
            elif idade <= 23:
                valor = 120.43
            elif idade <= 28:
                valor = 134.88
            elif idade <= 33:
                valor = 155.11
            elif idade <= 38:
                valor = 178.38
            elif idade <= 43:
                valor = 212.27
            elif idade <= 48:
                valor = 265.34
            elif idade <= 53:
                valor = 331.68
            elif idade <= 58:
                valor = 563.86
            else:
                valor = 631.52
        elif plano == 'apartamento (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 198.94
            elif idade <= 23:
                valor = 222.81
            elif idade <= 28:
                valor = 249.55
            elif idade <= 33:
                valor = 286.98
            elif idade <= 38:
                valor = 330.03
            elif idade <= 43:
                valor = 392.74
            elif idade <= 48:
                valor = 490.93
            elif idade <= 53:
                valor = 613.66
            elif idade <= 58:
                valor = 1043.22
            else:
                valor = 1168.41
        elif plano == 'apartamento (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 160.52
            elif idade <= 23:
                valor = 179.78
            elif idade <= 28:
                valor = 201.35
            elif idade <= 33:
                valor = 231.55
            elif idade <= 38:
                valor = 266.28
            elif idade <= 43:
                valor = 316.87
            elif idade <= 48:
                valor = 396.09
            elif idade <= 53:
                valor = 495.11
            elif idade <= 58:
                valor = 841.69
            else:
                valor = 942.69
        elif plano == 'nosso medico enfermaria (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 122.61
            elif idade <= 23:
                valor = 137.32
            elif idade <= 28:
                valor = 153.80
            elif idade <= 33:
                valor = 176.87
            elif idade <= 38:
                valor = 203.40
            elif idade <= 43:
                valor = 242.05
            elif idade <= 48:
                valor = 302.56
            elif idade <= 53:
                valor = 378.20
            elif idade <= 58:
                valor = 642.94
            else:
                valor = 720.09
        elif plano == 'nosso medico enfermaria (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 99.05
            elif idade <= 23:
                valor = 110.94
            elif idade <= 28:
                valor = 124.25
            elif idade <= 33:
                valor = 142.89
            elif idade <= 38:
                valor = 164.32
            elif idade <= 43:
                valor = 195.54
            elif idade <= 48:
                valor = 244.43
            elif idade <= 53:
                valor = 305.54
            elif idade <= 58:
                valor = 519.42
            else:
                valor = 581.75
        elif plano == 'nosso medico apartamento (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 183.16
            elif idade <= 23:
                valor = 205.14
            elif idade <= 28:
                valor = 229.76
            elif idade <= 33:
                valor = 264.22
            elif idade <= 38:
                valor = 303.85
            elif idade <= 43:
                valor = 361.58
            elif idade <= 48:
                valor = 451.98
            elif idade <= 53:
                valor = 564.98
            elif idade <= 58:
                valor = 960.47
            else:
                valor = 1075.73
        elif plano == 'nosso medico apartamento (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 147.80
            elif idade <= 23:
                valor = 165.54
            elif idade <= 28:
                valor = 185.40
            elif idade <= 33:
                valor = 213.21
            elif idade <= 38:
                valor = 245.19
            elif idade <= 43:
                valor = 291.78
            elif idade <= 48:
                valor = 364.73
            elif idade <= 53:
                valor = 455.91
            elif idade <= 58:
                valor = 775.05
            else:
                valor = 868.06
        else:
            return 'Plano inválido'

        if idade not in valores:
            valores[idade] = {'plano': [], 'qtd': 0}

        valores[idade]['plano'].append(valor)
        total_valor += valor
        valores[idade]['qtd'] += 1

    total_valor = '{:.2f}'.format(total_valor)

    return render_template('resposta.html', valores=valores, total_valor=total_valor, plano_selecionado=plano)

if __name__ == '__main__':
    app.run(debug=True)
