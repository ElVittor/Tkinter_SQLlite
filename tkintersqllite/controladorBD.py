from tkinter import messagebox
import sqlite3
import bcrypt #biblioteca para encriptar

class controladorBD:
    def __init__(self):
        pass
    def conexionBD(self):#Primer metodo para establecer conexión
        try:
            conexion=sqlite3.connect("C:/Users/leon_/Documents/UPQ/5° Cuatri/PROGRMACIÓN OO/Tkinter_SQLlite/tkintersqllite/BasedeDatosUsuarios.db")#Funcion de sql lite, para conectar, usa la ruta de donde esta el archivo físico
            print("Conectado a BD")
            return conexion#para poder conectar la base datos osea conexion carga la conexion
        except sqlite3.OperationalError:#Para pedir que continue a pesar de errores
            print("No se pudo Conectar")
    def guardarusuario(self,nom,cor,con):#Metodo para guardar usuario, usa self por el encapsulado y las variables que vamos a requerir para trabajar
        #El primer paso es mandar a llamar la conexión, guardandola en una variable llamada  conx
        conx=self.conexionBD()
        #2 paso, validar vacios en la informacion a guardar
        if(nom=="" or cor=="" or con==""):
            messagebox.showwarning("Cuidado","Formulario incompleto")
            conx.close()#cierra la conexion evita errores, siempre que se abre, se vuelve a cerrar despues de usar
        else:#Ahora si realizamos el inser a la base de datos
            cursor=conx.cursor()#es la que le va a permitir ejecutar acciones a la base datos(insert), por tanto debe tner conexion a BD y usar un objeto Cursor
            #crear una lista para evitar errores de sintxis con los para metros que insertaremos
            conh=self.encriptarcontraseña(con)#usamos self porque es un metodo de la clase, con esto encriptamos la contraseña en con, es decir el return conha se guarda en con
            datos=(nom,cor,conh)#Usamos el conh para guaradar la contraseña encriptada
            #creamos la sintaxis sql para hacer el insert(lenguaje de sql).
            sqlinsert="insert into tbRegistrados(Nombre,Correo,Contraseña) values(?,?,?)"#El signo es para decir que es pendiente el parametro porqe va por el cursor
            #5 ejecutar insert
            cursor.execute(sqlinsert,datos)#le pedimos al cursor ejecutar el insert con los datos guardados en la variable datos(antes definida)
            conx.commit()#Esta funcion se usa para guardar la informacion en la base datos, la informacion proporcionadapor el cursor
            conx.close
            messagebox.showinfo("Exito","Usuario guardado")
    #Creamos metodo para encriptar
    def encriptarcontraseña(self,con):#ocupa la contraseña para encriptar
        #contraseña plana es la contraseña sin encriptar y la guardamos en una variable
        conplana=con
        #pasamos la contraseña guardada en conplana a bytes usando el encode
        conplana=conplana.encode()
        #sal(es una varibal que puedo cambiar 'sal' permite que la contraseña sea lo más aleatora posible y la vamos a usar con la funcion bcrypt y usamos gensalt
        sal=bcrypt.gensalt()
        #ahora guardamos la contraseña encriptada en una variable nueva, usamos bcript, usamos la funcion hashpw mas la contraseña original y sal que es la seguridad a usar
        conha=bcrypt.hashpw(conplana,sal)
        print(conha)
        #regresamos la contraseña encriptada
        return conha