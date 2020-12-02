# IMPORTAMOS LAS LIBRERIAS --------------------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter.ttk import Treeview
from tkinter.ttk import Combobox
import os
import tkinter
import matplotlib.pyplot as plt

# GESTIONAR ESTADISTICAS ------------------------------------------------------------------------------------------------------------------------------
def gestionar_estadisticas():
    # CALCULOS
    #   HABITACIONES DISPONIBLES Y NO DISPOBNIBLES
    hab_disponible = 0
    hab_nodisp = 0
    with open("habitaciones.txt","r") as f:
        for linea in f:
            campos=linea.split(";")
            if str(campos[2])=="disponible":
                hab_disponible+=1
            else:
                hab_nodisp+=1

    #   CANTIDAD DE PASAJEROS 
    cant_pasajeros = 0
    with open("reservas.txt","r") as f:
        for linea in f:
            campos=linea.split(";")
            cant_pasajeros = cant_pasajeros + int(campos[2])

    #   CANTIDAD DE RESERVAS
    f = open("reservas.txt", "r")
    vectortotal2 = f.readlines()
    cant_reservas = len(vectortotal2)

    #   GANANCIAS DE LAS RESERVAS REGISTRADAS 
    ganancias = 0
    with open("reservas.txt","r") as f:
        for linea in f:
            campos=linea.split(";")
            ganancias = ganancias + int(campos[17])

    #  GANANCIAS ANUALES SEGÚN MES
    ganancias_anuales = [0,0,0,0,0,0,0,0,0,0,0,0]
    ganancias_totales = 0
    i = 0
    with open("ganancias.txt","r") as f:
        for linea in f:
            campos=linea.split(";")
            ganancias_anuales[i] = int(campos[1])
            ganancias_totales = ganancias_totales + int(campos[1])
            i +=1


    # INTERFAZ
    pantalla_estadisticas = Tk()
    pantalla_estadisticas.title("GESTION DE ESTADISTICAS")
    pantalla_estadisticas.geometry("400x320")
    pantalla_estadisticas.resizable(width = 'False', height = 'False')

    def volver2(): # funcion para volver el menu principal
        pantalla_estadisticas.destroy()
        menu_principal()
    
    btnvolver2 = Button(pantalla_estadisticas,text="Volver",command=volver2).place(x=330,y=278)


    #   contenido primer recuadro
    recuadro_est_hab= tkinter.LabelFrame(pantalla_estadisticas, padx=15, pady=10, text="HABITACIONES")
    recuadro_est_hab.pack(padx=10, pady=10)
    lblesthab1 = Label(recuadro_est_hab,text="Habitaciones Disponibles       ").grid(row=0,column=0)
    lblesthab11 = Label(recuadro_est_hab,text=hab_disponible).grid(row=0,column=2)
    lblesthab2 = Label(recuadro_est_hab,text="Habitaciones No Disponibles").grid(row=1,column=0)
    lblesthab22 = Label(recuadro_est_hab,text=hab_nodisp).grid(row=1,column=2)
    
    def grafica1(): # funcion que genera la grafica  de torta
        from matplotlib import pyplot as plt 
        import numpy as np 
        aaa = ['Habitaciones disponibles', 'Habitaciones No Disponibles']
        data = [int(hab_disponible), int(hab_nodisp)]
        fig = plt.figure(figsize =(10, 7)) 
        plt.pie(data, labels = aaa)  
        plt.show()
    
    btnesthab = Button(recuadro_est_hab,text="Ver Gráfica", command=grafica1).grid(row=2,column=4)
    
    
    #   contenido segundo recuadro
    recuadro_est_res= tkinter.LabelFrame(pantalla_estadisticas, padx=15, pady=10, text="RESERVAS")
    recuadro_est_res.pack(padx=10, pady=10)
    lblesthab3 = Label(recuadro_est_res,text="Cantidad de Pasajeros   ").grid(row=0,column=0)
    lblesthab33 = Label(recuadro_est_res,text=cant_pasajeros).grid(row=0,column=2)
    lblesthab4 = Label(recuadro_est_res,text="Cantidad de Reservas  ").grid(row=1,column=0)
    lblesthab44 = Label(recuadro_est_res,text=cant_reservas).grid(row=1,column=2)
    lblesthab5 = Label(recuadro_est_res,text="Ganancias   ").grid(row=2,column=0)
    lblesthab55 = Label(recuadro_est_res,text=ganancias).grid(row=2,column=2)
    
    def grafica2(): # funcion que general el grafico lineal
        plt.plot(["ENE", "FEB", "MAR", "ABRIL","MAY","JUN", "JUL", "AGO", "SEP","OCT","NOV","DIC"],[ganancias_anuales[0],ganancias_anuales[1],ganancias_anuales[2],ganancias_anuales[3],ganancias_anuales[4],ganancias_anuales[5],ganancias_anuales[6],ganancias_anuales[7],ganancias_anuales[8],ganancias_anuales[9],ganancias_anuales[10],ganancias_anuales[11]])
        plt.suptitle("GANANCIA ANUAL: $" + str(ganancias_totales))
        plt.show()
    
    btnestres1 = Button(recuadro_est_res,text="Ver Gráfica Anual", command=grafica2).grid(row=3,column=4)
    pantalla_estadisticas.mainloop()

