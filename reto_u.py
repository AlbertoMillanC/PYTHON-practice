def cliente(informacion:dict)->dict: 
    if informacion['edad']>18 and informacion['primer_ingreso']==True:
        informacion={ 'nombre' : informacion["nombre"],
            'edad': informacion["edad"],
            "atraccion" : "X-Treme",
            'primer_ingreso': True, 
            "total_boleta" :20000-(20000*0.05) 

  }
print(cliente(informacion))

