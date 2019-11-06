#import a
import project

query1 = """hero{ hero{
name friends{ name } friends{ name } id   name }
hero{ hola } }
      
"""

query28 = "hero(episode:JEDI){ on Droid{ name } on Human{ id } name }"


test28 = ['hero(episode:JEDI){', 'on', 'Droid{', 'name', '}', 'on', 'Human{', 'id', 'name', '}', 'on', 'Animal{', 'name', '}', '}']
#
#RULE 1
#
query2 = """
hero(episode:JEDI){ name name }
      
"""
test2 = ['hero(episode:JEDI){', 'on', 'Droid{', 'name', '}', 'on', 'Human{', 'name', '}','on', 'Animal{', 'name', '}', '}']

query16= """
hero(episode:JEDI){ name name name name id id id }
      
"""
test16 = ['hero(episode:JEDI){', 'on', 'Droid{', 'name', 'id', '}', 'on', 'Human{', 'name', 'id', '}', 'on', 'Animal{', 'name', 'id', '}','}']

#
#RULE 2
#
query5 = """
hero(episode:JEDI){ friends{ name } friends{ id } }
      
"""

test5 = ['hero(episode:JEDI){', 'on', 'Droid{', 'friends{', 'id', 'name', '}', '}', 'on', 'Human{', 'friends{', 'id', 'name', '}', '}','on', 'Animal{', 'friends{', 'id', 'name', '}' ,'}', '}']

query18 = """
hero(episode:JEDI){ name friends{ amigos{ id } amigos{ name } } friends{ id }  id  }
      
"""

test18 = ['hero(episode:JEDI){', 'on', 'Droid{', 'name', 'friends{', 'id', 'amigos{', 'name', 'id', '}', '}', 'id', '}', 'on', 'Human{', 'name', 'friends{', 'id', 'amigos{', 'name', 'id', '}', '}', 'id', '}', 'on', 'Animal{', 'name', 'friends{', 'id', 'amigos{', 'name', 'id', '}', '}', 'id', '}','}']
query17 = """
hero(episode:JEDI){ name friends{ amigos{ id  primos{ name } primos{ id } } amigos{ name } } friends{ id } id  }
      
"""

test17 = ['hero(episode:JEDI){', 'on', 'Droid{', 'name', 'friends{', 'id', 'amigos{', 'name', 'id', 'primos{', 'id', 'name', '}', '}', '}', 'id', '}', 'on', 'Human{', 'name', 'friends{', 'id', 'amigos{', 'name', 'id', 'primos{', 'id', 'name', '}', '}', '}', 'id', '}', 'on', 'Animal{', 'name', 'friends{', 'id', 'amigos{', 'name', 'id', 'primos{', 'id', 'name', '}', '}', '}', 'id', '}', '}']

query19 = """
hero(episode:JEDI){ friends{ amigos{ id } } friends{ amigos{ name } }  }
      
"""

test19 = ['hero(episode:JEDI){', 'on', 'Droid{', 'friends{', 'amigos{', 'id', 'name', '}', '}', '}', 'on', 'Human{', 'friends{', 'amigos{', 'id', 'name', '}', '}', '}', 'on', 'Animal{', 'friends{', 'amigos{', 'id', 'name', '}', '}', '}', '}']
 

query20 = """
hero(episode:JEDI){ friends{ amigos{ id primos{ name } } } friends{ amigos{ name primos{ id } } }  }
      
"""

test20 = ['hero(episode:JEDI){', 'on', 'Droid{', 'friends{', 'amigos{', 'id', 'primos{', 'id', 'name', '}', 'name', '}', '}', '}', 'on', 'Human{', 'friends{', 'amigos{', 'id', 'primos{', 'id', 'name', '}', 'name', '}', '}', '}', 'on', 'Animal{', 'friends{', 'amigos{', 'id', 'primos{', 'id', 'name', '}', 'name', '}', '}', '}', '}']


#
#RULE 2 & RULE 1
#

query31 = """
hero(episode:JEDI){ name friends{ name friends{ name friends{ name } } } }
      
"""


