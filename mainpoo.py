from cosas import alumno

def main():
    """
    al1= alumno()
    print(al1)
    al2= alumno()
    print(al1.facultad)
    print(al2.facultad)
    print(alumno.facultad)
    #Ojo
    print("__________")
    al1.facultad="FES Aragón EDOMEX"
    print(al1.facultad)
    print(al2.facultad)
    print(alumno.facultad)
    print("---Un vistazo a los objetos")
    print(vars(al1))
    print(vars(al2))
    print("-----Modificar atributos publicos")
    al1.edad=999
    print(vars(al1))
    print(vars(al2))
    """
    al1= alumno("Pedro", 21, "ICO")
    al2= alumno("José", 20, "Derecho")
    print(vars(al1))
    al1.__edad= 333
    print(al1.__edad)
    print(vars(al1))

main()