car={"brand":"Ford","model":"Mustang","year":2024}#membuat dictionary berisi brand model dan year
print(car["model"])#mencetak model dari dictionary yaitu Mustang
car["color"]="red"#menambahkan key color dengan value red ke dictionary
print(car)#mencetak semua key dan value dalam dictionary
car.pop("brand")#menghapus key brand dari dictionary
print(car)#menghapus key brand dari dictionary