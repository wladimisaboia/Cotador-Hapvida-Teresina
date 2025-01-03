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
                valor = 114.59
            elif idade <= 23:
                valor = 150.44
            elif idade <= 28:
                valor = 171.29
            elif idade <= 33:
                valor = 190.91
            elif idade <= 38:
                valor = 200.84
            elif idade <= 43:
                valor = 225.30
            elif idade <= 48:
                valor = 275.18
            elif idade <= 53:
                valor = 381.10
            elif idade <= 58:
                valor = 513.23
            else:
                valor = 666.12
        elif plano == 'ambulatorial (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 96.13
            elif idade <= 23:
                valor = 126.02
            elif idade <= 28:
                valor = 143.40
            elif idade <= 33:
                valor = 159.76
            elif idade <= 38:
                valor = 168.04
            elif idade <= 43:
                valor = 188.43
            elif idade <= 48:
                valor = 230.02
            elif idade <= 53:
                valor = 318.32
            elif idade <= 58:
                valor = 428.47
            else:
                valor = 555.93
        elif plano == 'enfermaria com obstetrícia (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 170.19
            elif idade <= 23:
                valor = 223.50
            elif idade <= 28:
                valor = 256.49
            elif idade <= 33:
                valor = 286.84
            elif idade <= 38:
                valor = 301.00
            elif idade <= 43:
                valor = 339.66
            elif idade <= 48:
                valor = 413.59
            elif idade <= 53:
                valor = 569.39
            elif idade <= 58:
                valor = 767.42
            else:
                valor = 996.57
        elif plano == 'enfermaria com obstetrícia (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 142.51
            elif idade <= 23:
                valor = 186.96
            elif idade <= 28:
                valor = 214.46
            elif idade <= 33:
                valor = 239.76
            elif idade <= 38:
                valor = 251.57
            elif idade <= 43:
                valor = 283.81
            elif idade <= 48:
                valor = 345.46
            elif idade <= 53:
                valor = 475.37
            elif idade <= 58:
                valor = 640.49
            else:
                valor = 831.56
        elif plano == 'enfermaria sem obstetrícia (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 133.98
            elif idade <= 23:
                valor = 175.70
            elif idade <= 28:
                valor = 201.52
            elif idade <= 33:
                valor = 225.27
            elif idade <= 38:
                valor = 236.35
            elif idade <= 43:
                valor = 266.61
            elif idade <= 48:
                valor = 324.47
            elif idade <= 53:
                valor = 446.40
            elif idade <= 58:
                valor = 601.38
            else:
                valor = 780.71
        elif plano == 'enfermaria sem obstetrícia (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 112.31
            elif idade <= 23:
                valor = 147.10
            elif idade <= 28:
                valor = 168.63
            elif idade <= 33:
                valor = 188.43
            elif idade <= 38:
                valor = 197.67
            elif idade <= 43:
                valor = 222.90
            elif idade <= 48:
                valor = 271.15
            elif idade <= 53:
                valor = 372.82
            elif idade <= 58:
                valor = 502.05
            else:
                valor = 651.59
        elif plano == 'apartamento com obstetrícia (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 192.17
            elif idade <= 23:
                valor = 252.51
            elif idade <= 28:
                valor = 289.85
            elif idade <= 33:
                valor = 324.20
            elif idade <= 38:
                valor = 340.23
            elif idade <= 43:
                valor = 383.99
            elif idade <= 48:
                valor = 467.68
            elif idade <= 53:
                valor = 644.03
            elif idade <= 58:
                valor = 868.18
            else:
                valor = 1127.55
        elif plano == 'apartamento com obstetrícia (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 160.83
            elif idade <= 23:
                valor = 211.14
            elif idade <= 28:
                valor = 242.27
            elif idade <= 33:
                valor = 270.91
            elif idade <= 38:
                valor = 284.28
            elif idade <= 43:
                valor = 320.77
            elif idade <= 48:
                valor = 390.55
            elif idade <= 53:
                valor = 537.59
            elif idade <= 58:
                valor = 724.49
            else:
                valor = 940.76
        elif plano == 'apartamento sem obstetrícia (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 173.10
            elif idade <= 23:
                valor = 227.34
            elif idade <= 28:
                valor = 260.90
            elif idade <= 33:
                valor = 291.78
            elif idade <= 38:
                valor = 306.19
            elif idade <= 43:
                valor = 345.53
            elif idade <= 48:
                valor = 420.75
            elif idade <= 53:
                valor = 579.27
            elif idade <= 58:
                valor = 780.75
            else:
                valor = 1013.90
        elif plano == 'apartamento sem obstetrícia (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 144.93
            elif idade <= 23:
                valor = 190.16
            elif idade <= 28:
                valor = 218.14
            elif idade <= 33:
                valor = 243.88
            elif idade <= 38:
                valor = 255.89
            elif idade <= 43:
                valor = 288.69
            elif idade <= 48:
                valor = 351.41
            elif idade <= 53:
                valor = 483.58
            elif idade <= 58:
                valor = 651.57
            else:
                valor = 845.96
        elif plano == 'ambulatorial (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 103.33
            elif idade <= 23:
                valor = 115.73
            elif idade <= 28:
                valor = 129.62
            elif idade <= 33:
                valor = 149.06
            elif idade <= 38:
                valor = 171.42
            elif idade <= 43:
                valor = 203.99
            elif idade <= 48:
                valor = 254.99
            elif idade <= 53:
                valor = 318.74
            elif idade <= 58:
                valor = 541.86
            else:
                valor = 606.88
        elif plano == 'ambulatorial (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 83.53
            elif idade <= 23:
                valor = 93.55
            elif idade <= 28:
                valor = 104.78
            elif idade <= 33:
                valor = 120.50
            elif idade <= 38:
                valor = 138.58
            elif idade <= 43:
                valor = 164.91
            elif idade <= 48:
                valor = 206.14
            elif idade <= 53:
                valor = 257.68
            elif idade <= 58:
                valor = 438.06
            else:
                valor = 490.63
        elif plano == 'enfermaria (pessoa jurídica) - Sem coparticipação, exceto terapias':
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
        elif plano == 'enfermaria (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 101.52
            elif idade <= 23:
                valor = 113.70
            elif idade <= 28:
                valor = 127.34
            elif idade <= 33:
                valor = 146.44
            elif idade <= 38:
                valor = 168.41
            elif idade <= 43:
                valor = 200.41
            elif idade <= 48:
                valor = 250.51
            elif idade <= 53:
                valor = 313.14
            elif idade <= 58:
                valor = 532.34
            else:
                valor = 596.22
        elif plano == 'apartamento (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 187.76
            elif idade <= 23:
                valor = 210.29
            elif idade <= 28:
                valor = 235.52
            elif idade <= 33:
                valor = 270.85
            elif idade <= 38:
                valor = 311.48
            elif idade <= 43:
                valor = 370.66
            elif idade <= 48:
                valor = 463.33
            elif idade <= 53:
                valor = 579.16
            elif idade <= 58:
                valor = 984.57
            else:
                valor = 1102.72
        elif plano == 'apartamento (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 151.51
            elif idade <= 23:
                valor = 169.69
            elif idade <= 28:
                valor = 190.05
            elif idade <= 33:
                valor = 218.56
            elif idade <= 38:
                valor = 251.34
            elif idade <= 43:
                valor = 299.09
            elif idade <= 48:
                valor = 373.86
            elif idade <= 53:
                valor = 467.33
            elif idade <= 58:
                valor = 794.76
            else:
                valor = 889.80
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
