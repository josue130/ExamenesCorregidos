class canchas:
     contFactura=0#Se utiliza para contar las factura
     facturas=[]#Guardan las facturas
     validacion_canchas=100#Contador creado para que ningun contador se repitiera
     canchA=[]#En esta variable se guardarn todas las canchas con su respectivo precio e identificador
     clientes=[]#En esta variable se guardaran los clientes registrados
     validacion_reserva=0#Contador crado para el que que el identificador de la reserva no se repita
     validacion_r=[]#En esta variable se guardan la reserva con su repectiva informcvacion
     dis=[]#Variable creada para almacenar las reservaciones
     #Entradas:Recibe 4 parametros de entrada
     #Restricciones:Los parametros tienen que cumplir las validacion correspondientes de int ,str y que no sean vacias 
     #Salidas:Se establecen las entradas con variables de instancia
     def __init__(self,nombre,telefono,direccion,correo):
          
          if isinstance(nombre,str) and isinstance(telefono,int) and isinstance(direccion,str) and isinstance(correo,str):
               if nombre!=""  and telefono!="" and telefono<1000000000 and telefono>9999999 and direccion!="" and correo!="":
                    self.nombre=nombre
                    self.telefono=telefono
                    self.direccion=direccion
                    self.correo=correo
               else:
                    print("Ningun espacio puede estar vacio, y el numero tiene que ser mayor de 8 digitos")
          else:
               print("Nombre,direccion , correo son str y telefono es int")
     
    
     #Entrada:Recibe la "correspondencias" del __init__
     #Salida: Retorna un print con la informcion del contructor
     def mostrarInfo(self):
          print("Nombre",self.nombre)
          print("Telefono",self.telefono)
          print("Direccion",self.direccion)
          print("Correo",self.correo)
     #Entrada:Recibe un parametro de entrada
     #Restricciones:EL valor tiene que ser entero mayor a cero y diferente a vacio
     #Salida:La informacion recolectada es ingresa en una lista
     def crear_cancha(self,precio):
          if isinstance(precio,int) and precio >0 and precio!="":
               canchas.validacion_canchas+=1
               lista=cancha(canchas.validacion_canchas,precio)
               canchas.canchA+=[lista]
               print("identificador",canchas.validacion_canchas)
               
          else:
               return "El precio tiene que ser entero mayor a cero, el espcaio no puede estar vacio"
     #Entradas:Recibe 4 parametros de entrada
     #Restricciones:Los parametros tienen que cumplir las validacion correspondientes de int ,str y que no sean vacias 
     #Salidas:La informacion recolectada es ingresa en una lista
     def crear_cliente(self,cedula,nombre,telefono,correo):
          if isinstance(cedula,int) and isinstance(nombre,str) and isinstance(nombre,str) and isinstance(telefono,int) and isinstance(correo,str):
               if cedula!="" and cedula<10000000000 and cedula>99999999:
                    if nombre!="" and telefono!="" and telefono<1000000000 and telefono>9999999 and correo!="":
                         if canchas.clientes==[]:
                              lista=cliente(cedula,nombre,telefono,correo)
                              canchas.clientes+=[lista]
                              print("Cliente creado")
                              
                         else:
                              for i in canchas.clientes:
                                   if i.cedula==cedula:
                                        return "La cedula ya existe"
                              lista=cliente(cedula,nombre,telefono,correo)
                              canchas.clientes+=[lista]
                              print("Cliente creado")
                              
                    else:
                         return "El nombre no puede estar vacion, el numero telefonico tiene que ser mayor a 8 digitos"
               else:
                    return "Ningún espacio puede estar vacio, y la cedula tiene que ser igual a 9 digitos"
          else:
               return "La cedula tiene que ser un valor entero , el nombre un str , el telefono un valor entero, el correo un str"
     #Entradas:Recibe 3 parametros de entrada
     #Restricciones:Los parametros tienen que cumplir las validacion correspondientes de int ,str y que no sean vacias 
     #Salidas:La informacion recolectada es ingresa en una lista
     
     def modificar_cliente(self,cedula,Nuevo_telefono,Nuevo_correo):
          val=0
          if cedula=="TODOS":
               for i in canchas.clientes:
                    i.mostrar()
          else:
               
               if isinstance(cedula,int) and isinstance(Nuevo_telefono,int) and isinstance(Nuevo_correo,str):
                    if cedula!="" and cedula<10000000000 and cedula>99999999:
                         if Nuevo_telefono!=""and Nuevo_telefono<1000000000 and Nuevo_telefono>9999999 and Nuevo_correo!="":
                              for x in canchas.clientes:
                                   if x.cedula==cedula:
                                        val+=1
                                        x.telefono=Nuevo_telefono
                                        x.correo=Nuevo_correo
                              if val==0:
                                   return "NO se encotró la cedula"
                              else:
                                   return "Datos modificados correctamente"
                                   
                         else:
                              return "Ningún espacio puede estar vacio, el telefono tiene que ser de un minimo de 8 digitos"
                    else:
                         return "El espacio de la cedula no puede estar vacio, la cedula tiene que ser de un largo de 9 digitos"
               else:
                    return "La cedula tiene que ser un valor entero, el telefono tiene que ser un valor entero, el correo tiene que ser un str"
     #Entradas:Recibe 1 parametros de entrada
     #Restricciones:Los parametros tienen que cumplir las validacion correspondientes de int ,str y que no sean vacias 
     #Salidas:Dependiendo del parametro de entrda se hace un print de informcacion
     def mostrarCliente(self,cedula):
          val1=0
          if cedula!="" and cedula<10000000000 and cedula>99999999:
               if canchas.clientes==[]:
                    return "NO hay ningun cliente registrado"
               else:
                    for u in canchas.clientes:
                         if u.cedula==cedula:
                              val1+=1
                              u.mostrar()
                    if val1==0:
                         return "NO se encontro la cedula"
                         
          else:
               return "Parametro incompleto"
     #Entradas:Recibe 5 parametros de entrada
     #Restricciones:Los parametros tienen que cumplir las validacion correspondientes de int ,str y que no sean vacias 
     #Salidas:La informacion recolectada es ingresa en una lista
     def reservar_cancha(self,cedula,identificador_cancha,fecha,hora_inicio,hora_fin):
          val_cedula=0#Variable creada para validar si la cedula se encunetra existente
          val_id=0#Variable creada para validar si el identificador se encuentra existente
          val_cedula2=0#Variable creada para validar si la cedula se encunetra existente
          val_id2=0#Variable creada para validar si el identificador se encuentra existente
          if cedula!="" and cedula<10000000000 and cedula>99999999:
               
               if isinstance(identificador_cancha,int) and isinstance(fecha,str) and isinstance(hora_inicio,int) and isinstance(hora_fin,int):
                    if identificador_cancha!="" and fecha!="" and hora_inicio!="" and hora_fin!="":
                         if hora_inicio>0 and hora_inicio<=10:
                              if hora_fin>0 and hora_fin<=10:
                                   if hora_inicio!=hora_fin:
                                        if canchas.canchA==[]:
                                             return "No hay canchas registradas"
                                        if canchas.clientes==[]:
                                             return "No hay clientes registrados"
                                        if canchas.validacion_r==[]:
                                             for i in canchas.clientes:
                                                  if i.cedula==cedula:
                                                       val_cedula+=1
                                             if val_cedula==0:
                                                  return "No EXISTE esa cedula"
                                             for x in canchas.canchA:
                                                  if x.identificador==identificador_cancha:
                                                       val_id+=1
                                             if val_id==0:
                                                  return "NO existe el identificador cancha"
                                             canchas.validacion_reserva+=1
                                             lista=reserva(cedula,identificador_cancha,fecha,hora_inicio,hora_fin,canchas.validacion_reserva)
                                             canchas.validacion_r+=[lista]
                                             lista2=disponible(identificador_cancha,hora_inicio,hora_fin,canchas.validacion_reserva)
                                             canchas.dis+=[lista2]
                                             print("Su identificador de reserva es:",canchas.validacion_reserva)
                                        else:
                                             

                                             for q in canchas.clientes:
                                                  
                                                  if q.cedula==cedula:
                                                       val_cedula2+=1
                                             if val_cedula2==0:
                                                  return "No EXISTE es cedula"
                                             for ñ in canchas.canchA:
                                                  if ñ.identificador==identificador_cancha:
                                                       val_id2+=1
                                             if val_id2==0:
                                                  return "NO existe el identificador cancha"
                                             for j in canchas.dis:
                                                  if j.identificador== identificador_cancha :
                                                       if j.HoraI==hora_inicio or j.HoraF==hora_fin:
                                                            return "Esa cancha no tiene disponibilidad"
                                                       else:
                                                            if hora_inicio>j.HoraI and hora_inicio<j.HoraF:
                                                                 return "Esa cancha no tiene disponibilidad"
                                            
                                             canchas.validacion_reserva+=1
                                             lista=reserva(cedula,identificador_cancha,fecha,hora_inicio,hora_fin,canchas.validacion_reserva)
                                             canchas.validacion_r+=[lista]
                                             lista2=disponible(identificador_cancha,hora_inicio,hora_fin,canchas.validacion_reserva)
                                             canchas.dis+=[lista2]
                                             print("Su identificador de reserva es:",canchas.validacion_reserva)
                                             
                                             
                                        
                                   else:
                                        return "La hora de inicio no puede ser igual a la hora fin"
                              else:
                                   return "El horario de atencio es de 1 a 10 de la noche"
                         else:
                              return "El horario de atencio es de 1 a 10 de la noche"
                    else:
                         return "Ningún espacio puede estar vacio"
          else:
               return "La cedula no puede estar vacio y tiene que ser de 9 digitos"
     #Entradas:Recibe 1 parametros de entrada
     
     
     def quitar_reserva(self,identificador):
          val=0#Variable que muestra si el identificador existe
          new=[]#Variable donde se van a almacenar los datos no eliminados
          val2=0#Variable que muestra si el identificador existe
          if isinstance(identificador,int) and identificador!="":
               
               for i in canchas.validacion_r:
                    if i.identificador_reserva==identificador:
                         val+=1
                         continue
                    new+=[i]
               if val==0:
                    return "No esta el id"
               else:
                    canchas.validacion_r=new
                    new1=[]
                    print("Reserva eliminada")
                    for y in canchas.dis:
                         if y.reserva==identificador:
                              continue
                         new1+=[y]
                    canchas.dis=new1
                         
          else:
               return "El identificador tiene que ser un número entero diferente a vacio"
     def modificar_reserva(self,identificador_reserva,Fecha,horaI,horaF):
          if isinstance(identificador_reserva,int) and isinstance(Fecha,str) and isinstance(horaI,int) and isinstance(horaF,int) and horaI >0 and horaF>0 and horaI<=10 and horaF<=10:
               if identificador_reserva!="" and Fecha!="" and horaI!="" and horaF!="":
                    cont=0
                    for i in canchas.validacion_r:
                         if i.identificador_reserva==identificador_reserva:
                              cont+=1
                              for k in canchas.dis:
                                   if k.reserva==identificador_reserva:
                                        cancha=k.identificador
                                   
                              for j in canchas.dis:
                                   if j.identificador==cancha:
                                        if j.HoraI==horaI or j.HoraF==horaF:
                                             return "Esa cancha no tiene disponibilidad"
                                        else:
                                             if horaI>j.HoraI and horaI<j.HoraF:
                                                  return "Esa cancha no tiene disponibilidad"
                                   else:
                                        continue
                    if cont==0:
                         return "El identificador no existe"
                    else:
                         for l in canchas.validacion_r:
                              if l.identificador_reserva==identificador_reserva:
                                   l.fecha=Fecha
                                   l.hora_inicio=horaI
                                   l.hora_fin=horaF
                         print("Cambios realizados con exito")
                         for ñ in canchas.dis:
                              if ñ.reserva==identificador_reserva:
                                   ñ.HoraI=horaI
                                   ñ.HoraF=horaF
                              
                                   
                              
               else:
                    return "Ningún espacio puede estar vacio"
               
               
          else:
               return "El identificador tiene que ser entero, la fecha str, la hora de inicio y fin enteros"
          
         
     def mostrar_reserva(self,identificador):
          cont=0
          if isinstance(identificador,int) and identificador!="":
               for i in canchas.validacion_r:
                    if i.identificador_reserva==identificador:
                         cont+=1
                         for j in canchas.clientes:
                              if i .cedula==j.cedula:
                                   i.mostrar()
                                   j.mostrar()
               if cont==0:
                    return "El identificador no existe"
          else:
               return "El identificador tiene que ser entero y diferente a vacio"
     def ver_reservas(self,fecha):
          cont=0
          if isinstance(fecha,str) and fecha!="":
               for i in canchas.validacion_r:
                    if i.fecha==fecha:
                         cont+=1
                         i.mostrar()
               if cont==0:
                    return "No hay ningúna reserva en esa fecha"
          else:
               return "La fecha tiene que ser str y diferente a vacio"
     def facturar(self,identificador_reserva):
          if isinstance(identificador_reserva,int) and identificador_reserva!="":
               cont=0
               new=[]
               for i in canchas.validacion_r:
                    if i.identificador_reserva==identificador_reserva:
                         cont+=1
                         cancha=i.identificador_cancha
                         fecha=i.fecha
                         horai=i.hora_inicio
                         horaf=i.hora_fin
                         cel=i.cedula
                         continue
                    else:
                         new+=[i]
               #
               if cont==0:
                    return "No existe esa reserva"
               else:
                    for p in canchas.canchA:
                         if p.identificador==cancha:
                              precio=p.precio
                         
                    horas=0
                    for m in range(horai,horaf):
                         horas+=1
                    total=precio*horas
                    for ñ in canchas.clientes:
                         if ñ.cedula==cel:
                              cliente=ñ.nombre
                    new1=[]
                    for a in canchas.dis:
                         if a.reserva==identificador_reserva:
                              continue
                         else:
                              new1+=[a]
                    canchas.contFactura+=1
                    
                    canchas.validacion_r=new
                    canchas.dis=new1
                    lista=factura(identificador_reserva,fecha,horas,precio,total,cliente,canchas.contFactura)
                    canchas.facturas+=[lista]
                    print("Factura:",canchas.contFactura)
                    print("Cliente:",cliente)
                    print("Horas:",horas)
                    print("Total:",total)
                              
                         
                         
                         
                         
                         
               
          else:
               return "El identificador tiene que ser entero y diferente a vacio"
     def ver_fecturas(self,fecha):
          cont=0
          total=0
          if isinstance(fecha,str) and fecha!="":
               for k in canchas.facturas:
                    if k.fecha==fecha:
                         cont+=1
                         total+=k.total
                         
               for i in canchas.facturas:
                    if i.fecha==fecha:
                         i.mostrar()
                         print("Total:",total)
               if cont==0:
                    return "No se encontro ningúna fecha relacionada"
          else:
               return "La fecha tiene que ser un str y diferente a vacio"
     
          
          
          
          
                    
                    
                         
                    
               
          
