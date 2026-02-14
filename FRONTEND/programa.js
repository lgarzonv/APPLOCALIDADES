// URL base de tu API local
let url = "http://127.0.0.1:8000/";

// Capturamos elementos del DOM
const select = document.getElementById("opciones");
const boton = document.getElementById("obtener");

// Evento del botón
boton.addEventListener("click", function () {
    const localidad = select.value;
    console.log("Localidad seleccionada:", localidad);

    crearPeticion(localidad);
});

// Función que recibe la localidad
async function crearPeticion(localidad) {

    // Construimos la URL con parámetro dinámico
    let myAPI = `${url}?localidad=${localidad}`;

    try {
        let response = await fetch(myAPI);

        if (!response.ok) {
            throw new Error("Error en la respuesta del servidor");
        }

        let datos = await response.json();

        console.log("GeoJSON recibido:", datos);

    } catch (error) {
        console.error("Error:", error);
    }
}