# GESTIONAR RESERVAS ----------------------------------------------------------------------------------------------------------------------------------
def gestionar_reservas():
    # INTERFAZ
    pantalla_reserva = Tk()
    pantalla_reserva.title("GESTION DE RESERVAS")
    pantalla_reserva.geometry("1000x400")
    pantalla_reserva.resizable(width = 'False', height = 'False')
    recuadro_reserva = tkinter.LabelFrame(pantalla_reserva, padx=15, pady=10, text="Opciones")
    recuadro_reserva.pack(padx=10, pady=10)
    recuadro_tabla_res = tkinter.LabelFrame(pantalla_reserva, padx=15, pady=10)
    recuadro_tabla_res.pack(padx=10, pady=10)

    # BOTONES-FUNCIONES
    def RegistrarReserva(): # INTERFAZ PARA REGISTRAR UNA RESERVA
        pantalla_reserva.destroy()
        win_reg_reserva = Tk()
        win_reg_reserva.title("REGISTRAR RESERVA")
        win_reg_reserva.geometry('700x500')

        #   primer recuadro con datos de la reserva
        recuadro_reserva = tkinter.LabelFrame(win_reg_reserva, padx=15, pady=10, text="Datos Reserva ")
        recuadro_reserva.pack(padx=10, pady=10)

        lblfi= Label(recuadro_reserva, text="Fecha de Ingreso ").grid(row=0)
        fi = Entry(recuadro_reserva)
        fi.grid(row=0, column=1)

        lbfe= Label(recuadro_reserva, text="Fecha de Egreso  ").grid(row=1)
        fe = Entry(recuadro_reserva)
        fe.grid(row=1, column=1)

        lblcant_pasajeros= Label(recuadro_reserva, text="Pasajeros          ").grid(row=1, column=3)
        cant_pasajeros = Entry(recuadro_reserva)
        cant_pasajeros.grid(row=1, column=4)

        lblcant_dias= Label(recuadro_reserva, text="   Cantidad de Dias ").grid(row=0, column=3)
        cant_dias = Entry(recuadro_reserva)
        cant_dias.grid(row=0, column=4)
        
        lbltemporada = Label(recuadro_reserva, text="Temporada       ").grid(row=2)
        temporada = Combobox(recuadro_reserva,width=17)
        temporada['values']= ("Temporada","-------------","Alta", "Media", "Baja")
        temporada.current(0) 
        temporada.grid(row=2, column=1)

        lblhabitaciones = Label(recuadro_reserva, text="Habitaciones    ").grid(row=2,column=3)
        habitaciones = Entry(recuadro_reserva)
        habitaciones.grid(row=2,column=4)


        #   segundo recuadro con datos del pasajero
        recuadro_pasajero = tkinter.LabelFrame(win_reg_reserva, padx=15, pady=10, text="Datos Pasajero ")
        recuadro_pasajero.pack(padx=10, pady=10) 
        
        lblnombre= Label(recuadro_pasajero, text="Nombre ").grid(row=0)
        nombre = Entry(recuadro_pasajero)
        nombre.grid(row=0, column=1)

        lblapellido= Label(recuadro_pasajero, text="  Apellido  ").grid(row=0,column=3)
        apellido = Entry(recuadro_pasajero)
        apellido.grid(row=0, column=4)

        lbldni= Label(recuadro_pasajero, text="DNI").grid(row=0,column=5)
        dni = Entry(recuadro_pasajero)
        dni.grid(row=0, column=6)
        
        lbldomicilio= Label(recuadro_pasajero, text="Domicilio ").grid(row=2)
        domicilio = Entry(recuadro_pasajero)
        domicilio.grid(row=2, column=1)
        
        lblciudad= Label(recuadro_pasajero, text="Ciudad ").grid(row=2,column=3)
        ciudad = Entry(recuadro_pasajero)
        ciudad.grid(row=2, column=4)

        lblprovincia= Label(recuadro_pasajero, text="  Provincia  ").grid(row=2,column=5)
        provincia = Entry(recuadro_pasajero)
        provincia.grid(row=2, column=6)

        lblcorreo= Label(recuadro_pasajero, text="Correo  ").grid(row=4)
        correo = Entry(recuadro_pasajero,width=51)
        correo.place(x=58,y=45)

        lbltelefono= Label(recuadro_pasajero, text="  Telefono  ").grid(row=4,column=5)
        telefono = Entry(recuadro_pasajero)
        telefono.grid(row=4, column=6)


        #   tercer recuadro con datos sobre el metodo de pago y los montos
        recuadro_metodo = tkinter.LabelFrame(win_reg_reserva, padx=15, pady=10, text="Método de Pago ")
        recuadro_metodo.pack(padx=10, pady=10) 

        lblmetodo = Label(recuadro_metodo, text="Metodo de Pago  ").grid(row=0)
        metodo = Combobox(recuadro_metodo)
        metodo['values']= ("metodo","---------","Efectivo", "Tarjeta", "Deposito")
        metodo.current(0) 
        metodo.grid(row=0, column=1)

        lbldescuento = Label(recuadro_metodo, text="Descuento  ").grid(row=1)
        descuento = Combobox(recuadro_metodo)
        descuento['values']= ("porcentajes","-------------","0","10","15","20", "25","30")
        descuento.current(0) 
        descuento.grid(row=1, column=1)

        lblestado = Label(recuadro_metodo, text="Estado  ").grid(row=2)
        estado = Combobox(recuadro_metodo)
        estado['values']= ("estado","-----------","a confirmar", "confirmada")
        estado.current(0) 
        estado.grid(row=2, column=1)

        #MONTOS
        lblmonto_total = Label(recuadro_metodo, text="  Monto Total  ").grid(row=0,column=3)
        lblmonto_total_rdo = Label(recuadro_metodo, text=" ")
        lblmonto_total_rdo.grid(row=0,column=4)
        lblmonto_seña = Label(recuadro_metodo, text="  Monto Seña  ")
        lblmonto_seña.grid(row=1,column=3)
        lblmonto_seña_rdo = Label(recuadro_metodo, text=" ")
        lblmonto_seña_rdo.grid(row=1,column=4)


        # BOTONES
        def disponibilidad(): # debería mostrar una tabla con la disponibilidad de habitaciones en el rango de fechas
            # INTERFAZ
            dispohabitaciones = Tk()
            dispohabitaciones.geometry("300x250")

            # DEFINICION DE TABLA
            tabla = Treeview(dispohabitaciones, columns=[f"#{n}" for n in range(1, 3)])
            titulo = Label(dispohabitaciones,text="Disponibilidad de Habitaciones en el rango de fechas").grid(row=0,column=1)

            tabla.grid(row=1,column=1)
            tabla.column("#0", width=80), tabla.column("#1", width=80), tabla.column("#2", width=140)
            tabla.heading("#0", text="NUMERO"), tabla.heading("#1", text="TIPO"), tabla.heading("#2", text="ESTADO")
            
            # CARGA EL ARCHIVO DE LAS HABITACIONES EN LA TABLA 
            # (utilizamos el mismo archivo ya que no sabiamos como manejar bien el tema de la disponibilidad en varias fechas)
            # VEMOS LA CANTIDAD DE REGISTROS PARA VER EL LARGO DE LA TABLA
            if not os.path.exists("habitaciones.txt"):
                f = open("habitaciones.txt","w")
                f.close()

            f = open("habitaciones.txt","r")
            cantidad = len(f.readlines())
            f.close()

            f = open("habitaciones.txt","r")
            for i in range(cantidad):
                registro = f.readline()
                campos = registro.split(";")
                tabla.insert("", i, text=campos[0], values=(campos[1], campos[2]))
            f.close()

            dispohabitaciones.mainloop()

        def guardar(): # guarda la reserva en el txt de reservas, cambiando el estado de habitaciones
            f2 = open("reservas.txt","a")

            # ESCRIBE LOS DATOS DE LA RESERVA EN EL ARCHIVO
            # DIVIDIDO EN 3 CAMPOS RESPETANDO LOS RECUADROS
            montos = calcular()
            texto1 = fi.get() + ";" + fe.get() + ";" + cant_pasajeros.get() + ";" + cant_dias.get() + ";" + temporada.get() + ";" + habitaciones.get() + ";"
            texto2 = nombre.get() + ";" +  apellido.get() + ";"  + dni.get() + ";" + domicilio.get() + ";" + ciudad.get() + ";" + provincia.get() + ";" + correo.get() + ";" + telefono.get() + ";"
            texto3 = metodo.get() + ";" + descuento.get() + ";" + estado.get() + ";" + str(montos[0]) + ";" +  str(montos[1]) + ";" 
            f2.write(texto1+texto2+texto3)
            f2.write("\n")
            f2.close()

            messagebox.showinfo("Atencion!", "La reserva ha sido registrada !")

            habitaciones_modif_estado = habitaciones.get()
            campos_hab_modificar = habitaciones_modif_estado.split("-")

            # CAMBIA EL ESTADO DE LA HABITACION, DE DISPONIBLE A OCUPADA, USANDO EL ARCHIVO AUXILIAR
            with open("habitaciones.txt","r") as f:
                for i in range(len(campos_hab_modificar)):
                    a = open("habitacionesauxiliar.txt","w")
                    for registros_hab_mod_estado in f:
                        campos_mod_reg_estado = registros_hab_mod_estado.split(";")

                        if campos_hab_modificar[i] == campos_mod_reg_estado[0]:
                            texto_modif = campos_mod_reg_estado[0] + ";"+ campos_mod_reg_estado[1] + ";" + "ocupada" + ";" + campos_mod_reg_estado[3] + ";" 
                            texto2_modif = campos_mod_reg_estado[4] + ";" + campos_mod_reg_estado[5] + ";"

                            a.write(texto_modif+texto2_modif)
                            a.write("\n")
                        else:
                            a.write(registros_hab_mod_estado)
                    a.close()
            
            #PASA DEL ARCHIVO AUXILIAR AL ORIGINAL EL CAMBIO
            with open("habitacionesauxiliar.txt","r") as f:
                a = open("habitaciones.txt","w")
                for registro in f:
                    a.write(registro)
            
            a.close()
            win_reg_reserva.destroy()
            gestionar_reservas()

        def calcular(): # calcula el monto total y la seña segun los parametros introducidos
            # DATOS NECESARIOS
            d = int(cant_dias.get())    # cantidad de dias
            t = str(temporada.get())    # la temporada
            des = int(descuento.get())  # descuento si lo hay

            # las habitaciones y sus costos segun temporada
            acu_hab = int()
            acu_hab = 0
            habitaciones_calcular = habitaciones.get()
            vect_hab = habitaciones_calcular.split("-")

            for i in range(len(vect_hab)):
                with open("habitaciones.txt","r") as f:
                    for registro in f:
                        campos = registro.split(";")
                        if vect_hab[i] == campos[0]:
                            if t=="Baja": 
                                acu_hab += int(campos[3])
                            elif t=="Media":
                                acu_hab += int(campos[4])
                            elif t=="Alta":
                                acu_hab += int(campos[5])
                            else:
                                messagebox.showinfo("Atencion!", "No se encontro la habitacion !")
            
            # CALCULOS A REALIZAR
            # monto total = cantidad de dias x las habitaciones s/ temporada - descuento
            # monto seña = monto total x 40%
            monto_total = int(d*acu_hab)
            if des!=0:
                monto_total_desc = int(monto_total-((monto_total*des)/100))
            else:
                monto_total_desc = monto_total 
            monto_seña = int((monto_total_desc*40)/100)

            lblmonto_total_rdo.configure(text=monto_total_desc)
            lblmonto_seña_rdo.configure(text=monto_seña)
            vector_montos = [monto_total_desc, monto_seña]

            return(vector_montos) # le mandamos los valores de los montos a la funcion de registrar reserva
            
        def cancelar(): # cierra la ventana y nos dirije al menu de reservas
            win_reg_reserva.destroy()
            gestionar_reservas()
        
        #BOTONES DE PANTALLA REGISTRAR HABITACIONES
        btndispohabitaciones = Button(recuadro_reserva,text="Disponibilidad", command=disponibilidad).grid(row=3,column=4)
        btncalcular = Button(recuadro_metodo,text="Calcular", command=calcular)
        btncalcular.grid(row=2,column=3)
        btnCAN = Button(win_reg_reserva, text="Cancelar", command=cancelar)
        btnCAN.place(x=500, y=420)
        btnSAV = Button(win_reg_reserva, text="Guardar", command=guardar)
        btnSAV.place(x=600, y=420)

        win_reg_reserva.mainloop()

    def ModificarReserva(): # INTERFAZ PARA MODIFICAR UNA RESERVA
        # tomamos los datos que pueden ser modificados de la reserva ya existente
        vector_borrar_res_mod = [str() for ind0 in range(8)]
        vector_borrar_res_mod[0] = str(tabla.item(tabla.selection())["text"])

        for i in range(1,8):
            vector_borrar_res_mod[i] = str(tabla.item(tabla.selection())["values"][i-1])
            if i==5:
                if len(vector_borrar_res_mod[i])==1:
                    vector_borrar_res_mod[i] = "0" + str(vector_borrar_res_mod[i])
        pantalla_reserva.destroy()

        # DEFINIMOS LA MISMA INTERFAZ QUE EN REGISTRAR RESERVAS
        # HABILITAMOS UNICAMENTE ALGUNOS CAMPOS
        # EN LA MAYORIA APARECE state = "disabled"
        win_reg_reserva = Tk()
        win_reg_reserva.title("MODIFICAR RESERVA")
        win_reg_reserva.geometry('700x500')

        # RECUADRO CON DATOS DE LA RESERVA A MODIFICAR
        recuadro_reserva = tkinter.LabelFrame(win_reg_reserva, padx=15, pady=10, text="Datos Reserva ")
        recuadro_reserva.pack(padx=10, pady=10)

        lblfi= Label(recuadro_reserva, text="Fecha de Ingreso ").grid(row=0)
        fi = Entry(recuadro_reserva)
        fi.grid(row=0, column=1)

        lbfe= Label(recuadro_reserva, text="Fecha de Egreso  ").grid(row=1)
        fe = Entry(recuadro_reserva)
        fe.grid(row=1, column=1)

        lblcant_pasajeros= Label(recuadro_reserva, text="Pasajeros          ").grid(row=1, column=3)
        cant_pasajeros = Entry(recuadro_reserva)
        cant_pasajeros.grid(row=1, column=4)

        lblcant_dias= Label(recuadro_reserva, text="   Cantidad de Dias ").grid(row=0, column=3)
        cant_dias = Entry(recuadro_reserva)
        cant_dias.grid(row=0, column=4)

        lbltemporada = Label(recuadro_reserva, text="Temporada       ").grid(row=2)
        temporada = Combobox(recuadro_reserva,width=17, state="disabled")
        temporada['values']= ("Temporada","-------------","Alta", "Media", "Baja")
        temporada.grid(row=2, column=1)

        lblhabitaciones = Label(recuadro_reserva, text="Habitaciones    ").grid(row=2,column=3)
        habitaciones = Entry(recuadro_reserva, state="disabled")
        habitaciones.grid(row=2,column=4)

        #RECAUDRO DATOS DE TITULAR DE RESERVA A MODIFICAR
        # NO SE MUESTRA NINGUN DATO
        recuadro_pasajero = tkinter.LabelFrame(win_reg_reserva, padx=15, pady=10, text="Datos Pasajero ")
        recuadro_pasajero.pack(padx=10, pady=10) 

        lblnombre= Label(recuadro_pasajero, text="Nombre ").grid(row=0)
        nombre = Entry(recuadro_pasajero, state="disabled")
        nombre.grid(row=0, column=1)

        lblapellido= Label(recuadro_pasajero, text="  Apellido  ").grid(row=0,column=3)
        apellido = Entry(recuadro_pasajero, state="disabled")
        apellido.grid(row=0, column=4)

        lbldni= Label(recuadro_pasajero, text="DNI").grid(row=0,column=5)
        dni = Entry(recuadro_pasajero, state="disabled")
        dni.grid(row=0, column=6)

        lbldomicilio= Label(recuadro_pasajero, text="Domicilio ").grid(row=2)
        domicilio = Entry(recuadro_pasajero, state="disabled")
        domicilio.grid(row=2, column=1)

        lblciudad= Label(recuadro_pasajero, text="Ciudad ").grid(row=2,column=3)
        ciudad = Entry(recuadro_pasajero, state="disabled")
        ciudad.grid(row=2, column=4)

        lblprovincia= Label(recuadro_pasajero, text="  Provincia  ").grid(row=2,column=5)
        provincia = Entry(recuadro_pasajero, state="disabled")
        provincia.grid(row=2, column=6)

        lblcorreo= Label(recuadro_pasajero, text="Correo  ").grid(row=4)
        correo = Entry(recuadro_pasajero,width=51, state="disabled")
        correo.place(x=58,y=45)

        lbltelefono= Label(recuadro_pasajero, text="  Telefono  ").grid(row=4,column=5)
        telefono = Entry(recuadro_pasajero, state="disabled")
        telefono.grid(row=4, column=6)


        # RECUADRO METODO DE PAGO
        # NO SE MUESTRA NINGUN DATO
        recuadro_metodo = tkinter.LabelFrame(win_reg_reserva, padx=15, pady=10, text="Método de Pago ")
        recuadro_metodo.pack(padx=10, pady=10) 

        lblmetodo = Label(recuadro_metodo, text="Metodo de Pago  ").grid(row=0)
        metodo = Combobox(recuadro_metodo, state="disabled")
        metodo['values']= ("metodo","---------","Efectivo", "Tarjeta", "Deposito")
        metodo.grid(row=0, column=1)

        lbldescuento = Label(recuadro_metodo, text="Descuento  ").grid(row=1)
        descuento = Combobox(recuadro_metodo, state="disabled")
        descuento['values']= ("porcentajes","-------------","0","10","15","20", "25","30")
        descuento.grid(row=1, column=1)

        lblestado = Label(recuadro_metodo, text="Estado  ").grid(row=2)
        estado = Combobox(recuadro_metodo, state="disabled")
        estado['values']= ("estado","-----------","a confirmar", "confirmada")
        estado.grid(row=2, column=1)

        # MONTOS
        lblmonto_total = Label(recuadro_metodo, text="  Monto Total  ").grid(row=0,column=3)
        lblmonto_total_rdo = Label(recuadro_metodo, text=" ")
        lblmonto_total_rdo.grid(row=0,column=4)
        lblmonto_seña = Label(recuadro_metodo, text="  Monto Seña  ")
        lblmonto_seña.grid(row=1,column=3)
        lblmonto_seña_rdo = Label(recuadro_metodo, text=" ")
        lblmonto_seña_rdo.grid(row=1,column=4)

        # BUSCA QUE REGISTRO SE DEBE CAMBIAR
        with open("reservas.txt","r") as f:
            for registros_reservas_mod in f:
                campos_reser_mod1 = registros_reservas_mod.split(";")
                campos_res_mod_comparar1 = [campos_reser_mod1[7], campos_reser_mod1[6], campos_reser_mod1[8], campos_reser_mod1[0],
                campos_reser_mod1[1], campos_reser_mod1[5], campos_reser_mod1[16], campos_reser_mod1[17]]
                
                # CUANDO ENCUENTRA EL REGISTRO A CAMBIAR MUESTRA LOS DATOS POSIBLES DE CAMBIAR
                if campos_res_mod_comparar1 == vector_borrar_res_mod:
                    cant_dias.insert(0, campos_reser_mod1[3])
                    cant_pasajeros.insert(0, campos_reser_mod1[2])
                    fi.insert(0, campos_reser_mod1[0])
                    fe.insert(0, campos_reser_mod1[1])


        def calcular_mod_hab(): # calcula el NUEVO monto total y la seña
            with open("reservas.txt","r") as f:
                habitaciones_calcular = ""
                for registros_calc_modhab in f:
                    campos_reser_calc = registros_calc_modhab.split(";")
                    campos_res_mod_calc = [campos_reser_calc[7], campos_reser_calc[6], campos_reser_calc[8], campos_reser_calc[0],
                    campos_reser_calc[1], campos_reser_calc[5], campos_reser_calc[16], campos_reser_calc[17]]

                    # OBTIENE DEL ARCHIVO LOS DATOS DE TEMPORADA, DESCUENTO Y HABITACIONES PARA EL NUEVO CALCULO
                    if campos_res_mod_calc == vector_borrar_res_mod:
                        des = int(campos_reser_calc[15])
                        t = campos_reser_calc[4]
                        habitaciones_calcular = campos_reser_calc[5]

            # CALCULO
            d = int(cant_dias.get())
            with open("habitaciones.txt","r") as f:
                acu_hab = int()
                acu_hab = 0
                vect_hab = habitaciones_calcular.split("-")
                for registro in f:
                    for i in range(len(vect_hab)):
                        campos = registro.split(";")
                        if vect_hab[i] == campos[0]:
                            if t=="Baja": 
                                acu_hab += int(campos[3])
                            elif t=="Media":
                                acu_hab += int(campos[4])
                            elif t=="Alta":
                                acu_hab += int(campos[5])
                            else:
                                print("no se encontro la habitacioon")
            
                monto_total = int(d*acu_hab)
                if des!=0:
                    monto_total_desc = int(monto_total-((monto_total*des)/100))
                else:
                    monto_total_desc = monto_total 
            
            # MONTOS
            monto_seña = int((monto_total_desc*40)/100)
            lblmonto_total_rdo.configure(text=monto_total_desc)
            lblmonto_seña_rdo.configure(text=monto_seña)
            vector_montos = [monto_total_desc, monto_seña]
            
            return(vector_montos) # devolvemos los nuevos montos 


        def guardar_mod_hab(): # guardar la reserva ya MODIFICADA EN EL ARCHIVO AUXILIAR
            with open("reservas.txt","r") as f:
                a = open("reservasauxiliar.txt","w")
                for registros_reservas_mod in f:
                    campos_reser_mod2 = registros_reservas_mod.split(";")
                    campos_res_mod_comparar2 = [campos_reser_mod2[7], campos_reser_mod2[6], campos_reser_mod2[8], campos_reser_mod2[0],
                    campos_reser_mod2[1], campos_reser_mod2[5], campos_reser_mod2[16], campos_reser_mod2[17]]

                    if campos_res_mod_comparar2 != vector_borrar_res_mod:
                        a.write(registros_reservas_mod)
                    else:
                        montos = calcular_mod_hab()
                        
                        texto1 = fi.get() + ";" + fe.get() + ";" + cant_pasajeros.get() + ";" + cant_dias.get() + ";" 
                        texto2 = campos_reser_mod2[4] + ";" + campos_reser_mod2[5] + ";" + campos_reser_mod2[6] + ";" + campos_reser_mod2[7] + ";" 
                        texto3 = campos_reser_mod2[8] + ";" +campos_reser_mod2[9] + ";" +campos_reser_mod2[10] + ";" +campos_reser_mod2[11] + ";" 
                        texto4 = campos_reser_mod2[12] + ";" +campos_reser_mod2[13] + ";" +campos_reser_mod2[14] + ";" +campos_reser_mod2[15] + ";"+ campos_reser_mod2[16] + ";" 
                        texto5 = str(montos[0]) + ";" +  str(montos[1]) + ";"
                        
                        a.write(texto1+texto2+texto3+texto4+texto5)
                        a.write("\n")
                a.close()
                
                # PASA DEL ARCHIVO AUXILIAR AL ORIGINAL
                with open("reservasauxiliar.txt","r") as f:
                    a = open("reservas.txt","w")
                    for registros_modificados_res in f:
                        a.write(registros_modificados_res)
                a.close()
                
                messagebox.showinfo("Atencion!", "La reserva ha sido modificada !")
                win_reg_reserva.destroy()
                gestionar_reservas()
        
        def cancelar_mod_hab():
            win_reg_reserva.destroy()
            gestionar_reservas()
            
        # BOTONES PANTALLA MODIFICAR HABITACION
        btnCAN_mod_hab = Button(win_reg_reserva, text="Cancelar", command=cancelar_mod_hab)
        btnCAN_mod_hab.place(x=500, y=420)
        btnSAV_mod_hab = Button(win_reg_reserva, text="Guardar", command=guardar_mod_hab)
        btnSAV_mod_hab.place(x=600, y=420)
        btncalcular_mod_hab = Button(recuadro_metodo,text="Calcular", command=calcular_mod_hab)
        btncalcular_mod_hab.grid(row=2,column=3)
    

    def EliminarReserva(): # FUNCION QUE ELIMINAR UNA RESERVA
        # TOMA LOS VALORES A BORRAR DE LA TABLA
        vector_borrar = [str() for ind0 in range(8)]
        vector_borrar[0] = str(tabla.item(tabla.selection())["text"])
        for i in range(1,8):
            vector_borrar[i] = str(tabla.item(tabla.selection())["values"][i-1])
            if i==5:
                if len(vector_borrar[i])==1:
                    vector_borrar[i] = "0" + str(vector_borrar[i])
        
        x = tabla.selection()[0]
        tabla.delete(x)
        
        # PASA AL ARCHIVO AUXILIAR TODOS LOS REGISTROS MENOS EL QUE SE QUIERE BORRAR
        with open("reservas.txt","r") as f:
            a = open("auxiliarreservas.txt","w")
            for registro in f:
                if registro != "":
                    campos = registro.split(";")
                    campos_comparar = [campos[7],campos[6],campos[8],campos[0],campos[1],campos[5],campos[16], campos[17]]
                    if campos_comparar != vector_borrar:
                        a.write(registro)
            a.close()
        
        # SE PASA DEL ARCHIVO AUXILIAR AL ORIGINAL
        with open("auxiliarreservas.txt","r") as f:
            a = open("reservas.txt","w")
            for registro in f:
                a.write(registro)
            a.close()
        
        habitaciones_modif_estado = vector_borrar[5]

        # CAMBIA EL ESTADO DE LA HABITACION DE OCUPADA A DISPONIBLE CON EL ARCHIVO AUXILIAR
        with open("habitaciones.txt","r") as f:
            campos_hab_mod = habitaciones_modif_estado.split("-")
            for i in range(len(campos_hab_mod)):
                a = open("habitacionesauxiliar.txt","w")
                for registros_hab_mod_estado in f:
                    campos_hab_reg_mod = registros_hab_mod_estado.split(";")
                    if campos_hab_mod[i] == campos_hab_reg_mod[0]:
                        texto_modif = campos_hab_reg_mod[0] + ";"+ campos_hab_reg_mod[1] + ";" + "disponible" + ";" + campos_hab_reg_mod[3] + ";" 
                        texto2_modif = campos_hab_reg_mod[4] + ";" + campos_hab_reg_mod[5] + ";"
                        
                        a.write(texto_modif+texto2_modif)
                        a.write("\n")
                    else:
                        a.write(registros_hab_mod_estado)
                a.close()
        
        #PASA DE ARCHIVO AUXILIAR A ORIGINAL
        with open("habitacionesauxiliar.txt","r") as f:
            a = open("habitaciones.txt","w")
            for registro in f:
                a.write(registro)
            a.close()

    def volver_f_reservas(): # FUNCION QUE NOS DEVUELVE AL MENU PRINCIPAL
        pantalla_reserva.destroy()
        menu_principal()

    # BOTONES PANTALLA RESERVA
    btn_registrar_reserva = Button(recuadro_reserva, text="Registrar",command=RegistrarReserva)
    btn_registrar_reserva.grid(row=0, column=0)
    btn_modificar_reserva = Button(recuadro_reserva, text="Modificar", command=ModificarReserva)
    btn_modificar_reserva.grid(row=0, column=1)
    btn_eliminar_reserva = Button(recuadro_reserva, text="Eliminar", command=EliminarReserva)
    btn_eliminar_reserva.grid(row=0, column=2)
    btn_volver_fr = Button(pantalla_reserva, text="Volver", command=volver_f_reservas)
    btn_volver_fr.place(x=935,y=360)

    # TABLA CON EL ARCHIVO DE RESERVAS
    tabla = Treeview(recuadro_tabla_res, columns=[f"#{n}" for n in range(1, 8)]) #1 a 9 son las columnas
    tabla.grid(row=0,column=1)
    tabla.column("#0", width=100), tabla.column("#1", width=100), tabla.column("#2", width=100)
    tabla.column("#3", width=100), tabla.column("#4", width=130), tabla.column("#5", width=130)
    tabla.column("#6", width=130), tabla.column("#7", width=130)
    tabla.heading("#0", text="APELLIDO"), tabla.heading("#1", text="NOMBRE"), tabla.heading("#2", text="DNI")
    tabla.heading("#3", text="FECHA INGRESO"), tabla.heading("#4", text="FECHA EGRESO"), tabla.heading("#5", text="HABITACIONES")
    tabla.heading("#6", text="ESTADO"), tabla.heading("#7", text="MONTO TOTAL")

    #   barra scroll de la misma
    verscrlbar2 = Scrollbar(recuadro_tabla_res, orient ="vertical", command = tabla.yview) 
    verscrlbar2.grid(row=0) 

    #   CARGAMOS LA TABLA
    with open("reservas.txt", "r") as f:
        for linea in f:
            campos = linea.split(";")
            tabla.insert("", 0, text=campos[7],
                        values=(campos[6], campos[8], campos[0], campos[1], campos[5],campos[16], campos[17]))

    pantalla_reserva.mainloop()

