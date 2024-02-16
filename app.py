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
    desconto_aplicado = False

    for idade in idades:
        valor = 0

        #if plano == 'ambulatorial (pessoa física) - Coparticipação parcial' or plano == 'ambulatorial (pessoa física) - Com coparticipação' or plano == 'enfermaria com obstetrícia (pessoa física) - Coparticipação parcial' or plano == 'enfermaria com obstetrícia (pessoa física) - Com coparticipação' or plano == 'enfermaria sem obstetrícia (pessoa física) - Coparticipação parcial' or plano == 'enfermaria sem obstetrícia (pessoa física) - Com coparticipação' or plano == 'apartamento com obstetrícia (pessoa física) - Coparticipação parcial' or plano == 'apartamento com obstetrícia (pessoa física) - Com coparticipação' or plano == 'apartamento sem obstetrícia (pessoa física) - Coparticipação parcial' or plano == 'apartamento sem obstetrícia (pessoa física) - Com coparticipação':
            #if len(idades) >= 2 and not desconto_aplicado:
                #valor = valor * 0.95
                #desconto_aplicado = True

        if plano == 'ambulatorial (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 112.45
            elif idade <= 23:
                valor = 148.30
            elif idade <= 28:
                valor = 169.15
            elif idade <= 33:
                valor = 188.77
            elif idade <= 38:
                valor = 198.70
            elif idade <= 43:
                valor = 223.16
            elif idade <= 48:
                valor = 273.04
            elif idade <= 53:
                valor = 378.96
            elif idade <= 58:
                valor = 511.09
            else:
                valor = 663.98
        elif plano == 'ambulatorial (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 93.99
            elif idade <= 23:
                valor = 123.88
            elif idade <= 28:
                valor = 141.26
            elif idade <= 33:
                valor = 157.62
            elif idade <= 38:
                valor = 165.90
            elif idade <= 43:
                valor = 186.29
            elif idade <= 48:
                valor = 227.88
            elif idade <= 53:
                valor = 316.18
            elif idade <= 58:
                valor = 426.33
            else:
                valor = 553.79
        elif plano == 'enfermaria com obstetrícia (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 168.05
            elif idade <= 23:
                valor = 221.36
            elif idade <= 28:
                valor = 254.35
            elif idade <= 33:
                valor = 284.70
            elif idade <= 38:
                valor = 298.86
            elif idade <= 43:
                valor = 337.52
            elif idade <= 48:
                valor = 411.45
            elif idade <= 53:
                valor = 567.25
            elif idade <= 58:
                valor = 765.28
            else:
                valor = 994.43
        elif plano == 'enfermaria com obstetrícia (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 140.37
            elif idade <= 23:
                valor = 184.82
            elif idade <= 28:
                valor = 212.32
            elif idade <= 33:
                valor = 237.62
            elif idade <= 38:
                valor = 249.43
            elif idade <= 43:
                valor = 281.67
            elif idade <= 48:
                valor = 343.32
            elif idade <= 53:
                valor = 473.23
            elif idade <= 58:
                valor = 638.35
            else:
                valor = 829.42
        elif plano == 'enfermaria sem obstetrícia (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 131.84
            elif idade <= 23:
                valor = 173.56
            elif idade <= 28:
                valor = 199.38
            elif idade <= 33:
                valor = 223.13
            elif idade <= 38:
                valor = 234.21
            elif idade <= 43:
                valor = 264.47
            elif idade <= 48:
                valor = 322.33
            elif idade <= 53:
                valor = 444.26
            elif idade <= 58:
                valor = 599.24
            else:
                valor = 778.57
        elif plano == 'enfermaria sem obstetrícia (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 110.17
            elif idade <= 23:
                valor = 144.96
            elif idade <= 28:
                valor = 166.49
            elif idade <= 33:
                valor = 186.29
            elif idade <= 38:
                valor = 195.53
            elif idade <= 43:
                valor = 220.76
            elif idade <= 48:
                valor = 269.01
            elif idade <= 53:
                valor = 370.68
            elif idade <= 58:
                valor = 499.91
            else:
                valor = 649.45
        elif plano == 'apartamento com obstetrícia (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 190.03
            elif idade <= 23:
                valor = 250.37
            elif idade <= 28:
                valor = 287.71
            elif idade <= 33:
                valor = 322.06
            elif idade <= 38:
                valor = 338.09
            elif idade <= 43:
                valor = 381.85
            elif idade <= 48:
                valor = 465.54
            elif idade <= 53:
                valor = 641.89
            elif idade <= 58:
                valor = 866.04
            else:
                valor = 1125.41
        elif plano == 'apartamento com obstetrícia (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 158.69
            elif idade <= 23:
                valor = 209.00
            elif idade <= 28:
                valor = 240.13
            elif idade <= 33:
                valor = 268.77
            elif idade <= 38:
                valor = 282.14
            elif idade <= 43:
                valor = 318.63
            elif idade <= 48:
                valor = 388.41
            elif idade <= 53:
                valor = 535.45
            elif idade <= 58:
                valor = 722.35
            else:
                valor = 938.62
        elif plano == 'apartamento sem obstetrícia (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 170.96
            elif idade <= 23:
                valor = 225.20
            elif idade <= 28:
                valor = 258.76
            elif idade <= 33:
                valor = 289.64
            elif idade <= 38:
                valor = 304.05
            elif idade <= 43:
                valor = 343.39
            elif idade <= 48:
                valor = 418.61
            elif idade <= 53:
                valor = 577.13
            elif idade <= 58:
                valor = 778.61
            else:
                valor = 1011.76
        elif plano == 'apartamento sem obstetrícia (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 142.79
            elif idade <= 23:
                valor = 191.26
            elif idade <= 28:
                valor = 219.73
            elif idade <= 33:
                valor = 245.92
            elif idade <= 38:
                valor = 258.14
            elif idade <= 43:
                valor = 291.51
            elif idade <= 48:
                valor = 355.52
            elif idade <= 53:
                valor = 489.79
            elif idade <= 58:
                valor = 660.71
            else:
                valor = 858.49
        elif plano == 'ambulatorial (pessoa jurídica) - Coparticipação parcial':
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
        elif plano == 'enfermaria (pessoa jurídica) - Coparticipação parcial':
            if idade <= 18:
                valor = 125.68
            elif idade <= 23:
                valor = 140.76
            elif idade <= 28:
                valor = 157.65
            elif idade <= 33:
                valor = 181.30
            elif idade <= 38:
                valor = 208.50
            elif idade <= 43:
                valor = 248.12
            elif idade <= 48:
                valor = 310.15
            elif idade <= 53:
                valor = 387.69
            elif idade <= 58:
                valor = 659.07
            else:
                valor = 738.16
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
        elif plano == 'apartamento (pessoa jurídica) - Coparticipação parcial':
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

    if desconto_aplicado:
        total_valor = total_valor * 0.95

    total_valor = '{:.2f}'.format(total_valor)

    return render_template('resposta.html', valores=valores, total_valor=total_valor, desconto_aplicado=desconto_aplicado, plano_selecionado=plano)

if __name__ == '__main__':
    app.run(debug=True)