class factura:
     def __init__(self,reserva,fecha,horas,precio,total,cliente,val_factura):
          self.reserva=reserva
          self.fecha=fecha
          self.horas=horas
          self.precio=precio
          self.total=total
          self.cliente=cliente
          self.val_factura=val_factura
     def mostrar(self):
          print("Cliente",self.cliente)
          print("Identificador",self.reserva)
          print("Fecha",self.fecha)
          print("horas",self.horas)
          print("Precio",self.precio)
          print("Total",self.total)
          print("----------------------------")
               
class disponible:
     def __init__(self,identificador,HoraI,HoraF,reserva):
          self.identificador=identificador
          self.HoraI=HoraI
          self.HoraF=HoraF
          self.reserva=reserva
     def mostrar(self):
          print("Identificador",self.identificador)
          print("Hora inicio",self.HoraI)
          print("Hora final",self.HoraF)
          print("Codigo reserva",self.reserva)
          
     
                    
class reserva:
     def __init__(self,cedula,identificador_cancha,fecha,hora_inicio,hora_fin,identificador_reserva):
          self.cedula=cedula
          self.identificador_cancha=identificador_cancha
          self.fecha=fecha
          self.hora_inicio=hora_inicio
          self.hora_fin=hora_fin
          self.identificador_reserva=identificador_reserva
          
     def mostrar(self):
          print("Cedula",self.cedula)
          print("Identifacador",self.identificador_cancha)
          print("Fecha",self.fecha)
          print("HoraInicio",self.hora_inicio)
          print("HoraFin",self.hora_fin)
          print("Identifacador_reserva",self.identificador_reserva)
          print("-----------------------------------------------------")
     
          



class cliente:
     def __init__(self,cedula,nombre,telefono,correo):
          self.cedula=cedula
          self.nombre=nombre
          self.telefono=telefono
          self.correo=correo
     def mostrar(self):
          print("Nombre",self.nombre)
          print("Cedula",self.cedula)
          print("Telefono",self.telefono)
          print("Correo",self.correo)
          print("--------------------------------")
     
          
          


class cancha:
     def __init__(self,identificador,precio):
          self.identificador=identificador
          self.precio=precio
     def mostar(self):
          print("ID",self.identificador)
          print("Precio",self.precio)
          print("-----------------------------")


