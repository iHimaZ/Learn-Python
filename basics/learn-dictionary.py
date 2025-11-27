
data = { 'ibrahim':'38y','salma':'27y','loreen':'2.8y','sedra':'6m' }
# this throw error ( KeyError: 'ss' ) if the key not exists
print(data['sedra'])

# this not throw error if key not exists will get none
print(data.get('ss'))

# can use overload method of get like that
print(data.get('ss','Key not found'))

# If I have keys separate from the values
keys = {'hima','salma','loreen'}
values = {38,28,2.5}
# can use dict function to combine keys and values in dictionary
myDic = dict(zip(keys,values))
print(myDic) # {'loreen': 2.5, 'hima': 28, 'salama': 38}

print(myDic.pop('loreen')) # pop will remove after get value
print(myDic)

del myDic['salma'] # to delete from dictionary
print(myDic)