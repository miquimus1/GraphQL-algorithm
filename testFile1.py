#import a
import project







query31 = """
hero(episode:JEDI){ on Human{ on Human{ name on Human{ id name  }   } } } 
hero(episode:JEDI){ hola  on Human{ name on Human{ friends{ id } friends{ name }   }   } }
      
"""
test31= [
    'hero(episode:JEDI){' , 'on', 'Human{', 'name', 'id', '}', '}',
    'hero(episode:JEDI){' , 'on', 'Droid{', 'hola', '}', 'on', 'Human{', 'hola', 'name', 'friends{', 'name', 'id', '}', '}', '}']

query32 = """
hero(episode:JEDI){ on Human{ on Human{ name on Human{ id name  }   } } } 
hero(episode:JEDI){ hola  on Human{ name on Human{ friends{ id } friends{ name }   }   } }
hero(episode:JEDI){ friends{ name } friends{ id } }
hero(episode:JEDI){ friends{ amigos{ id } } friends{ amigos{ name } }  }
"""
test32 = [
    'hero(episode:JEDI){' , 'on', 'Human{', 'name', 'id', '}', '}',
    'hero(episode:JEDI){' , 'on', 'Droid{', 'hola', '}', 'on', 'Human{', 'hola', 'name', 'friends{', 'name', 'id', '}', '}', '}',
    'hero(episode:JEDI){' , 'on', 'Droid{', 'friends{', 'id', 'name', '}', '}', 'on', 'Human{', 'friends{', 'id', 'name', '}', '}', '}',
    'hero(episode:JEDI){' , 'on', 'Droid{', 'friends{', 'amigos{', 'id', 'name', '}', '}', '}', 'on', 'Human{', 'friends{', 'amigos{', 'id', 'name', '}', '}', '}', '}']

query33 = """
hero(episode:JEDI){ friends{ amigos{ id primos{ name } } } friends{ amigos{ name primos{ id } } }  }
hero(episode:JEDI){ hola  on Human{ name on Human{ name }  } }
"""
test33 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'friends{', 'amigos{', 'id', 'primos{', 'id', 'name', '}', 'name', '}', '}', '}', 'on', 'Human{', 'friends{', 'amigos{', 'id', 'primos{', 'id', 'name', '}', 'name', '}', '}', '}', '}', 'hero(episode:JEDI){' , 'on', 'Droid{', 'hola', '}', 'on', 'Human{', 'hola', 'name', '}', '}']

query34 = """
hero(episode:JEDI){ friends{ name } friends{ id } }
hero(episode:JEDI){ friends{ amigos{ id } } friends{ amigos{ name } }  }
      
"""
test34 = [
    'hero(episode:JEDI){' , 'on', 'Droid{', 'friends{', 'id', 'name', '}', '}', 'on', 'Human{', 'friends{', 'id', 'name', '}', '}', '}',
    
    'hero(episode:JEDI){' , 'on', 'Droid{', 'friends{', 'amigos{', 'id', 'name', '}', '}', '}', 'on', 'Human{', 'friends{', 'amigos{', 'id', 'name', '}', '}', '}', '}']




query35 = "hero(episode:JEDI){ name }"

test35 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'name', '}', 'on', 'Human{', 'name', '}', '}']

query36 = "hero(episode:JEDI){ friends{ name } }"

test36 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'friends{', 'name', '}', '}', 'on', 'Human{', 'friends{', 'name', '}', '}', '}']


query37 = "hero(episode:JEDI){ on Human{ name } on Droid{ name } }"

test37 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'name', '}', 'on', 'Human{', 'name', '}', '}']

query38 = "hero(episode:JEDI){ on Human{ name id } on Droid{ id name } }"

test38 =['hero(episode:JEDI){' , 'on', 'Droid{', 'id', 'name', '}', 'on', 'Human{', 'name', 'id', '}', '}']

query39 = "hero(episode:JEDI){ id name }"

test39 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'id', 'name', '}', 'on', 'Human{', 'id', 'name', '}', '}']

query40= ""

test40 = []


#
#RULE 1
#
query2 = """
hero(episode:JEDI){ name name }
      
"""
test2 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'name', '}', 'on', 'Human{', 'name', '}', '}']

query3= """
hero(episode:JEDI){ name name name name id id id }
      
"""
test3 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'name', 'id', '}', 'on', 'Human{', 'name', 'id', '}', '}']

#
#RULE 2
#
query4 = """
hero(episode:JEDI){ friends{ name } friends{ id } }
      
"""

test4 = ['hero(episode:JEDI){', 'on', 'Droid{', 'friends{', 'id', 'name', '}', '}', 'on', 'Human{', 'friends{', 'id', 'name', '}', '}', '}']

