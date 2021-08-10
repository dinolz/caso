class Pato:
    def hablar(self):
        print("cua, cua")
#para llamar al metodo es de la forma 
p = Pato()
p.hablar() 
  
def llama_hablar(x):#se define una funcion que llama al metodo hablar con cualquier objeto
    x.hablar()
p = Pato()
llama_hablar(p)
class perro:#definimos otras clases
    def hablar(self):
        print("guau, guau")
class gato:
    def hablar(self):
        print("miau, miau")
class vaca:
    def hablar(self):
        print("muu, muu")
g = gato()#se da instancia a cada objeto de cada una de las clases
v = vaca()
pe = perro()        

#la funcion llama_hablar()funciona con todos los objetos
llama_hablar(g)
llama_hablar(v)
llama_hablar(pe)
#iteramos una lista 
#tipado dinamico, animal va tomando los valores de cada objeto gato, vaca, etc.
#se crea una lista con los objetos instanciados
listaanimales = [pe, v, g]
for animal in listaanimales:
    animal.hablar()
llama_hablar(pe)
llama_hablar(g)

