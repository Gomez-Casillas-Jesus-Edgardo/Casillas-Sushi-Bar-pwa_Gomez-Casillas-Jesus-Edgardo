# Nombre de tu negocio — PWA de ventas

| Dato | Valor |
|---|---|
| **Alumno** | GOMEZ CASILLAS JESUS EDGARDO |
| **Grupo** | ING10-1 |
| **Negocio · giro** | Casillas Sushi Bar · Sushi y comida japonesa|

| **URL del repositorio** | https://github.com/Gomez-Casillas-Jesus-Edgardo/Casillas-Sushi-Bar-pwa_Gomez-Casillas-Jesus-Edgardo|

| **URL de GitHub Pages** | https://gomez-casillas-jesus-edgardo.github.io/Casillas-Sushi-Bar-pwa_Gomez-Casillas-Jesus-Edgardo/ |

## Historial de avances

| Avance | Hash del commit entregado | Fecha |
|---|---|---|
| 1 | efe0779 | 11/10/2026 |
| 2 | b3ac272 | 18/10/2026 |
| 3 | 83c058d | 25/10/2026 |
| 4 | (se escribe en el reporte PDF) | 01/11/2026 |

## Comparación SSR vs CSR

### SSR (Django): los productos llegan escritos en el HTML
![Código fuente SSR](docs/captura-ssr.png)

### CSR (JavaScript): el div del catálogo llega vacío
![Código fuente CSR](docs/captura-csr.png)

## Funciones PWA (avance 3)

### index.html: manifest y registro del Service Worker activos
![Código fuente index.html](docs/captura-index-pwa.png)

### sw.js: Workbox precachea el catálogo y las fotos
![Código fuente sw.js](docs/captura-sw.png)

## Versión publicada (avance 4)

### index.html en GitHub Pages
![Código fuente publicado](docs/captura-pages-index.png)

### manifest.json en GitHub Pages
![manifest.json publicado](docs/captura-pages-manifest.png)

### Mi app instalada en el celular
![App instalada en el celular](docs/captura-celular.png)

### Guia de instalacion de la app para celulares:

La app se puede instalar directo desde el navegador desde esta URL:
https://gomez-casillas-jesus-edgardo.github.io/Casillas-Sushi-Bar-pwa_Gomez-Casillas-Jesus-Edgardo/

#### Android (Chrome)

1. Abrir **Chrome** en celular y entrar a la URL de GitHub Pages.
2. Esperar a que cargue el catálogo con sus fotos. Con eso el Service Worker queda registrado y la app ya se puede instalar.
3. Tocar el menú de **tres puntos (⋮)** que está arriba a la derecha.
4. Seleccionar **"Instalar app"** (en algunas versiones aparece como **"Agregar a la pantalla principal"**).
5. En el mensaje de confirmación presionar **"Instalar"**.
6. El ícono de **Sushi Casillas Bar** aparecera en la pantalla de inicio y en el cajón de aplicaciones.
7. Lo seleccionamos para abrirla. Se ve a pantalla completa, sin la barra de direcciones del navegador, como una app normal.

#### iPhone (Safari)

> En iPhone la instalación solo funciona desde **Safari**. Si se abre la URL en Chrome u otro navegador, no aparece la opción.

1. Abrir **Safari** en iPhone y entro a la URL de GitHub Pages.
2. Esperar a que cargue el catálogo completo.
3. seleccionar el botón **Compartir** (el cuadrito con una flecha hacia arriba) en la barra inferior.
4. Deslizar el menú hacia abajo y seleccionar **"Agregar a pantalla de inicio"**.
5. Dejar el nombre **"Sushi Casillas Bar"** (o puedes cambiarlo) y seleccionar **"Agregar"** arriba a la derecha.
6. El ícono de **Sushi Casillas Bar** aparece en la pantalla de inicio.
7. Lo seleccionamos para abrirla. Se abre a pantalla completa, sin las barras de Safari.