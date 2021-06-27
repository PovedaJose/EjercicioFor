class Ciclos:
    def __init__ (self):
        pass

    def usoFor(self,):
        dat = ["Daniel", 50, True]
        num = (2,5.6,4,1)
        doc = {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
        lisNota = [(30,40),[20,40],(50,40)]
        lisAlum = [{"nombre":"Erick","ExmF":70},{"nombre":"Yady","ExmF":60},{"nombre":"Danny","ExmF":80}]
        
        for i in range(5):
            print("i={}".format(i), end=" ")
        for i in range(2,10,2):
            print("i={}".format(i), end=" ")
        for i in range(20,0,-4):
            print("i={}".format(i))



        long = len(dat)
        for i in range(long):
            print(dat[i], end=" ")
        for i in range(long-1,-1,-1):
            print("for", dat[i])
        for dato in num:
            print(dato)
        for dato in ['H','O','L', 'A', 'como','estas']:
            print(dato)
        print("\nDiccionario de notas")
        for clave, valor in doc.items():
            print(clave, ":", valor, end= " ")
        for alumnos in lisAlum:
            for clave, valor in alumnos.items():
                print(clave, ":", valor, end= " ")


buc1 = Ciclos()
buc1.usoFor()