# GESTIONAR HABITACIONES ------------------------------------------------------------------------------------------------------------------------------
def gestionar_habitaciones():
    # INTERFAZ
    pantalla_habitaciones = Tk()
    pantalla_habitaciones.title("GESTION DE HABITACIONES")
    pantalla_habitaciones.geometry('400x400')
    pantalla_habitaciones.resizable(width = 'False', height = 'False')
    recuadro_habitaciones = tkinter.LabelFrame(pantalla_habitaciones, padx=15, pady=10, text="Opciones")
    recuadro_habitaciones.pack(padx=10, pady=10)
    recuadro_estado = tkinter.LabelFrame(pantalla_habitaciones, padx=15, pady=10, text="Estado de las Habitaciones")
    recuadro_estado.pack(padx=10, pady=10)

    # BOTONES
    def registrar_habitacion(): # INTERFAZ REGISTRAR HABITACION
        pantalla_habitaciones.destroy()
        
        reg_habitaciones = Tk()
        reg_habitaciones.title("REGISTRAR HABITACION")
        reg_habitaciones.geometry('600x150')
        reg_habitaciones.resizable(width = 'False', height = 'False')


        # RECUADRO CON TODAS LAS ENTRADAS DE DATOS 
        recuadro = tkinter.LabelFrame(reg_habitaciones, padx=15, pady=10)
        recuadro.pack(padx=10, pady=10)

        lblnro = Label(recuadro, text= "Numero    ").grid(row=0)
        nro = Entry(recuadro,width=5)
        nro.grid(row=0, column=1)
        
        lbltipo = Label(recuadro, text="  Tipo  ").grid(row=0,column=2)
        tipo = Combobox(recuadro,width=15)
        tipo['values']= ("tipo","----------","simple", "doble", "triple","suite","depto.4","depto.5")
        tipo.current(0) 
        tipo.grid(row=0, column=3)
        
        lblestado = Label(recuadro,text="  Estado  ").grid(row=0, column=4)
        estado = Combobox(recuadro,width=15)
        estado['values']= ("estado","----------","disponible","ocupado", "mantenimiento")
        estado.current(0) 
        estado.grid(row=0, column=5)
        
        # COSTO TEMPORADA BAJA-MEDIA-ALTA
        lblcosto = Label(recuadro,text="Costo por ").grid(row=2)
        lblcosto2 = Label(recuadro,text="temporada").grid(row=3)
        lblbaja = Label(recuadro, text="Baja").grid(row=2,column=2)
        baja = Entry(recuadro, width=15)
        baja.grid(row=3,column=2)
        lblmedia = Label(recuadro, text="Media").grid(row=2,column=3)
        media = Entry(recuadro, width=15)
        media.grid(row=3,column=3)
        lblalta = Label(recuadro, text="Alta").grid(row=2,column=4)
        alta = Entry(recuadro, width=15)
        alta.grid(row=3,column=4)
        
        
        # BOTONES 
        def cancelar(): # nos devuelve a la ventana de habitaciones
            reg_habitaciones.destroy()
            gestionar_habitaciones()
        
        def guardar(): # registra en el archivo, los datos de la nueva habitacion
            f2 = open("habitaciones.txt","a")
            texto = nro.get() + ";" + tipo.get() + ";" + estado.get() + ";" + baja.get() + ";" + media.get() + ";" + alta.get() + ";"
            f2.write(texto)
            f2.write("\n")
            f2.close()
            messagebox.showinfo("Atencion!", "La habitacion ha sido registrada !")
            reg_habitaciones.destroy()
            gestionar_habitaciones()
        
        # BOTONES PANTALLA REGISTRAR HABITACION
        btn1 = Button(reg_habitaciones, text="Cancelar",command=cancelar)
        btn1.place(x=340,y=110)
        
        btn2 = Button(reg_habitaciones,text="Guardar",command=guardar)
        btn2.place(x=440,y=110)
        
        #MANTIENE LA PANTALLA Y VUEVE A HABITACIONES
        reg_habitaciones.mainloop()
        gestionar_habitaciones()

    def modificar_habitacion():  # INTERFAZ PARA MODIFICAR UNA HABITACION
        vector_hab_modificar = [str() for ind0 in range(3)]
        vector_hab_modificar[0] = str(tabla_hab.item(tabla_hab.selection())["text"])
        vector_hab_modificar[1] = str(tabla_hab.item(tabla_hab.selection())["values"][0])
        vector_hab_modificar[2] = str(tabla_hab.item(tabla_hab.selection())["values"][1])
        
        pantalla_habitaciones.destroy()

        # PANTALLA DE REGISTRAR RESERVAS
        reg_habitaciones = Tk()
        reg_habitaciones.title("MODIFICAR HABITACION")
        reg_habitaciones.geometry('600x150')
        reg_habitaciones.resizable(width = 'False', height = 'False')

        # RECUADRO CON TODAS LAS ENTRADAS DE DATOS 
        recuadro = tkinter.LabelFrame(reg_habitaciones, padx=15, pady=10)
        recuadro.pack(padx=10, pady=10)
        
        lblnro = Label(recuadro, text= "Numero    ").grid(row=0)
        nro = Entry(recuadro,width=5)
        nro.grid(row=0, column=1)

        lbltipo = Label(recuadro, text="  Tipo  ").grid(row=0,column=2)
        tipo = Combobox(recuadro,width=15)
        tipo['values']= ("tipo","----------","simple", "doble", "triple","suite","depto.4","depto.5")
        tipo.grid(row=0, column=3)
        
        lblestado = Label(recuadro,text="  Estado  ").grid(row=0, column=4)
        estado = Combobox(recuadro,width=15)
        estado['values']= ("estado","----------","disponible","ocupado", "mantenimiento")
        estado.grid(row=0, column=5)
        
        # COSTO TEMPORADA BAJA-MEDIA-ALTA
        lblcosto = Label(recuadro,text="Costo por ").grid(row=2)
        lblcosto2 = Label(recuadro,text="temporada").grid(row=3)
        lblbaja = Label(recuadro, text="Baja").grid(row=2,column=2)
        baja = Entry(recuadro, width=15)
        baja.grid(row=3,column=2)
        lblmedia = Label(recuadro, text="Media").grid(row=2,column=3)
        media = Entry(recuadro, width=15)
        media.grid(row=3,column=3)
        lblalta = Label(recuadro, text="Alta").grid(row=2,column=4)
        alta = Entry(recuadro, width=15)
        alta.grid(row=3,column=4)
        

        vector_habmod_comparar = [str() for ind3 in range(3)]

        with open("habitaciones.txt","r") as f: 
            for registro_hab in f:
                campos_habmod = registro_hab.split(";")
                campos_habmod_comparar = [campos_habmod[0],campos_habmod[1], campos_habmod[2]]

                if campos_habmod_comparar == vector_hab_modificar: # MUESTRA LOS DATOS QUE SE PUEDEN CAMBIAR
                    nro.insert(0,str(campos_habmod[0]))
                    tipo.insert(0,str(campos_habmod[1]))
                    estado.insert(0,str(campos_habmod[2]))
                    baja.insert(0,str(campos_habmod[3]))
                    media.insert(0,str(campos_habmod[4]))
                    alta.insert(0,str(campos_habmod[5]))      
        
        def guardar_modificacion_hab(): # GUARDA LOS NUEVOS CAMBIOS

            vector_habmod_comparar = [str() for ind3 in range(3)]

            with open("habitaciones.txt","r") as f:
                a = open("habitacionesauxiliar.txt","w")
                for registro_hab in f:
                    campos_habmod = registro_hab.split(";")
                    campos_habmod_comparar = [campos_habmod[0],campos_habmod[1], campos_habmod[2]]

                    if campos_habmod_comparar != vector_hab_modificar: # SI ES DIFERENTE, GUARDA EL REGISTRO COMO ESTABA
                        a.write(registro_hab)
                    else: # SI ES EL REGISTRO MODIFICADO, GUARDA LOS NUEVOS CAMBIOS TOMANDO LOS ENTRY
                        texto_modificar = nro.get() + ";" + tipo.get() + ";" + estado.get() + ";" + baja.get() + ";" + media.get() + ";" + alta.get() + ";"
                        a.write(texto_modificar)
                        a.write("\n")
                a.close()
            
            with open("habitacionesauxiliar.txt","r") as f: # PASA DEL ARCHIVO AUXILIAR AL ORIGINAL
                a = open("habitaciones.txt","w")
                for registrosmodificados in f:
                    a.write(registrosmodificados)
            a.close()
            
            messagebox.showinfo("Atencion!", "La habitacion ha sido modificada !")
            reg_habitaciones.destroy()
            gestionar_habitaciones()

        def cancelar_modificacion_hab():
            reg_habitaciones.destroy()
            gestionar_habitaciones()

        # BOTONES PANTALLA MODIFICAR HABITACION
        btn1 = Button(reg_habitaciones, text="Cancelar",command=cancelar_modificacion_hab)
        btn1.place(x=340,y=110)
        btn2 = Button(reg_habitaciones,text="Guardar",command=guardar_modificacion_hab)
        btn2.place(x=440,y=110)

    def eliminar_habitacion(): # FUNCION QUE ELIMINA UNA HABITACION
        vector_borrar_habitacion = [str() for ind0 in range(3)]
        vector_borrar_habitacion[0] = str(tabla_hab.item(tabla_hab.selection())["text"])
        vector_borrar_habitacion[1] = str(tabla_hab.item(tabla_hab.selection())["values"][0])
        vector_borrar_habitacion[2] = str(tabla_hab.item(tabla_hab.selection())["values"][1])

        vector_comparar_habitaciones = [str() for ind1 in range(3)]

        with open("habitaciones.txt","r") as f:
            a = open("habitacionesauxiliar.txt","w")
            for registro_hab in f:
                campos_habitacion = registro_hab.split(";")
                campos_habitacion_comparar = [campos_habitacion[0],campos_habitacion[1],campos_habitacion[2]]

                # SI EL REGISTRO ES DIFERENTE AL QUE QUEREMOS ELIMINAR
                # LO PASA AL ARCHIVO AUXILIAR
                # (COPIA TODOS LOS ARCHIVOS MENOS EL QUE ELIMINA)
                if campos_habitacion_comparar != vector_borrar_habitacion:
                    a.write(registro_hab)
            a.close()
        
        with open("habitacionesauxiliar.txt","r") as f: # PASA LOS REGISTROS DEL AUXILIAR AL ORIGINAL
            a = open("habitaciones.txt","w")
            for registros_habaux in f:
                a.write(registros_habaux)
            a.close()
        
        x = tabla_hab.selection()[0] # BORRA EL REGISTRO DE LA TABLA
        tabla_hab.delete(x)
    
    def volver():
        pantalla_habitaciones.destroy()
        menu_principal()

    #BOTONES DE LA PANTALLA HABITACION
    btn_registrar_habitacion = Button(recuadro_habitaciones, text="Registrar", width=10, command=registrar_habitacion)
    btn_registrar_habitacion.grid(row=0, column=0)
    btn_modificar_habitacion = Button(recuadro_habitaciones, text="Modificar", width=10, command= modificar_habitacion)
    btn_modificar_habitacion.grid(row=0, column=1)
    btn_eliminar_habitacion = Button(recuadro_habitaciones, text="Eliminar", width=10, command= eliminar_habitacion)
    btn_eliminar_habitacion.grid(row=0, column=2)
    btn_volver = Button(pantalla_habitaciones, text="Volver",command=volver)
    btn_volver.place(x=300,y=365)

    # MOSTRAMOS EL ARCHIVO DE ESTADO DE HABITACIONES EN UN TABLA
    tabla_hab = Treeview(recuadro_estado, columns=[f"#{n}" for n in range(1, 3)]) #1 a 3 son las columnas
    tabla_hab.grid(row=0,column=1)
    tabla_hab.column("#0", width=80), tabla_hab.column("#1", width=80), tabla_hab.column("#2", width=140)
    tabla_hab.heading("#0", text="NUMERO"), tabla_hab.heading("#1", text="TIPO"), tabla_hab.heading("#2", text="ESTADO")

    #   agregamos una barra scroll
    verscrlbar = Scrollbar(recuadro_estado, orient ="vertical", command = tabla_hab.yview) 
    verscrlbar.grid(row=0)

    #   cargamos el archivo a la tabla
    # VEMOS CUANTOS REGISTROS HAY PARA VER LA LONGITUD DE LA TABLA
    if not os.path.exists("habitaciones.txt"):
        f = open("habitaciones.txt","w")
        f.close()
    
    f = open("habitaciones.txt","r")
    cantidad = len(f.readlines())
    f.close()

    f = open("habitaciones.txt","r")
    for i in range(cantidad):
        registro = f.readline()
        campos = registro.split(";")
        tabla_hab.insert("", i, text=campos[0], values=(campos[1], campos[2]))
    f.close()

    pantalla_habitaciones.mainloop()

