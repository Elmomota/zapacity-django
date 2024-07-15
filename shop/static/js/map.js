// Inicializar el mapa con una vista centrada en Santiago de Chile
var map = L.map('map').setView([-33.4372, -70.6506], 10);

// Añadir una capa de azulejos de OpenStreetMap al mapa
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Definir ubicaciones aleatorias para las tiendas en Santiago de Chile
var santiagoLocations = [
    [-33.4489, -70.6631], // Tienda 1
    [-33.4248, -70.6058], // Tienda 2
    [-33.4691, -70.6420], // Tienda 3
    [-33.4567, -70.6489]  // Tienda 4
];

// Añadir marcadores para las tiendas en Santiago de Chile
santiagoLocations.forEach(function (location, index) {
    L.marker(location).addTo(map)
        .bindPopup("Tienda " + (index + 1));
});

// Añadir una tienda en Valparaíso
L.marker([-33.0472, -71.6127]).addTo(map)
    .bindPopup("Tienda en Valparaíso");

// Manejar eventos de clic en el mapa
function onMapClick(e) {
    // Mostrar un mensaje con las coordenadas del clic
    alert("Haz hecho clic en el mapa en la ubicación: " + e.latlng);
}
map.on('click', onMapClick);