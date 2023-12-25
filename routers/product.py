from fastapi import APIRouter
from fastapi import FastAPI, Query, Path
from models.product import Product #de la carpeta "models" selecciono "." el archivo "product.py" e importo la clase "Product"



#rutas
router = APIRouter()

#lista productos. 
products = [
    {
        "id":1,
        "name": "Producto 1",
        "price":20,
        "stock":10 
    },
      {
        "id":2,
        "name": "Producto 2",
        "price":10,
        "stock":20 
      },
      {
        "id":3,
        "name": "Producto 3",
        "price":5,
        "stock":30
      }
]



@router.get('/products')#nueva ruta
def get_products():#funcion de ruta
    return products


@router.get('/products/{id}')# los {} indican que necesito un parametro para ingresar a esa ruta
def get_produt(id: int = Path(gt=0)):#gt es para validad que el id sea mayor a 0
    return list(filter(lambda item: item['id'] == id, products))


@router.get('/products/')#ruta query
def get_products_by_stock(stock: int, price:float = Query(gt=0)):
    return list(filter(lambda item: item['stock'] == stock and item['price'] == price,
                       products))



#ruta tipo POST[] 
@router.post('/products')#ruta post. Crea nuevos productos
def create_products(product: Product):#uso el modulo product y llamo a la clase Product
  products.append(product)#con append añado un item nuevo al final de la lista
  return products


@router.put('/products/{id}')#ruta para actualizar productos
def update_product(id: int, product: Product):#ingreso de parametros id, y 
  for index, item in enumerate(products):
    if item['id'] == id:#si el id iterado de products es igual al id parametro ingresaado entonces...
      products[index]['name'] = product.name
      products[index]['stock'] = product.stock
      products[index]['price'] = product.price
  return products#retorna lista actualizada
#index marco la posicion, item itero el numero de id. 

@router.delete('/products/{id}')
def delete_product(id: int):
  for item in products:
    if item['id'] == id:#si el id ingresado es igual entonces...
      products.remove(item)#la funcion remove elimina el id de la lista 
  return products




 #dentro de filter({condicion de busqueda} {en donde quiero que guarde esa busqueda}: {item[id]} si el id es igual entonces lo guarda en una lista)

