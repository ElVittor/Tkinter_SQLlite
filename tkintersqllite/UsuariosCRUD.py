from tkinter import *
from tkinter import ttk
import tkinter as tk
#despues de crear los metodos de controladorBD hacemos lo siguiente
from controladorBD import *
#Para poder conectar con controladorBD vamos a crear una instancia(puente entre los 2 archivos)
#creamos el objeto controlador , para la clase controladorBD
controlador=controladorBD()#de manera que controlador el la instancia o puente entre las 2 ventanas
#Creamos 8un metodo para poder ejecutar el insert

def ejecutainsert():#Este es el que vamos a ejecutar como comand
    #como la variable var.... tiene un string, eso no lo pude manejar la base de datos, extraemos los datos usando un get
    controlador.guardarusuario(varNom.get(),varCor.get(),varCon.get())#usamos el objeto/instancia controlador para ejecutar guardar ususario, y le pasamos las variables tomadas del entry de cada una
    #como es un metodo de guardar, no regresa nada

def ejecutaSelectU():
    rsUsu=controlador.consultarUsuario(varBus.get())
    #Itermos el contenido de la cosulta y lo guardamos
    for usu in rsUsu:
        cadena=str(usu[0])+" "+usu[1]+" "+usu[2]+" "+str(usu[3])#Tomamos lo elementos de Rsusu y los iteremoas para crear la cadena y lo pnemos en cadena, convertimos a str las que lo requiern 
        
    #para ver si existe e usuario
    if(rsUsu):#aqui esta funcionando con true y false, si tiene algo va, si no va al else
        print(cadena)#Esto es tarea para buscar como agregar esta informacion tambien en el cuadro de texto
        textBus.config(state="normal")#para habilitar la entrada de texto en el cuadro de texto
        textBus.delete(1.0,"end") #Limpia el contenido del cuadro de texto
        textBus.insert("end",cadena)#inserta el contenido de cadena en el cuadro de texto
        textBus.config(state="disabled")#desactiva la entra de texto en el cuadro de texto
    else:
        messagebox.showinfo("No encontrado","Usuario NO existe en Base de Datos")

def ejecutaconsultausuarios():
    
    RSConUsu=controlador.consultartodoslosusuarios()
    tabla.delete(*tabla.get_children())#limpia la tabla
    for usu in RSConUsu:
        tabla.insert("","end",text=usu[0],values=(usu[1],usu[2],usu[3])) #Tomamos lo elementos de Rsusu y los iteremoas para crear la cadena y lo pnemos en cadena, convertimos a str las que lo requiern 
            
       
def ejecutaactualizarusuario():
    RespYesNo=messagebox.askyesno("Actualizar","Desea actualizar el siguiente usuario:"+"\nID: "+str(varID2)+"\nNombre: "+str(varNom2)+"\nCorreo: "+str(varCor2))
    print(varID2,varNom2,varCor2,varCon2)
    if RespYesNo==True:
        controlador.editarusuario(varID2.get(),varNom2.get(),varCor2.get(),varCon2.get())

    
def ejecutaeliminarusuario():
    #RespElimYN=messagebox.askyesno("Eliminar","Desea eliminar el siguiente usuario:"+"\nID: "+str(varID))
    #if(RespElimYN==True):
        controlador.eliminarusuario(varID.get())
    
#paso 1
ventana=Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")
#paso 2
panel=ttk.Notebook(ventana) #crea un panel para usar dentro de la ventana, con .pack lo vamos a ubicar dentro de la ventana
panel.pack(fill="both",expand="yes")#ocupa toda la ventana, y permite expandirse con ella
#creamos 4 pestañas / frame spara trabajar denmtro del panel
pestaña1=ttk.Frame(panel)#pestaña 1 va al panel
pestaña2=ttk.Frame(panel)#pestaña 2 va al panel
pestaña3=ttk.Frame(panel)#pestaña 3 va al panel
pestaña4=ttk.Frame(panel)#pestaña 4 va al panel
pestaña5=ttk.Frame(panel)#pestaña 5 va al panel
#Paso 4
#Formulario de registro
titulo=Label(pestaña1,text="Registro Usuarios",fg="blue",font=("Modern",18)).pack() #posicionamos un titulo en una etiqueta, en pestaña 1, con texto, color de letra, tipo de fuente y tamaño, colocandolo con el pack

varNom=tk.StringVar()#para vaciar el Entry
lblNom=Label(pestaña1,text="Nombre: ").pack()
txtNom=Entry(pestaña1,textvariable=varNom).pack() #text variable te pide la variable donde va aguardar

varCor=tk.StringVar()#para vaciar el Entry
lblCor=Label(pestaña1,text="Correo: ").pack()
txtCor=Entry(pestaña1,textvariable=varCor).pack() #text variable te pide la variable donde va aguardar

