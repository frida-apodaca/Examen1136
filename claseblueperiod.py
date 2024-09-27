print("*** examen frida sofia apodaca cera ***")

class papeleria1136:
    def __init__(self,nombre1136):
        self.nombre1136=nombre1136
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre1136}")
        print("\n")
        
    def diccionario_empleado1136(self):
        print(" diccionario 1")
        empleado1136={"Miguel Dominguez","Maria Antonella","kimberly Loaiza"}
        print(empleado1136)
        thisadict = {
            "ID_empleado": "1348 | 3456 | 4577",
            "Nombre": "Miguel Dominguez | Maria Antonella | Kimberly Loaiza",
            "Edad": "24 | 35 | 26",
            "curp": "MGDO140006HSJDRRA0 | MAAT240889POTTAR1 | KBLI1406702HSJDRRA3",
            "Acta_nacimiento": "14/04/2000 | 24/08/1989 | 14/06/2002",
            "sueldo": "$2300 | 2350 | 3200 ",
            "sexo": "Masculino | Femenino | Femenino"
        }
        print(thisadict)
        for e, a in thisadict.items():
            print(e,a)
            print("\n")
            
    def diccionario_cliente1136(self):
        print(" diccionario 2")
        cliente1136={"Nancy Lara","Frida Cera","Marcus Durango"}
        print(cliente1136)
        thisadict2 = {
            "ID_cliente": "3456 | 6775 | 2345",
            "Nombre": "Nancy Lara | Frida Cera | Marcus Durango",
            "Edad": "45 | 18 | 65",
            "productos": "pinturas acrilicas, pinceles punta fina | lienzos, pinturas acrilicas | cartulina",
            "historial": "bueno | malo | bueno",
            "metodo_pago": "tarjeta | efectivo | tarjeta",
            "sexo": "Femenino"
        }
        print(thisadict2)
        for c, e in thisadict2.items():
            print(c,e)
            print("\n")
            
    def diccionario_productos1136(self):
        print("diccionario 3")
        productos1136={"pinturas acrilicas","acuarelas","pinceles punta fina","set de pinceles","cartulinas"}
        print(productos1136)
        thisadict3 = {
            "ID_producto": "3456 | 5456 | 5567 | 3153 | 2395  ",
            "Nombre": "Pinturas acrilicas Fabel Castell | Acuarelas Fabel Castell | Pinceles punta fina | set de pinceles | cartulinas",
            "Tamaño": "45cm/25cm | 20cm/15cm | 15cm/15cm | 24cm/20cm | 35cm/30cm ",
            "precio": "$450 | $35 | $15 | $230 | $3",
            "calidad": "buena | buena | mala | buena | mala",
            "peso": "123g | 21g | 12g | 50g | 10g",
            "catidad": "13set | 25set | 6set | 15set | 1set"
        }
        print(thisadict3)
        for pr, d in thisadict3.items():
            print(pr,d)
            print("\n")
        
    def diccionario_proveedores1136(self):
        print(" diccionario 4")
        proveedor1136 = {"faber Castell"}
        print(proveedor1136)
        thisadict4 = {
            "ID_proveedor": "4456",
            "nombre": "faber castell",
            "productos": "pinturas, acuarelas, pinceles, colores, lapices",
            "cantidad_de_producto": "54",
            "direccion": "Calle Nueva Zelanda",
            "fecha_contratacion": "25/12/2014",
            "sueldo": "$43,000"
            }
        print(thisadict4)
        for pro, v in thisadict4.items():
            print(pro, v)
            print("\n")
            
info=papeleria1136("papeleria blue period")  

info.mostrar_datos()
print("estos son los empleados")
info.diccionario_empleado1136

print("estos son los clientes de hoy")
info.diccionario_cliente1136

print("estos son los productos")
info.diccionario_productos1136

print("estos es el proveedor")
info.diccionario_proveedores1136
