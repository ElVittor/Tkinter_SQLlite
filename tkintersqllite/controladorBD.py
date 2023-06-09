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
    
        #Controlador de la  busqueda de usuario
        
    def consultarUsuario(self,id):
            #1 realizar conxión
        conx=self.conexionBD() #Para acceder a la funcion conexion
            #Verificar que ID no sea Vacio
        if(id==""):
                messagebox.showwarning("Cuidado","Escribe un Identificdor")
                conx.close()
        else:
                #3 ejecutar la consulta
            try:
                    #4Preparamos lo necesario
                cursor=conx.cursor()
                sqlSelect="Select* from tbRegistrados where id = "+id
                    #5 Ejecutamos y cerramos conexion
                cursor.execute(sqlSelect)#Ejecuta sqlSelecct
                RSusuario=cursor.fetchall()#result set o variable para guardar la información de la consulta, lo que tenga cursor lo pasamos a la variabale para seso sirve la funcion cursor.fetchall()
                conx.close()
                return RSusuario
            except sqlite3.OperationalError:
                print("Error de Consulta")
                
                
    def consultartodoslosusuarios(self):
            #1 realizar conxión
        conx=self.conexionBD() #Para acceder a la funcion conexion
            #Verificar que ID no sea Vacio
        if(id==""):
                messagebox.showwarning("Cuidado","Escribe un Identificdor")
                conx.close()
        else:
                #3 ejecutar la consulta
            try:
                    #4Preparamos lo necesario
                cursor=conx.cursor()
                sqlSelect="Select * from tbRegistrados;"
                    #5 Ejecutamos y cerramos conexion
                cursor.execute(sqlSelect)#Ejecuta sqlSelecct
                RSusuario=cursor.fetchall()#result set o variable para guardar la información de la consulta, lo que tenga cursor lo pasamos a la variabale para seso sirve la funcion cursor.fetchall()
                conx.close()
                return RSusuario
            except sqlite3.OperationalError:
                print("Error de Consulta")
                
                
    def editarusuario(self,id,nom,cor,con):
        #1 realizar conxión, y establecer cursor y accion
        conx=self.conexionBD() #Para acceder a la funcion conexion
        cursor=conx.cursor()
        sqlEdit="update tbRegistrados set Nombre=?,Correo=?,Contraseña=? where id=?"
        if(nom=="" or cor=="" or con=="" or id==""):
            messagebox.showwarning("Cuidado","Formulario incompleto")
            conx.close()#cierra la conexion evita errores, siempre que se abre, se vuelve a cerrar despues de usar
        else:#Ahora si realizamos el inser a la base de datos
            try:
                #crear una lista para evitar errores de sintxis con los para metros que insertaremos
                conh=self.encriptarcontraseña(con)#usamos self porque es un metodo de la clase, con esto encriptamos la contraseña en con, es decir el return conha se guarda en con
                datose=(nom,cor,conh,id)#Usamos el conh para guaradar la contraseña encriptada
                #creamos la sintaxis sql para hacer el insert(lenguaje de sql).
                #5 ejecutar insert
                cursor.execute(sqlEdit,datose)#le pedimos al cursor ejecutar el insert con los datos guardados en la variable datos(antes definida)
                conx.commit()#Esta funcion se usa para guardar la informacion en la base datos, la informacion proporcionadapor el cursor
                conx.close
                messagebox.showinfo("Exito","Usuario guardado")
            except sqlite3.OperationalError:
                print("Error de Actualizacion")
                messagebox.showwarning("Cuidado","Error de Actualizacion")
            
    
    def eliminarusuario(self,id):
        pass
        conx=self.conexionBD() #Para acceder a la funcion conexion
        cursor=conx.cursor()
        sqldelete="DELETE FROM tbRegistrados WHERE ID=?"
        
        if(id==""):
                messagebox.showwarning("Cuidado","Escribe un Identificdor")
                conx.close()
        else:
                #3 ejecutar la consulta
            try:
                    #4Preparamos lo necesario
                cursor.execute(sqldelete,id)#Ejecuta sqlSelecct
                conx.commit()
                conx.close()
                messagebox.showinfo("Correcto","Usuario Eliminado")
            except sqlite3.OperationalError:
                print("Error de Consulta")