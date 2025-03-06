def check_errors(problems):
    if len(problems) > 5:
        return 'Error: Too many problems.'
        

    for i in problems:
        a = i.split()
        if (a[1] != '+') and (a[1] != '-'):
            return "Error: Operator must be '+' or '-'."
        elif a[0].isnumeric() == False or a[2].isnumeric() == False:
                return 'Error: Numbers must only contain digits.'
        else:
            if len(a[0]) > 4 or len(a[2]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
        
    return True

def retorno(lista, respostas=False):
    resultados = []
    valores_cima = []
    valores_baixo = []
    sinal = []
    for i in lista:
        valores_cima.append(i.split()[0])
        valores_baixo.append(i.split()[2])
        sinal.append(i.split()[1])

    resultado_final_cima = ''
    resultado_final_baixo = ''
    corte = ''
    cont = 0

    for i, j in zip(valores_cima, valores_baixo):
        if len(i) > len(j):
            tam = len(i) - len(j) + 1
            if cont == 0:
                corte += '-'*(len(i)+2)
                resultado_final_cima +='  '+i
                resultado_final_baixo += sinal[cont] + (' '*tam) + j
            else:
                corte += '    '+'-'*(len(i)+2)
                resultado_final_cima +='      '+i
                resultado_final_baixo +='    '+sinal[cont]+(' '*tam)+j
        elif len(i) < len(j):
            tam = len(j) - len(i) + 2
            if cont == 0:
                corte += '-'*(len(j)+2)
                resultado_final_cima +=(' '*tam)+i
                resultado_final_baixo += sinal[cont]+' '+j
            else:
                corte += '    '+'-'*(len(j)+2)
                resultado_final_cima +='    '+(' '*tam)+i
                resultado_final_baixo += '    '+sinal[cont]+' '+j
        else:
            if cont == 0:
                corte += '-'*(len(j)+2)
                resultado_final_cima +='  '+i
                resultado_final_baixo += sinal[cont]+' '+j
            else:
                corte += '    '+'-'*(len(j)+2)
                resultado_final_cima +='      '+i
                resultado_final_baixo += '    '+sinal[cont]+' '+j

        cont += 1

    resultados = []
    resultado_final = ''
    cont = 0
    for i, j, k in zip(valores_cima, valores_baixo, sinal):
        if k == '+':
            soma = str(int(i)+int(j))
            resultados.append(soma)
        else:
            sub = str(int(i)-int(j))
            resultados.append(sub)
        
    for x, y in zip(corte.split(), resultados):
        tam = len(x)-len(y)
        if cont == 0:
            resultado_final += (' '*tam)+y
        else:
            resultado_final += '    '+(' '*tam)+y

        cont +=1
    
    finaleira = resultado_final_cima + '\n' + resultado_final_baixo + '\n' + corte
    
    if respostas==True:
        finaleira += '\n'+resultado_final
    
    return finaleira

def arithmetic_arranger(problems, show_answers=False):
    msg_de_erro = check_errors(problems)
    if msg_de_erro != True:
        return msg_de_erro
    
    return retorno(problems, respostas=show_answers)
