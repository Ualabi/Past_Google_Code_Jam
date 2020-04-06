from datetime import date
import os

#####################################
# Get Date
#####################################
def getDate(A):
    if len(A) == 10:
        dia = int(A[:2])
        mes = int(A[3:5])
        año = int(A[-4:])
        return date(año,mes,dia)
    elif len(A) == 8:
        dia = int(A[:2])
        mes = int(A[3:5])
        año = int('20'+A[-2:])
        return date(año,mes,dia)
    else:
        return A

#####################################
# Get Array
#####################################
def getArray(A):
    a = A.index(',')
    if ';' in A[:a]:
        wey = A[:a].split(';')
    else:
        if A[:5] == 'PAGOS':
            wey = ['PAGOS']
        else:
            wey = [A[:a]]
    A = A[a+1:] + ','
    
    aux = [wey]
    past = ''
    flag = False
    for x in A:
        if flag:
            if x == '"':
                past = float(past)
                flag = False
            elif x == ',':
                continue
            else:
                past += x
        else:
            if x == ',':
                if type(past) == float:
                    aux.append(past)
                elif '/' in past:
                    aux.append(getDate(past))
                else:
                    aux.append(past)
                past = ''
            elif x == '"':
                flag = True
            else:
                past += x
    
    return aux

#####################################
# Get the direction
#####################################
mydir = __file__
for x in range(len(mydir)-1,-1,-1):
    if (mydir[x] == '/') :
        mydir = mydir[:x+1]
        break
print(mydir)

#####################################
# Print the files
#####################################
entries = os.listdir(mydir)
print(entries,'\n')

egresosfiles = []
ingresosfiles = []
operaciones = None

for xfile in entries:
    if xfile[-3:] == 'csv' and 'Analysis' not in xfile:
        if 'E' == xfile[0]:
            egresosfiles.append(mydir+xfile)
        elif 'I' == xfile[0]:
            ingresosfiles.append(mydir+xfile)
        elif 'O' == xfile[0]:
            operaciones = mydir+xfile

print('Egresos files', egresosfiles)
print('Ingresos files', ingresosfiles)
print('Operaciones', operaciones,'\n\n')

#####################################
# Operaciones
#####################################
archivo = open(operaciones,'r', encoding='utf8')
text = archivo.read()
archivo.close()

text = text.split('\n')
arr = text[0].split(',')

ope = {}
for x in range(len(arr)):
    ope[arr[x]] = x
print(ope,'\n')

data = {'Pagos':[]}
for x in text[1:]:
    arr = x.split(',')
    key = arr[0]
    for y in range(6,13):
        arr[y] = getDate(arr[y])

    data[key] = {'Operaciones' : arr[1:]}

#####################################
# Egresos
#####################################
print('\nEgresos')
egr = {'REFERENCIA': 0, 'CONCEPTO': 1, 'RECEPTOR': 2, 'FACTURAS': 3, 'CUENTA ': 4, 'DIVISA': 5, 'MONTO': 6, 'T.C.': 7, 'VALOR MXN': 8, 'FECHA': 9}
for egresofile in egresosfiles:
    archivo = open(egresofile,'r', encoding='utf8')
    text = archivo.read()
    archivo.close()

    text = text.split('\n')[1:]
    for x in text:
        aux = getArray(x)
        print(aux)


#####################################
# Ingresos
#####################################
print('\nIngresos')
ing = {'REFERENCIA': 0, 'CONCEPTO': 1, 'EMISOR': 2, 'FACTURAS': 3, 'CUENTA': 4, 'DIVISA': 5, 'MONTO': 6, 'T.C.': 7, 'FECHA': 8}
for ingresofile in ingresosfiles:
    archivo = open(ingresofile,'r', encoding='utf8')
    text = archivo.read()
    archivo.close()

    text = text.split('\n')[1:]
    for x in text:
        aux = getArray(x)
        print(aux)