query5 = """
hero(episode:JEDI){ name friends{ amigos{ id } amigos{ name } } friends{ id }  id  }
      
"""

test5 = ['hero(episode:JEDI){', 'on', 'Droid{', 'name', 'friends{', 'id', 'amigos{', 'name', 'id', '}', '}', 'id', '}', 'on', 'Human{', 'name', 'friends{', 'id', 'amigos{', 'name', 'id', '}', '}', 'id', '}', '}']

query6 = """
hero(episode:JEDI){ name friends{ amigos{ id  primos{ name } primos{ id } } amigos{ name } } friends{ id } id  }
      
"""

test6 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'name', 'friends{', 'id', 'amigos{', 'name', 'id', 'primos{', 'id', 'name', '}', '}', '}', 'id', '}', 'on', 'Human{', 'name', 'friends{', 'id', 'amigos{', 'name', 'id', 'primos{', 'id', 'name', '}', '}', '}', 'id', '}', '}']

query7 = """
hero(episode:JEDI){ friends{ amigos{ id } } friends{ amigos{ name } }  }
      
"""

test7 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'friends{', 'amigos{', 'id', 'name', '}', '}', '}', 'on', 'Human{', 'friends{', 'amigos{', 'id', 'name', '}', '}', '}', '}']
 

query8 = """
hero(episode:JEDI){ friends{ amigos{ id primos{ name } } } friends{ amigos{ name primos{ id } } }  }
      
"""

test8 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'friends{', 'amigos{', 'id', 'primos{', 'id', 'name', '}', 'name', '}', '}', '}', 'on', 'Human{', 'friends{', 'amigos{', 'id', 'primos{', 'id', 'name', '}', 'name', '}', '}', '}', '}']


#
#RULE 2 & RULE 1
#




query9 = """
hero(episode:JEDI){ friends{ name } friends{ name }  }
      
"""

test9 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'friends{', 'name', '}', '}', 'on', 'Human{', 'friends{', 'name', '}', '}', '}']



query10 = """
hero(episode:JEDI){ name friends{ name } friends{ id } name }
      
"""

test10 = ['hero(episode:JEDI){', 'on', 'Droid{', 'name', 'friends{', 'id', 'name', '}', '}', 'on', 'Human{', 'name', 'friends{', 'id', 'name', '}', '}', '}']

query11 = """
hero(episode:JEDI){ name friends{ name } friends{ id } name id  }
      
"""

test11 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'name', 'friends{', 'id', 'name', '}', 'id', '}', 'on', 'Human{', 'name', 'friends{', 'id', 'name', '}', 'id', '}', '}']

query12 = """
hero(episode:JEDI){ name friends{ amigos{ id } amigos{ id } } friends{ id } name id  }
      
"""

test12 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'name', 'friends{', 'id', 'amigos{', 'id', '}', '}', 'id', '}', 'on', 'Human{', 'name', 'friends{', 'id', 'amigos{', 'id', '}', '}', 'id', '}', '}']

query13 = """
hero(episode:JEDI){ name friends{ amigos{ id  primos{ name } primos{ id } } amigos{ id } } friends{ id } name id  }
      
"""

test13 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'name', 'friends{', 'id', 'amigos{', 'id', 'primos{', 'id', 'name', '}', '}', '}', 'id', '}', 'on', 'Human{', 'name', 'friends{', 'id', 'amigos{', 'id', 'primos{', 'id', 'name', '}', '}', '}', 'id', '}', '}']
          
query14 = """
hero(episode:JEDI){ name friends{ amigos{ id  primos{ name } primos{ id name } } amigos{ id } } friends{ id } name id  }
      
"""

test14 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'name', 'friends{', 'id', 'amigos{', 'id', 'primos{', 'id', 'name', '}', '}', '}', 'id', '}', 'on', 'Human{', 'name', 'friends{', 'id', 'amigos{', 'id', 'primos{', 'id', 'name', '}', '}', '}', 'id', '}', '}']


#
#RULE 3 & RULE 4
#

query15 = """
hero(episode:JEDI){ on Human{ on Human{  name   } } }
      
"""

test15= ['hero(episode:JEDI){' , 'on', 'Human{', 'name', '}', '}']

query16 = """
hero(episode:JEDI){ on Human{ on Human{ on Human{ name  }   } } }
      
"""

test16= ['hero(episode:JEDI){' , 'on', 'Human{', 'name', '}', '}']

query17 = """
hero(episode:JEDI){ on Human{ on Human{ on Human{ on Human{  on Human{ name  } } }   } } }
      
"""

test17 = ['hero(episode:JEDI){' , 'on', 'Human{', 'name', '}', '}']








#
#RULE 3 & RULE 7
#

query18 = """
hero(episode:JEDI){ on Human{  on Droid{ name } name  }   } 
      
"""

