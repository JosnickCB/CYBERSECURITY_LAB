from matplotlib import pyplot as plt

# > Realizar las siguientes sustituciones: j x i, h x i, ñ x n, k x l, u x v, w x v, y x z
def task1():
    file = open('HERALDOSNEGROS.txt','r')
    task_1 = open('task1.txt','a')
    task_1_temp = []
    for i in file.read().split('\n'):
        line_temp = ""
        for character in i:
            #print("###",character)
            if(character == 'j'):
                line_temp = line_temp + 'i'
            elif(character == 'h'):
                line_temp = line_temp + 'i'
            elif(character == 'ñ'):
                line_temp = line_temp + 'n'
            elif(character == 'k'):
                line_temp = line_temp + 'l'
            elif(character == 'u'):
                line_temp = line_temp + 'v'
            elif(character == 'w'):
                line_temp = line_temp + 'x'
            elif(character == 'y'):
                line_temp = line_temp + 'z'
            else:
                line_temp = line_temp + character
        task_1_temp.append(line_temp)
        task_1_temp.append('\n')
        #print(task_1_temp)
    for i in task_1_temp:
        task_1.write(i)
    task_1.close()
    file.close()


# > Elimine las tildes
def task2():
    file = open('task1.txt','r',encoding='utf-8')
    task_2 = open('task2.txt','a',encoding='utf-8')
    tildes = 'áéíóúÁÉÍÓÚ'
    tildes_not = 'aeiouAEIOU'

    for i in file.read().split('\n'):
        #print("->",i)
        #print(normalize(i))
        for j in i:
            #print("\t#",str(j).encode('latin1'))
            if(j in tildes):
                print("Entró en",j,"#")
                for k in range(0,10):
                    if tildes[k] == j:
                        task_2.write(tildes_not[k])
                        break
            else:
                task_2.write(j)
        task_2.write('\n')

    file.close()
    task_2.close()

# > Convierta todas las letras a mayúsculas
def task3():
    file = open('task2.txt','r',encoding='utf-8')
    task_3 = open('task3.txt','a',encoding='utf-8')
    task_3.write(file.read().upper())
    file.close()
    task_3.close()

# > Elimine los espacios en blanco y los signos de puntuación
def task4():
    file = open('task3.txt','r',encoding='utf-8')
    task_4 = open('HERALDOSNEGROS_pre.txt','a',encoding='utf-8')
    specials = ';.,!¡ '
    for i in file.read().split('\n'):
        for j in i:
            if(j not in specials):
                task_4.write(j)
    file.close()
    task_4.close()

# > Abra el archivo generado e implementar una función que calcule una tabla de frecuencias para
#   cada letra de la ’A’ a ’Z’. La función deberá definirse como frecuencias(archivo) deberá devolver un
#   diccionario cuyos índices son las letras analizadas y cuyos valores son las frecuencias de las mismas
#   en el texto (número de veces que aparecen). Reconozca en el resultado obtenido los cinco caracteres
#   de mayor frecuencia
def frecuencias(archivo):
    #print(archivo.read())
    diccionario = {}
    for i in archivo.read():
        if(i in diccionario):
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    print(diccionario)
    #print(len(diccionario))
    #diccionario.sort()
    #dicc = sorted(diccionario.items() , key=lambda x: x[1] , reverse=True)
    dicc = {k: v for k, v in sorted(diccionario.items(), key=lambda item: item[1])}
    plt.bar(list(dicc.keys()),dicc.values(),color='c')
    plt.show()

# > Aplicar el método Kasiski, que recorre el texto preprocesado y halla los trigramas en el mismo
#   (sucesión de tres letras seguidas que se repiten) y las distancias (número de caracteres entre ellos)
#   entre los trigramas
def kasiski(archivo):
    trigramas = {}
    file = archivo.read()
    i = 0
    while(i < len(file)):
        if (file[i:i+3] in trigramas):
            trigramas[file[i:i+3]].append(i)
        else:
            trigramas[file[i:i+3]] = [i]
        i += 3
    
    i = 1
    while(i < len(file)):
        if (file[i:i+3] in trigramas):
            trigramas[file[i:i+3]].append(i)
        else:
            trigramas[file[i:i+3]] = [i]
        i += 3
    
    i = 2
    while(i < len(file)):
        if (file[i:i+3] in trigramas):
            trigramas[file[i:i+3]].append(i)
        else:
            trigramas[file[i:i+3]] = [i]
        i += 3
    #print(trigramas)

    trigramas_final = {}
    for key,value in trigramas.items():
        if(len(value)>1):
            trigramas_final[key] = value
    
    for key,value in trigramas_final.items():
        if(len(value)<3):
            print("Distancias de los trigramas",key,'-',value,":")
            print('\t',abs(value[1]-value[0]))
        else:
            print("Distancia de los triagramas",key,'-',value,":")
            distances = []
            for i in value:
                for j in value:
                    if( i < j and i != j):
                        if( (j,i) not in distances):
                            distances.append( (j,i) )
                            print('\t',j,'-',i,"=",j-i)
                    elif(j > i and i != j):
                        if( (i,j) not in distances):
                            distances.append( (i,j) )
                            print('\t',i,'-',j,"=",i-j)
    #print(trigramas_final)

# > Volver a preprocesar el archivo cambiando cada carácter según UNICODE-8
def task7():
    archivo = open('HERALDOSNEGROS_pre.txt','r')#,encoding='utf-8')
    task_7 = open('task7.txt','a')#,encoding='utf-8')
    for i in archivo.read():
        task_7.write(hex(ord(i))+' ')
    task_7.close()
    archivo.close()

def task8():
    archivo = open('HERALDOSNEGROS_pre.txt','r')#,encoding='utf-8')
    task_8 = open('task8.txt','a',encoding='utf-8')
    for i in archivo.read():
        task_8.write('\u8230'+' ')
    task_8.close()
    archivo.close()

def task9():
    archivo = open('HERALDOSNEGROS_pre.txt','r')#,encoding='utf-8')
    task_9 = open('task9.txt','a',encoding='utf-8')
    k = 1
    for i in archivo.read():
        if(k == 20):
            task_9.write('AQUI'+i)
            k = 1
        else:
            task_9.write(i)
            k += 1
    task_9.close()
    archivo.close()
#---------------------------------------------------
#---------------------main()------------------------
#---------------------------------------------------

task1()
task2()
task3()
task4()

archivo = open('HERALDOSNEGROS_pre.txt','r',encoding='utf-8')
frecuencias(archivo)
archivo.close()

archivo = open('HERALDOSNEGROS_pre.txt','r',encoding='utf-8')
kasiski(archivo)
archivo.close()

task7()
task8()
task9()
#plt.show()