varCon=tk.StringVar()#para vaciar el Entry
lblCon=Label(pestaña1,text="Contraseña: ").pack()
txtCon=Entry(pestaña1,textvariable=varCon).pack() #text variable te pide la variable donde va aguardar

btnGuardar=Button(pestaña1,text="Guardar Usuario",command=ejecutainsert).pack()#Usamos el ejecutar insert para guardar la información

#Practica 16 buscador y txt en ventana
#pestaña 2 BUscar Usuario
titulo2=Label(pestaña2,text="Buscar Usuario",fg="green",font=("Modern",18)).pack()

varBus=tk.StringVar()
lblid=Label(pestaña2,text="Identificador de usuario").pack()
txtid=Entry(pestaña2,textvariable=varBus).pack()
btnBus=Button(pestaña2,text="Buscar:",command=ejecutaSelectU).pack()

subBus=Label(pestaña2,text="Registrado",fg="Blue",font=("Modern",15)).pack()
textBus=tk.Text(pestaña2,height=5,width=52)#al usar el .tk estamos diciendo que usamos la libreria tk, y la funcion text, que es una entrada de texto mucho mayor
textBus.pack()

#Practica 17 Ventana Consultar Usuarios

varbususu=tk.StringVar
btnbususu=Button(pestaña3,text="Consultar Usuarios",command=ejecutaconsultausuarios).pack()

subus=Label(pestaña3,text="Usuario",fg="Blue",font=("Modern",15)).pack()
tabla=ttk.Treeview(pestaña3)
tabla["columns"]=("Nombre","Correo","Contraseña")
tabla.column("#0",width=60,minwidth=60)
tabla.column("Nombre",width=100,minwidth=100)
tabla.column("Correo",width=200,minwidth=200)
tabla.column("Contraseña",width=100,minwidth=100)
tabla.heading("#0",text="ID",anchor=tk.CENTER)
tabla.heading("Nombre",text="Nombre",anchor=tk.CENTER)
tabla.heading("Correo",text="Correo",anchor=tk.CENTER)
tabla.heading("Contraseña",text="Contraseña",anchor=tk.CENTER) 
tabla.pack()

#Practica 18 Ventana Actualizar/Eliminar Usuario

titulo=Label(pestaña4,text="Edicion de Usuarios",fg="blue",font=("Modern",18)).pack() #posicionamos un titulo en una etiqueta, en pestaña 1, con texto, color de letra, tipo de fuente y tamaño, colocandolo con el pack

varID2=tk.StringVar()#para vaciar el Entry
lblID2=Label(pestaña4,text="ID Usuario a Editar: ").pack()
txtID2=Entry(pestaña4,textvariable=varID2).pack() #text variable te pide la variable donde va aguardar

varNom2=tk.StringVar()#para vaciar el Entry
lblNom2=Label(pestaña4,text="Nombre: ").pack()
txtNom2=Entry(pestaña4,textvariable=varNom2).pack() #text variable te pide la variable donde va aguardar

varCor2=tk.StringVar()#para vaciar el Entry
lblCor2=Label(pestaña4,text="Correo: ").pack()
txtCor2=Entry(pestaña4,textvariable=varCor2).pack() #text variable te pide la variable donde va aguardar

varCon2=tk.StringVar()#para vaciar el Entry
lblCon2=Label(pestaña4,text="Contraseña: ").pack()
txtCon2=Entry(pestaña4,textvariable=varCon2).pack() #text variable te pide la variable donde va aguardar
btnEditar=Button(pestaña4,text="Editar Usuario",command=ejecutaactualizarusuario).pack()#Usamos el ejecutar insert para guardar la información

#Eliminar
varID=tk.StringVar()#para vaciar el Entry
titulo=Label(pestaña5,text="Eliminar Usuario",fg="blue",font=("Modern",18)).pack() #posicionamos un titulo en una etiqueta, en pestaña 1, con texto, color de letra, tipo de fuente y tamaño, colocandolo con el pack
lbID2=Label(pestaña5,text="ID del Usuario a Eliminar: ").pack()
txtID2=Entry(pestaña5,textvariable=varID).pack()
btnEliminar=Button(pestaña5,text="Eliminar Usuario",command=ejecutaeliminarusuario).pack()#Usamos el ejecutar insert para guardar la información


#Paso 3
panel.add(pestaña1,text="Agregar Usuarios")#posiciona la pestaña y le agrega el texto
panel.add(pestaña2,text="Buscar Usuario")#posiciona la pestaña y le agrega el texto
panel.add(pestaña3,text="Consultar Usuarios")#posiciona la pestaña y le agrega el texto
panel.add(pestaña4,text="Actualizar Usuario")#posiciona la pestaña y le agrega el texto
panel.add(pestaña5,text="Eliminar Usuario")#posiciona la pestaña y le agrega el texto



ventana.mainloop()

