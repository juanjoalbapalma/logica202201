# programa capaz de calcular el factorial de un número
print("Bienvenido, este programa calcula el factorial de un numero")

inicio=int(input("Por favor ingrese 1 para iniciar: \n"))
while(inicio==1):
  print("Por favor introduzca el número al que le desea calcular el factorial \n")
  numero=int(input("numero: "))
  factorial = 1
  i = 1
  for i in range(i, numero+1):
    factorial=factorial*i

  print ("El valor del número que ingresó es: \n")
  print (factorial)
  inicio=int(input("Si desea iniciar otra vez digite 1, de lo contrario cualquier otro numero \n"))