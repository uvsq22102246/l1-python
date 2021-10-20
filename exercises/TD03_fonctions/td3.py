#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    secondes=(temps[0]*86400,temps[1]*3600,temps[2]*60,temps[3])  
    return secondes   
    

temps = (3,23,1,34)
mon_temps=tempsEnSeconde(temps)
print (mon_temps)

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    temps=(seconde//86400),(seconde)%86400//3600,((seconde%86400)%3600)//60,(((seconde%86400)%3600)%60) 
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


    
