import json # mengimport library json
x = '{"name": "emil","age": 30}'# mendefinisikan string JSON
y = json.loads(x)# mengubah string JSON menjadi dictionary
print(y["age"])# mencetak nilai dari key "age"

