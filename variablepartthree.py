# set uses {}
# tuple uses ()
# list uses []

# set is not indexed and not ordered
fruits = {"apple", "orange", "mango", "banana", "durian"} #not ordered
print (fruits)

# cannot use index
# print (fruits[0])     #TypeError

#set is iterable
for fruit in fruits:
    print (fruit)

# more than one item assigned to a sinhle variable is called "Iterable Object"
# not all iterable objects are not "Subscriptable"

# set does not allow duplicate
fruits = ["apple", "orange", "mango", "banana", "apple", "grapes", "apple", "durian"]
print (fruits)

# can typecast any iterable object to a set using set function
fruitsset = set (fruits)    # [] becomes {}
print (fruitsset)

# cannot append (adding as last item) an item, since it is not allowed
# but we can add a new item to existing set
fruitsset.add ("rambutan")
print (fruitsset)

# remove existing item
fruitsset.remove ("apple")
print (fruitsset) 

# clear all item
fruitsset.clear()
print (fruitsset)    # print as "set()"" because {} used by dictionary

print ("----------------------------------------------------------")

# add more than one
fruitsset = {"apple", "orange", "mango", "banana", "grapes" }
localfruits = {"cempedak", "mangosteen", "grapes", "durian", "rambutan"}
fruitsset.update (localfruits)
print (fruitsset)   # grape has one because set cant duplicate

# set arithmetic
localfruits = {"cempedak", "mangosteen", "banana", "durian", "rambutan"}
overseafruits = {"apple", "orange", "mango", "grapes", "banana" }

allfruits = localfruits.union (overseafruits)
print (allfruits)
commonfruits = localfruits.intersection (overseafruits)
print (commonfruits)

print ("----------------------------------------------------------")

# available in Malaysia
malaysianfruits = localfruits.difference (overseafruits)
print (malaysianfruits)

# not in malaysia
importedfruits = overseafruits.difference (localfruits)
print (importedfruits)

print ("----------------------------------------------------------")

localfruits = {"cempedak", "mangosteen", "banana", "durian", "rambutan"}
overseafruits = {"apple", "orange", "mango", "grapes", "banana" }

favoritefruits = {"durian", "rambutan", "mangosteen"}
print (favoritefruits.issubset(localfruits))
print (localfruits.issuperset(favoritefruits))
print (favoritefruits.isdisjoint(overseafruits))

# get me all the fruits but minus the fruits which is available in both places
print (localfruits.symmetric_difference(overseafruits))

# find result and update localfruits with the result
# will loose data in localfruits
localfruits.intersection_update(overseafruits) 
print (localfruits)

print ("----------------------------------------------------------")

# set is a function that help us to create set object
# similarly frozen_set is another built in function that help us to create readonly set object
# similar to list
# similar to set

# frozenset not have intersection_update
readonlyset = frozenset ({"apple", "orange", "mango", "banana"})
print(readonlyset) 






