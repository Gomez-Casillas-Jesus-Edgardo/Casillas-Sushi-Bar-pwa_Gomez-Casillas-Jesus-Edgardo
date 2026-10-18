from django.shortcuts import render

# "Base de datos" falsa: una lista de diccionarios en memoria.
# En un proyecto real esto vendría de un modelo (models.py) y una tabla,
# pero para ENTENDER qué es SSR no necesitamos base de datos: lo importante
# es que estos datos se insertan en el HTML *antes* de enviarlo al navegador.
PRODUCTOS = [
  {"id":1,"nombre":"California","categoria":"Rollos","precio":120,"stock":20,"imagen":"img/california.webp"},
  {"id":2,"nombre":"Philadelphia","categoria":"Rollos","precio":130,"stock":20,"imagen":"img/philadelphia.webp"},
  {"id":3,"nombre":"Mar y tierra empanizado","categoria":"Rollos","precio":145,"stock":20,"imagen":"img/mar-y-tierra-empanizado.webp"},
  {"id":4,"nombre":"Dragón","categoria":"Rollos","precio":165,"stock":20,"imagen":"img/dragon.webp"},
  {"id":5,"nombre":"Chiquilín","categoria":"Rollos","precio":140,"stock":20,"imagen":"img/chiquilin.webp"},
  {"id":6,"nombre":"Gyozas (5 pzs)","categoria":"Entradas","precio":85,"stock":20,"imagen":"img/gyozas-5-pzs.webp"},
  {"id":7,"nombre":"Kushiage de queso","categoria":"Entradas","precio":70,"stock":20,"imagen":"img/kushiage-de-queso.webp"},
  {"id":8,"nombre":"Tostada de atún","categoria":"Entradas","precio":95,"stock":20,"imagen":"img/tostada-de-atun.webp"},
  {"id":9,"nombre":"Edamames","categoria":"Entradas","precio":65,"stock":20,"imagen":"img/edamames.webp"},
  {"id":10,"nombre":"Sopa miso","categoria":"Entradas","precio":55,"stock":20,"imagen":"img/sopa-miso.webp"},
  {"id":11,"nombre":"Yakimeshi","categoria":"Especiales y bebidas","precio":110,"stock":20,"imagen":"img/yakimeshi.webp"},
  {"id":12,"nombre":"Teppanyaki de pollo","categoria":"Especiales y bebidas","precio":145,"stock":20,"imagen":"img/teppanyaki-de-pollo.webp"},
  {"id":13,"nombre":"Té verde","categoria":"Especiales y bebidas","precio":35,"stock":20,"imagen":"img/te-verde.webp"},
  {"id":14,"nombre":"Limonada de pepino","categoria":"Especiales y bebidas","precio":45,"stock":20,"imagen":"img/limonada-de-pepino.webp"},
  {"id":15,"nombre":"Mochi helado","categoria":"Especiales y bebidas","precio":60,"stock":20,"imagen":"img/mochi-helado.webp"}
]


def vista_ssr(request):
    """
    Vista con Renderizado en Servidor (SSR).

    request: el objeto que representa la petición que hizo el navegador.

    render() hace tres cosas:
      1) toma la plantilla 'catalogo/catalogo_ssr.html'
      2) le inyecta el diccionario de "contexto" (aquí: la lista de productos)
      3) devuelve el HTML final, YA CON LOS DATOS DENTRO, listo para el navegador.

    Por eso es "servidor": el HTML que llega al navegador ya trae escritos
    los nombres y precios. Si haces clic derecho > "Ver código fuente de la
    página" verás los productos en el HTML, aunque JavaScript esté desactivado.
    Compáralo con la vista CSR de la Parte B, donde el HTML llega vacío y es
    JavaScript quien dibuja los productos DESPUÉS, ya en el navegador.
    """
    contexto = {"productos": PRODUCTOS}
    return render(request, 'catalogo/catalogo_ssr.html', contexto)