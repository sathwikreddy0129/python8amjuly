# a ={ 'username':'sathwik', 'password':'sanjev'}
# print(a)
# print(type(a))

#a = {'username': 'sanjev', ('mobile'):9898565645, 1:45} -- any data type for dictionary
# a = {'username': 'sanjev', ('mobile'):9898565645, 1:45} 
# print(a['password'])
# print(a[1])
# print(a[('mobile')])
# a['email'] = 'gsajev@gmail.com'
# print(a)

#nested dictioaries
# a = {"india" : {"telangana": "hyderabad", "tamiladu":"chennai"},
#     "usa" : {"newyork" : "newyork", "california" : "california"}}
# print(a["india"])
# print(a["india"] ["telangana"])
# print(a["usa"] ["newyork"])

# dictionary methods

#get
# a = {"continent" :"africa"}
# print(a.get("africa"))
# print(a)

#update

# a = {"username" : "sanjeev", "password" : "sajeev123"}
# b = {"email" : "sanjeev@gmail.com", "phone" : "9959452655"}
# a.update(b)
# print(a)
# a['city'] = "hyderabad"
# print(a)


#pop
# a = {"username" : "sanjeev", 'password' : "sajeev123"}
# a.pop('password')
# print(a)

#popitem
# a = {"username" : "sanjeev", 'password' : "sajeev123"}
# a.popitem( )
# print(a)

#clear
# a = {"username" : "sanjeev", 'password' : "sajeev123"}
# a.clear()
# print(a)

#keys
# a = {"username" : "sanjeev", 'password' : "sajeev123"}
# print(a.keys())

#value
# a = {"username" : "sanjeev", 'password' : "sajeev123"}
# print(a.values())

#items
# a = {"username" : "sanjeev", 'password' : "sajeev123"}
# print(a.items())

#fromkeys()
# a = ['username', 'password', 'email']
# print({}. fromkeys(a))
# print({}. fromkeys(a,12))

#setdefault
# a = {'username':'sanjeev', 'password':'san'}
# a.setdefault('phone')
# print(a)
# a['phone'] = none 
# a.setdefault('phone',7894561235)
# print(a)
# a['phone'] = 1597846325
# print(a)

#copy
# a = {'username':'sanjeev', 'password': 'sanjeev123'}
# b = a.copy()
# b = a
# print(a)
# print(b)

# a['phone'] = 7893214565
# print(a)
# print(b)

#dictionary comprehension

#1st way of syntax
# a = [3,8,3,6,4,1]
# print({j:j*2 for j in [3,8,3,6,4,1]})

#2nd way syntax
# print({{row : a[row] for row in [3,8,3,6,4,1]if row in ['username', 'password', 'email']}})
