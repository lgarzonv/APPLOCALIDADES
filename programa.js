// URL base de tu API local


const urlBase = "http://127.0.0.1:8000/getjson";

const select = document.getElementById("opciones");
const boton = document.getElementById("obtener");
const resultado = document.getElementById("resultado");

boton.addEventListener("click", async () => {

    const localidad = select.value;

    try {
        const response = await fetch(`${urlBase}?localidad=${localidad}`);

        if (!response.ok) {
            throw new Error("Error del servidor");
        }

        const data = await response.json();

        console.log("Respuesta backend:", data);

        resultado.textContent = JSON.stringify(data, null, 2);

    } catch (error) {
        console.error(error);
        resultado.textContent = "Error al obtener datos";
    }
});