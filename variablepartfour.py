# dictionary uses {}
# dictionary is indexed (using keys)
# dictionary is ordered
# dictionary is alos referred as key-value pair
# key must be different, but value can be duplicated

# create a student data
# edit data about khairi using keys

khairi = {
    "firstname": "Khairi",
    "lastname": "Abu Bakar",
    "icnumber": 778899,
    "subject": ["BM", "BI", "Maths", "Science", "Social science"],
    "active": True,
    "paid": True,
    "addresses": [
        {
            "street": "Jalan 26/1A",
            "area": "Cheras",
            "state": "Selangor",
            "country": "Malaysia"
        },
        {
            "street": "Lorong 99/9A",
            "area": "Petaling Jaya",
            "state": "Kuala Lumpur"
        }
    ]
} 

print ("First Name:", khairi["firstname"])
print ("Last Name:", khairi["lastname"])
print ("IC Number:", khairi["icnumber"])
print ("Subject:", khairi["subject"])
print ("Active:", khairi["active"])
print ("Paid:", khairi["paid"])

print ("Address") 
for address in khairi ["addresses"]:
    print(address["street"])
    print(address["area"])
    print(address["state"])
    if ("country" in address.keys()):
        print (address ["country"]) 

print ("------------------------------------------------------")

print (khairi.keys())
print (khairi.values())

print (khairi.items()) #list of tuple where each tuple has key, value
for key, value in khairi.items():
    print (key, value)

print ("------------------------------------------------------")

khairi ["car"] = {
    "brand": "Proton",
    "model": "Saga",
    "number": "ABC1234"
}

print (khairi)

print ("------------------------------------------------------")

khairi ["icnumber"] = 556677
print (khairi)

print ("------------------------------------------------------")

khairi ['addresses'][1]["country"] = "Malaysia"
khairi ['addresses'][1]["street"] = "Terowong 105/110A"
print (khairi)

print ("------------------------------------------------------")

khairi['addresses'].append({
    "street": "Longkang 101/103A",
    "area": "Petaling Jaya",
    "state": "Kuala Lumpur"
})
print (khairi)

print ("------------------------------------------------------")

khairi.pop("car")     #delete item by key (eg. car)
print (khairi)

print ("------------------------------------------------------")

newdictionary = dict()
print(newdictionary)

#mynumbers = [[0,1,2], [3,4,5], [6,7,8]]
#print (mynumbers [0][2])

 