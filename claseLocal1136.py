print("--frida sofia apodaca cera")
class local1136:
    def __init__(self,nombre, direccion,id_local):
        self.nombre=nombre
        self.direccion=direccion
        self.id_local=id_local
        def mostrar_datos(self):
            print(f"nombre: {self.nombre}, direccion: {self.direccion}, ID_local: {self.id_local} ")
            
    def listar_empleados1136():
        print("***lista***")
        empleados=["jose alarez","maria antonella","mario vasquez","miguel dominguez",]
        print(empleados)
        for e in empleados:
            print(e)
        print("\n")
            
    def tupla_capacidad1136():
        print("***tupla***")
        capacidad=("maxima: 300","minima:50","estable:150")
        print(capacidad)
        for c in capacidad:
            print(c)
        print("\n")
        
    def diccionario_telefono1136():
        print("***diccionario***")
        telefono={
            "dueño: ","6568834567",
            "gerente: ","6563215874"
        }
        telefono={"dueño","gerente"}
        print(telefono)
        for t in telefono:
            print(t)
        print("\n")
        
# informacion datos
info=local1136("blue period","calle nueva zelanda",1136)

#mostrar todos los datos
info.mostrar_datos()
print("lista de empleados")
info.listar_empleados1136()

print("capacidad del local")
info.tupla_capacidad1136()

print("numeros telefonicos")
info.diccionario_telefono1136()