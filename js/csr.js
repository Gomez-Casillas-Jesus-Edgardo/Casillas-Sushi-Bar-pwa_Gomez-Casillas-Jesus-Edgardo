// csr.js — Renderizado en el Cliente (CSR) con Filtros por Categoría

// 1) Buscamos el contenedor del catálogo y los botones de filtro
const contenedorCatalogo = document.getElementById("catalogo");
const botonesFiltro = document.querySelectorAll(".btn-filtro");

let todosLosProductos = []; // Guardamos la lista original recibida del JSON

// Función auxiliar para dibujar las tarjetas de productos
function renderizarProductos(productos) {
  contenedorCatalogo.innerHTML = "";
  contenedorCatalogo.removeAttribute("aria-busy");
  contenedorCatalogo.removeAttribute("aria-label");

  if (productos.length === 0) {
    contenedorCatalogo.innerHTML = "<p>No hay productos disponibles en esta categoría.</p>";
    return;
  }

  productos.forEach((producto) => {
    // creamos un <div class="producto"> por cada producto
    const tarjeta = document.createElement("div");
    tarjeta.className = "producto";

    tarjeta.innerHTML = `
      <img class="producto__foto" src="${producto.imagen}" alt="${producto.nombre}" loading="lazy">
      <strong>${producto.nombre}</strong>
      <span class="precio">$${producto.precio}</span>
      <p>Stock: ${producto.stock}</p>
      <button type="button" data-id="${producto.id}">Agregar al carrito</button>
    `;

    contenedorCatalogo.appendChild(tarjeta);

    // Conectamos con el carrito si existe la función
    tarjeta.querySelector("button").addEventListener("click", () => {
      if (typeof agregarAlCarrito === "function") {
        agregarAlCarrito(producto);
      }
    });
  });
}

// 2) fetch() le pide el archivo catalogo.json al servidor
fetch("catalogo.json")
  .then((respuesta) => respuesta.json())
  .then((productos) => {
    todosLosProductos = productos; // Guardamos la lista completa
    renderizarProductos(todosLosProductos); // Dibujamos todos los productos al inicio
  })
  .catch((error) => {
    contenedorCatalogo.innerHTML = "<p>No se pudo cargar el catálogo. Intenta más tarde.</p>";
    contenedorCatalogo.removeAttribute("aria-busy");
    contenedorCatalogo.removeAttribute("aria-label");
    console.error("Error al cargar catálogo:", error);
  });

// 3) Evento clic para los botones de filtro
botonesFiltro.forEach((boton) => {
  boton.addEventListener("click", () => {
    // Cambiamos la clase "activo" al botón presionado
    botonesFiltro.forEach((btn) => btn.classList.remove("activo"));
    boton.classList.add("activo");

    const categoria = boton.getAttribute("data-categoria");

    if (categoria === "Todos") {
      renderizarProductos(todosLosProductos);
    } else {
      // Filtramos la lista usando el atributo "categoria" de tu catalogo.json
      const filtrados = todosLosProductos.filter((p) => p.categoria === categoria);
      renderizarProductos(filtrados);
    }
  });
});