query6 = """
hero(episode:JEDI){ friends{ name } friends{ name }  }
      
"""

test6 = ['hero(episode:JEDI){', 'on', 'Droid{', 'friends{', 'name', '}', '}', 'on', 'Human{', 'friends{', 'name', '}', '}', 'on', 'Animal{', 'friends{', 'name', '}', '}', '}']



query7 = """
hero(episode:JEDI){ name friends{ name } friends{ id } name }
      
"""

test7 = ['hero(episode:JEDI){', 'on', 'Droid{', 'name', 'friends{', 'id', 'name', '}', '}', 'on', 'Human{', 'name', 'friends{', 'id', 'name', '}', '}', 'on', 'Animal{', 'name', 'friends{', 'id', 'name', '}', '}', '}']

query8 = """
hero(episode:JEDI){ name friends{ name } friends{ id } name id  }
      
"""

test8= ['hero(episode:JEDI){', 'on', 'Droid{', 'name', 'friends{', 'id', 'name', '}', 'id', '}', 'on', 'Human{', 'name', 'friends{', 'id', 'name', '}', 'id', '}', 'on', 'Animal{', 'name', 'friends{', 'id', 'name', '}', 'id', '}', '}']

query13 = """
hero(episode:JEDI){ name friends{ amigos{ id } amigos{ id } } friends{ id } name id  }
      
"""

test13 = ['hero(episode:JEDI){', 'on', 'Droid{', 'name', 'friends{', 'id', 'amigos{', 'id', '}', '}', 'id', '}', 'on', 'Human{', 'name', 'friends{', 'id', 'amigos{', 'id', '}', '}', 'id', '}', 'on', 'Animal{', 'name', 'friends{', 'id', 'amigos{', 'id', '}', '}', 'id', '}', '}']

query14 = """
hero(episode:JEDI){ name friends{ amigos{ id  primos{ name } primos{ id } } amigos{ id } } friends{ id } name id  }
      
"""

test14 = ['hero(episode:JEDI){', 'on', 'Droid{', 'name', 'friends{', 'id', 'amigos{', 'id', 'primos{', 'id', 'name', '}', '}', '}', 'id', '}', 'on', 'Human{', 'name', 'friends{', 'id', 'amigos{', 'id', 'primos{', 'id', 'name', '}', '}', '}', 'id', '}', 'on', 'Animal{', 'name', 'friends{', 'id', 'amigos{', 'id', 'primos{', 'id', 'name', '}', '}', '}', 'id', '}' , '}']
          
query15 = """
hero(episode:JEDI){ name friends{ amigos{ id  primos{ name } primos{ id name } } amigos{ id } } friends{ id } name id  }
      
"""

test15 = ['hero(episode:JEDI){', 'on', 'Droid{', 'name', 'friends{', 'id', 'amigos{', 'id', 'primos{', 'id', 'name', '}', '}', '}', 'id', '}', 'on', 'Human{', 'name', 'friends{', 'id', 'amigos{', 'id', 'primos{', 'id', 'name', '}', '}', '}', 'id', '}', 'on', 'Animal{', 'name', 'friends{', 'id', 'amigos{', 'id', 'primos{', 'id', 'name', '}', '}', '}', 'id', '}', '}']


#
#RULE 3 & RULE 4
#

query10 = """
hero(episode:JEDI){ on Human{ on Human{  name   } } }
      
"""

test10= ['hero(episode:JEDI){', 'on', 'Human{', 'name', '}', '}']

query21 = """
hero(episode:JEDI){ on Human{ on Human{ on Human{ name  }   } } }
      
"""

test21= ['hero(episode:JEDI){', 'on', 'Human{', 'name', '}', '}']

query22 = """
hero(episode:JEDI){ on Human{ on Human{ on Human{ on Human{  on Human{ name  } } }   } } }
      
"""

test22= ['hero(episode:JEDI){', 'on', 'Human{', 'name', '}', '}']








#
#RULE 3 & RULE 7
#

query11 = """
hero(episode:JEDI){ on Human{  on Droid{ name } name  }   } 
      
"""

test11= ['hero(episode:JEDI){', 'on', 'Human{', 'name', '}', '}']


