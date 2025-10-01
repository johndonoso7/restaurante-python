print("Bienvenido a mi restaurante")
print("Hay ensalada, pizza hamburguesa o pasta")

orden1 = input ("\nQue desea ordenar? ")
print("muy bien, elegiste",orden1)

cantidad1 = int(input ("De su primer orden Cuantos desea?"))


if cantidad1 > 0:
    print(f"- {cantidad1} {orden1}(s)")
if orden1.lower() == "ensalada":
    precio1 = 5
    print("La ensalada muy fresca y cuesta 5 euros")
    print(f"Entonces como son {cantidad1} {orden1}(s) seria un total a pagar:{cantidad1 * precio1}euros")
elif orden1.lower() == "pizza":
    precio1 = 8
    print ("La pizza esta recien salida del horno y cuesta 8 euros")
    print(f"Entonces como son {cantidad1} {orden1}(s) seria un total a pagar: {cantidad1 * precio1}euros"  )
elif orden1.lower() == "pasta":
    precio1= 7
    print("La pasta nuestra especialidad y cuesta 7 euros")
    print(f"Entonces como son {cantidad1} {orden1}(s) seria un total a pagar: {cantidad1 * precio1}euros"  )
elif orden1.lower() == "hamburguesa":
    precio1 = 9
    print("La hamburguesa con queso y papas fritas cuesta 9 euros")
    print(f"Entonces como son {cantidad1} {orden1}(s) seria un total a pagar: {cantidad1 * precio1}euros"  )
else:
    print("Lo siento, no esta en el menu") 

    precio1 = 0
    cantidad1 = 0

orden2 = input ("\n Desea ordenar otro plato cual es? ")
print("muy bien, elegiste",orden2)
cantidad2 = int(input ("De su segunda orden Cuat@s desea ordenar?"))

if cantidad2 > 0:
    print(f"- {cantidad2} {orden2}(s)")

if orden2.lower() == "ensalada":
    precio2 = 5
    print("La ensalada muy fresca y cuesta 5 euros")
    print(f"Entonces como son {cantidad2} {orden2}(s) seria un total a pagar:{cantidad2 * precio2}euros")
elif orden2.lower() == "pizza":
    precio2 = 8
    print ("La pizza esta recien salida del horno y cuesta 8 euros")
    print(f"Entonces como son {cantidad2} {orden2}(s) seria un total a pagar: {cantidad2 * precio2}euros"  )
elif orden2.lower() == "pasta":
    precio2= 7
    print("La pasta nuestra especialidad y cuesta 7 euros")
    print(f"Entonces como son {cantidad2} {orden2}(s) seria un total a pagar: {cantidad2 * precio2}euros"  )
elif orden2.lower() == "hamburguesa":
    precio2 = 9
    print("La hamburguesa con queso y papas fritas cuesta 9 euros")
    print(f"Entonces como son {cantidad2} {orden2}(s) seria un total a pagar: {cantidad2 * precio2}euros"  )
else:
    print("Lo siento, no esta en el menu") 
   
    precio2 = 0
    cantidad2 = 0

total1 = cantidad1 * precio1
total2 = cantidad2 * precio2
total_general = total1 + total2

print("\nResumen de tu pedido:")
if cantidad1 > 0:
    print(f"- {cantidad1} {orden1}(s)")
if cantidad2 > 0:
    print(f"- {cantidad2} {orden2}(s)")

print("Total a pagar:", total_general, "EUROS. ¡Gracias por tu compra!")

if (cantidad1 + cantidad2) >= 5:
    print("Tienes una bebida gratis por tu pedido") 
else:
    print("vuelve pronto")