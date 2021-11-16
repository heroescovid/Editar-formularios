data = {'school':'coronel filiberto', 'class': '7', 'name': 'abc', 'city': 'paramount'}
def agregar(producto_nuevo,**valores):
    schoolname  = data['school']
    cityname = data['city']
    standard = data['class']
    studentname = data['name']
    print(cityname)
    print(producto_nuevo)
agregar(100,**data)