test18 = ['hero(episode:JEDI){' , 'on', 'Human{', 'name', '}', '}']


#
#RULE 3 & RULE 4 & RULE 7
#

query19 = """
hero(episode:JEDI){ on Human{  on Droid{ on Human{  name  } } name }   } 
      
"""

test19 = ['hero(episode:JEDI){' , 'on', 'Human{', 'name', '}', '}']

query20 = """
hero(episode:JEDI){ on Human{  on Droid{ on Human{ on Human{ on Human{ on Human{  on Human{ name  } } }   } } } name }   } 
      
"""


test20= ['hero(episode:JEDI){' , 'on', 'Human{', 'name', '}', '}']

query21 = """
hero(episode:JEDI){ on Human{ on Human{ on Human{ id on Droid{ name } name  }   } } }
  
"""

test21 = ['hero(episode:JEDI){' , 'on', 'Human{', 'id', 'name', '}', '}']

query22 = """
hero(episode:JEDI){ on Human{ on Human{ on Human{ on Human{ id } on Droid{ name } name  }   } } }
      
"""

test22 = ['hero(episode:JEDI){' , 'on', 'Human{', 'id', 'name', '}', '}']





#
#RULE 1 & RULE 3 & RULE 4
#

query23 = "hero(episode:JEDI){ on Droid{ name } on Human{ id } name }"


test23 = ['hero(episode:JEDI){' , 'on', 'Droid{','name', '}', 'on', 'Human{', 'id', 'name', '}', '}']

query24 = """
hero(episode:JEDI){ hola  on Human{ name on Human{ name }  } }
      
"""
test24 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'hola', '}', 'on', 'Human{', 'hola', 'name', '}', '}']
#
query25 = """
hero(episode:JEDI){ on Human{ on Human{ name on Human{ id name  }   } } }
      
"""

test25 = ['hero(episode:JEDI){' , 'on', 'Human{', 'name', 'id', '}', '}']

query26 = """
hero(episode:JEDI){ on Human{ on Human{ on Human{ on Human{ on Human{  on Human{ name  } }    } } } name }   } 
      
"""

test26 = ['hero(episode:JEDI){' , 'on', 'Human{', 'name', '}', '}']

query27 = """
hero(episode:JEDI){ on Human{ on Human{ name on Human{ name on Human{ on Human{  on Human{ name  } }    } } } name }   } 
      
"""

test27 = ['hero(episode:JEDI){' , 'on', 'Human{', 'name', '}', '}']

query28 = """
hero(episode:JEDI){ name on Human{ on Human{ name on Human{ name on Human{ on Human{  on Human{ name  } }    } } } name }  name } 
      
"""

test28 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'name', '}', 'on', 'Human{', 'name', '}', '}']


#
#RULE 2 & RULE 3 & RULE 4
#
query29 = """
hero(episode:JEDI){ hola  on Human{ name on Human{ friends{ id } friends{ name }   }   } }
      
"""

test29 = ['hero(episode:JEDI){' , 'on', 'Droid{', 'hola', '}', 'on', 'Human{', 'hola', 'name', 'friends{', 'name', 'id', '}', '}', '}']

query30 = """
hero(episode:JEDI){ on Human{ id on Human{ name } name }  }
      
"""
test30 = ['hero(episode:JEDI){' , 'on', 'Human{', 'id', 'name', '}', '}']

#MAL
query100 = """
hero(episode:JEDI){ name friends{ on Human{ on Alien{ name } } }  }
      
"""

query101 = """
hero(episode:JEDI){ friends{ name } friends{ id } }
      
"""
query102 = """
hero(episode:JEDI){ name friends{ name friends{ name friends{ name } } } }
      
"""

lista5 = [[query2,test2],[query3,test3],[query4,test4],[query5,test5],[query6,test6],[query7,test7],[query8,test8],[query9,test9],[query10,test10],[query11,test11],[query12,test12],[query13,test13],[query14,test14], [query15,test15],[query16,test16],[query17,test17],[query18,test18],[query19,test19],[query20,test20],[query21,test21],[query22,test22],[query23,test23],[query24,test24],[query25,test25],[query26,test26],[query27,test27],[query28,test28],[query29,test29],[query30,test30],[query31,test31],[query32,test32],[query33,test33],[query34,test34],[query35,test35],[query36,test36],[query37,test37],[query38,test38],[query39,test39],[query40,test40]]



#
#    TEST
#
lista1 = []
count = 2
for i in lista5:
    cadena = i[0]
    print count 
    if  project.main(cadena,'schema.txt') == i[1]:
        lista1.append(['query'+str(count),True])
    else:
        lista1.append(False)
    count = count + 1
for i in lista1:
    print i
'''

cadena = query5
lista= cadena.split() #argumentos separados
print a.main(lista)

'''
