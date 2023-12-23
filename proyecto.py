from sklearn import tree
#Se crea la instancia del arbol de decision.
clf = tree.DecisionTreeClassifier()

#[sintoma1, sintoma2, sintoma3]
X = [[1, 2,  7], [1, 2,  8], [1, 7, 8], [2, 7,  8], [1, 7,11], 
     [1, 7, 13], [1, 8, 11], [1, 8,13], [2, 8, 11], [2, 8,13], 
     [1, 11,13], [2, 11,13], [2, 7, 8], [2, 7, 11], [2, 7,13], 
     [7, 8, 11], [7, 8, 13], [8,11,13], [1, 2,  3], [1, 2, 5], 
     [1, 2,  9], [1, 2, 10], [1, 2,12], [2, 3,  5], [2, 3, 9], 
     [2, 3, 10], [2, 3, 12], [3, 5, 9], [3, 5, 10], [3, 5,12], 
     [1, 3,  5], [1, 3,  9], [1, 3,10], [1, 3, 12], [1, 5, 9], 
     [1, 5, 10], [1, 5, 12], [5, 9,10], [5, 9, 12], [5,10,12], [9,10,12]]

#La salida donde se dice cual es la enfermedad
Y = ['1A', '2A', '3A', '4A', '5A', 
     '1B', '2B', '3B', '4B', '5B', 
     '1C', '2C', '3C', '4C', '5C', 
     '1D', '2D', '3D', '4D', '5D', 
     '1E', '2E', '3E', '4E', '5E', 
     '1F', '2F', '3F', '4F', '5F', 
     '1G', '2G', '3G', '4G', '5G', 
     '1H', '2H', '3H', '4H', '5H', '6H']

#Se le pasa los datos  X y Y
clf = clf.fit(X, Y)


#los datos de los sintomas se puede capturar por consola

print(" ")
print("------------------------------------------------------------")
print("                  lista de Signos clinicos")
print("------------------------------------------------------------")
print("id	Sintoma")
print("1	Fiebre")
print("2	Tos")
print("3	Moco")
print("4	Congestión nasal")
print("5	Estornudo")
print("6	Dolor de garganta")
print("7	Dificultad para respirar")
print("8	Flema")
print("9	Vómito")
print("10	Diarrea")
print("11	Cansancio")
print("12	Dolor en los huesos")
print("------------------------------------------------------------")

#Ingreso de sintomas
print(" DIGITE LOS SINTOMAS:")
S1 = input("Digite el sintoma 1: ")
S2 = input("Digite el sintoma 2: ")
S3 = input("Digite el sintoma 3: ")
sintomas = [S1, S2, S3]

#Sintomas del paciente
print("------------------------------------------------------------")
print("sintomas paciente 1")
print(sintomas)
print("------------------------------------------------------------")


#Se realiza el proceso de prediccion
prediction = clf.predict([sintomas])

#Se muestra el resultado de la prediccion 

print("Diagnostico del Paciente")
print(prediction)


#Se le pregunta al usuario si desea realizar otro diagnóstico

while True:
     print("------------------------------------------------------------")
     respuesta = input("¿Desea realizar otro diagnóstico? (s/n): ")
     if respuesta.lower() == 's':
        print(" ")
        print("------------------------------------------------------------")
        print(" lista de Signos clinicos")
        print("------------------------------------------------------------")
        print("id Sintoma")
        print("1 Fiebre")
        print("2 Tos")
        print("3 Moco")
        print("4 Congestión nasal")
        print("5 Estornudo")
        print("6 Dolor de garganta")
        print("7 Dificultad para respirar")
        print("8 Flema")
        print("9 Vómito")
        print("10 Diarrea")
        print("11 Cansancio")
        print("12 Dolor en los huesos")
        print("13 Mancha pulmón rayos x")
        print("------------------------------------------------------------")
        S1 = input("Digite el sintoma 1: ")
        S2 = input("Digite el sintoma 2: ")
        S3 = input("Digite el sintoma 3: ")
        sintomas = [S1, S2, S3]

        # Sintomas del paciente
        print("------------------------------------------------------------")
        print("sintomas paciente 1")
        print(sintomas)
        print("------------------------------------------------------------")

        # Se realiza el proceso de prediccion
        prediction = clf.predict([sintomas])

        # Se muestra el resultado de la prediccion
        print("Diagnostico del Paciente")
        print(prediction)


     elif respuesta.lower() == 'n':
          print("------------------------------------------------------------")
          print("Gracias por usar el sistema de diagnóstico. ¡Hasta luego!")
          print("------------------------------------------------------------")

          break
     else:
          print("----------------------------------")
          print("Respuesta inválida. Por favor, responda 's' o 'n'.")
          print("----------------------------------")





