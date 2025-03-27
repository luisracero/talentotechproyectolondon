// Obtener el mes y año actual
const date = new Date();
const month = date.getMonth(); // Mes actual (0-11)
const year = date.getFullYear(); // Año actual

// Nombres de los meses
const monthNames = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
];

// Actualizar el título del calendario
document.getElementById("month-year").textContent = `${monthNames[month]} ${year}`;

// Obtener el primer día del mes y el número de días en el mes
const firstDay = new Date(year, month, 1).getDay(); // Día de la semana del primer día (0-6)
const daysInMonth = new Date(year, month + 1, 0).getDate(); // Número de días en el mes

// Generar los días del mes
const daysContainer = document.getElementById("days");
daysContainer.innerHTML = ""; // Limpiar el contenedor

// Añadir celdas vacías para los días anteriores al primer día del mes
for (let i = 0; i < firstDay; i++) {
    const emptyDay = document.createElement("li");
    emptyDay.classList.add("empty");
    daysContainer.appendChild(emptyDay);
}

// Añadir los días del mes
for (let day = 1; day <= daysInMonth; day++) {
    const dayElement = document.createElement("li");
    dayElement.textContent = day;

    // Resaltar el día actual
    if (day === date.getDate() && month === new Date().getMonth() && year === new Date().getFullYear()) {
        dayElement.style.backgroundColor = "#007bff";
        dayElement.style.color = "#fff";
    }

    daysContainer.appendChild(dayElement);
}