# MENU PRINCIPAL --------------------------------------------------------------------------------------------------------------------------------------
def menu_principal():
    # INTERFAZ
    menu= Tk()
    menu.title("SISTEMA DE GESTION")
    menu.geometry('400x240')
    menu.resizable(width = 'False', height = 'False')

    #   TIPOGRAFIAS
    fontStyle  = tkFont.Font(family='Verdana', size=10)
    fontStyle2  = tkFont.Font(family='Verdana', size=7)
    etiqueta1=Label(menu,text="HOTEL SOL DE LAS SIERRAS", font = fontStyle)
    etiqueta1.place(x=170,y=5)

    #   BOTONES (primero las funciones y despues lo visual)
    def habitaciones(): # nos dirije a la pantalla exlusiva de habitaciones
        menu.destroy()
        gestionar_habitaciones()
        
    def reservas(): # nos dirije a la pantalla exlusiva de reservas
        menu.destroy()
        gestionar_reservas()

    def estadisticas(): # nos dirije a la pantalla exlusiva de estadisticas
        menu.destroy()
        gestionar_estadisticas()
        
    def cerrar_sesion(): # nos dirije a la pantalla de inicio de sesion
        menu.destroy()
        inicio_sesion()
    
    Button(menu,text='Habitaciones', width = 20,command=habitaciones).place(x=20,y=10)
    Button(menu,text='Reservas', width = 20,command=reservas).place(x=20,y=40)
    Button(menu,text='Estadisticas', width = 20, command=estadisticas).place(x=203,y=160)
    Button(menu,text='Cerrar Sesion', width = 20,command=cerrar_sesion).place(x=20,y=200)
    #       botones sin ninguna funcionalidad
    Button(menu,text='Compras', width = 20).place(x=20,y=70)
    Button(menu,text='Recursos Humanos', width = 20).place(x=20,y=100)
    Button(menu,text='Mantenimiento', width = 20).place(x=20,y=130)
    Button(menu,text='Marketing', width = 20).place(x=20,y=160)
    
    #   FOTO DEL LOGO DE LA EMPRESA
    img = PhotoImage(file='Logo3.png')
    imgl = Label(menu,image=img).place(x=200,y=30)
    menu.mainloop()