#
#RULE 3 & RULE 4 & RULE 7
#

query23 = """
hero(episode:JEDI){ on Human{  on Droid{ on Human{  name  } } name }   } 
      
"""

test23= ['hero(episode:JEDI){', 'on', 'Human{', 'name', '}', '}']

query24 = """
hero(episode:JEDI){ on Human{  on Droid{ on Human{ on Human{ on Human{ on Human{  on Human{ name  } } }   } } } name }   } 
      
"""

test24= ['hero(episode:JEDI){', 'on', 'Human{', 'name', '}', '}']

query9 = """
hero(episode:JEDI){ on Human{ on Human{ on Human{ id on Droid{ name } name  }   } } }
  
"""

test9= ['hero(episode:JEDI){', 'on', 'Human{', 'id', 'name', '}', '}']

query27 = """
hero(episode:JEDI){ on Human{ on Human{ on Human{ on Human{ id } on Droid{ name } name  }   } } }
      
"""

test27= ['hero(episode:JEDI){', 'on', 'Human{', 'id', 'name', '}', '}']





#
#RULE 1 & RULE 3 & RULE 4
#

query3 = """
hero(episode:JEDI){ hola  on Human{ name on Human{ name }  } }
      
"""
test3 = ['hero(episode:JEDI){', 'on', 'Droid{', 'hola', '}', 'on', 'Human{', 'hola', 'name', '}', 'on', 'Animal{', 'hola', '}', '}']
#
query12 = """
hero(episode:JEDI){ on Human{ on Human{ name on Human{ id name  }   } } }
      
"""

test12= ['hero(episode:JEDI){', 'on', 'Human{', 'name', 'id', '}', '}']

query25 = """
hero(episode:JEDI){ on Human{ on Human{ on Human{ on Human{ on Human{  on Human{ name  } }    } } } name }   } 
      
"""

test25= ['hero(episode:JEDI){', 'on', 'Human{', 'name', '}', '}']

query29 = """
hero(episode:JEDI){ on Human{ on Human{ name on Human{ name on Human{ on Human{  on Human{ name  } }    } } } name }   } 
      
"""

test29= ['hero(episode:JEDI){', 'on', 'Human{', 'name', '}', '}']

query26 = """
hero(episode:JEDI){ name on Human{ on Human{ name on Human{ name on Human{ on Human{  on Human{ name  } }    } } } name }  name } 
      
"""

test26= ['hero(episode:JEDI){', 'on', 'Droid{', 'name', '}', 'on', 'Human{', 'name', '}', 'on', 'Animal{', 'name', '}' ,'}']


#
#RULE 2 & RULE 3 & RULE 4
#
query4 = """
hero(episode:JEDI){ hola  on Human{ name on Human{ friends{ id } friends{ name }   }   } }
      
"""

test4 = ['hero(episode:JEDI){', 'on', 'Droid{', 'hola', '}', 'on', 'Human{', 'hola', 'name', 'friends{', 'name', 'id', '}', '}', 'on', 'Animal{', 'hola', '}', '}']

query50 = """
hero(episode:JEDI){ id friends{ on Human{ name } on Droid{ id } id }  }
      
"""

lista5 = [[query2,test2],[query3,test3],[query4,test4],[query5,test5],[query6,test6],[query7,test7],[query8,test8],[query9,test9],[query10,test10],[query11,test11],[query12,test12],[query13,test13],[query14,test14], [query15,test15],[query16,test16],[query17,test17],[query18,test18],[query19,test19],[query20,test20],[query21,test21],[query22,test22],[query23,test23],[query24,test24],[query25,test25],[query26,test26],[query27,test27],[query28,test28],[query29,test29]]





#
#    TEST
#
lista1 = []
count = 2
for i in lista5:
    cadena = i[0]
    print count 
    if  project.main(cadena,'schema2.txt') == i[1]:
        lista1.append(['query'+str(count),True])
    else:
        lista1.append(False)
    count = count + 1
for i in lista1:
    print i


    

'''
cadena = query50
lista= cadena.split() #argumentos separados

print a.main(lista)
'''
