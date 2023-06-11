dinero_enero = input("¿Cual es el dinero recibido en Enero?: ")
dinero_febrero = input("¿Cual es el dinero recibido en Febrero?: ")
dinero_marzo = input("¿Cual es el dinero recibido en Marzo?: ")

dinero_enero = int(dinero_enero)
dinero_febrero = int(dinero_febrero)
dinero_marzo = int(dinero_marzo)
presupuesto = (dinero_enero + dinero_febrero + dinero_marzo) / 3

print(f"El presupuesto es: ${presupuesto}")