# INICIO DE SESION ------------------------------------------------------------------------------------------------------------------------------------
def inicio_sesion():
    # INTERFAZ
    win_inicio = Tk()
    win_inicio.title("SISTEMA DE GESTION") 
    win_inicio.geometry('350x170')
    win_inicio.resizable(width = 'False', height = 'False')
    recuadro = LabelFrame(win_inicio, text="Datos de la Cuenta",padx=20,pady=20)
    recuadro.pack(padx=10,pady=10)  

    #   INGRESO DE USUARIO 
    lblusuario = Label(recuadro, text="Usuario")
    lblusuario.grid(row=1, column=1)
    usuario = Entry(recuadro)
    usuario.grid(row=1, column=2)

    #   INGRESO DE CONTRASEÑA
    lblcontraseña = Label(recuadro, text="Contraseña     ")
    lblcontraseña.grid(row=2, column=1)
    contraseña = Entry(recuadro)
    contraseña.config(show="*")
    contraseña.grid(row=2, column=2)

    #   BOTONES ASOCIADOS (primero definimos las funciones y despues lo grafico)
    def ingresar(): # busca conicidencia entre las cuentas registradas de un archivo
        if not os.path.exists("usuarios.txt"):
            f = open("usuarios.txt","w")
            f.write("administrador;1234;\n")
            f.close() 

        f = open("usuarios.txt","r")
        usuario_verificar = usuario.get()
        contraseña_verificar = contraseña.get()
        verificar1 = False
        verificar2 = False

        for registros in f: # verifica si el usuario ingresado y la contraseña coinciden con
            campos = registros.split(";") # algun registro del archivo de usuarios
            if campos[0] == usuario_verificar: 
                verificar1 = True
            if campos[1] == contraseña_verificar:
                verificar2 = True
        f.close()

        if verificar1 == True and verificar2 == True: # en caso afirmativo, nos dirirje al menu
            win_inicio.destroy()
            menu_principal()
        else: # en caso contrario, nos hara ingresar los datos de nuevo
            usuario.delete(0,END) 
            contraseña.delete(0,END)
            messagebox.showinfo("Atencion!", "El usuario y/o la contraseña ingresados son incorrectos.")
            
    def cancelar(): # cierra el programa
        win_inicio.destroy()
    
    btnI = Button(win_inicio, text="Ingresar", command=ingresar)
    btnI.place(x=245, y=120)
    btnC = Button(win_inicio, text="Cancelar", command=cancelar)
    btnC.place(x=180, y=120)
    win_inicio.mainloop()

if __name__ == '__main__':
    inicio_sesion()
