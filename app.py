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
        elif plano == 'enfermaria com obstetrícia (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 180.30
            elif idade <= 23:
                valor = 236.81
            elif idade <= 28:
                valor = 271.78
            elif idade <= 33:
                valor = 303.95
            elif idade <= 38:
                valor = 318.96
            elif idade <= 43:
                valor = 359.94
            elif idade <= 48:
                valor = 438.31
            elif idade <= 53:
                valor = 603.46
            elif idade <= 58:
                valor = 813.37
            else:
                valor = 1056.27
        elif plano == 'enfermaria com obstetrícia (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 150.95
            elif idade <= 23:
                valor = 198.07
            elif idade <= 28:
                valor = 227.22
            elif idade <= 33:
                valor = 254.04
            elif idade <= 38:
                valor = 266.56
            elif idade <= 43:
                valor = 300.73
            elif idade <= 48:
                valor = 366.07
            elif idade <= 53:
                valor = 503.77
            elif idade <= 58:
                valor = 678.79
            else:
                valor = 881.31
        elif plano == 'enfermaria sem obstetrícia (pessoa física) - Sem coparticipação, exceto terapias':
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
        elif plano == 'enfermaria sem obstetrícia (pessoa física) - Com coparticipação':
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
        elif plano == 'apartamento com obstetrícia (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 203.59
            elif idade <= 23:
                valor = 267.55
            elif idade <= 28:
                valor = 307.13
            elif idade <= 33:
                valor = 343.54
            elif idade <= 38:
                valor = 360.53
            elif idade <= 43:
                valor = 406.92
            elif idade <= 48:
                valor = 495.63
            elif idade <= 53:
                valor = 682.56
            elif idade <= 58:
                valor = 920.16
            else:
                valor = 1195.10
        elif plano == 'apartamento com obstetrícia (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 170.37
            elif idade <= 23:
                valor = 223.70
            elif idade <= 28:
                valor = 256.70
            elif idade <= 33:
                valor = 287.06
            elif idade <= 38:
                valor = 301.23
            elif idade <= 43:
                valor = 339.91
            elif idade <= 48:
                valor = 413.87
            elif idade <= 53:
                valor = 569.73
            elif idade <= 58:
                valor = 767.84
            else:
                valor = 997.08
        elif plano == 'apartamento sem obstetrícia (pessoa física) - Sem coparticipação, exceto terapias':
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
        elif plano == 'apartamento sem obstetrícia (pessoa física) - Com coparticipação':
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
