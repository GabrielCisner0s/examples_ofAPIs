from fastapi import FastAPI
from routers.product import router as product_router# as sirve oara cambiar el nombre de la funcion pero como destinatario
#uvicorn {nombre de archivo.py}:{nombre de la aplicacion instanciada}
#/docs en la direccion para acceder a la Api



app = FastAPI()#instancia

@app.get('/')#ruta de inicio
def message():#funcion de ruta
    return "hola mundo!"


app.include_router(roduct_router)#luego de importar rutas las meto en esta funcion



