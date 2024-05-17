document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('registro-materia-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevenir el envío del formulario por defecto
        
        // Mostrar el cuadro emergente de confirmación
        mostrarModal();

        // Opcional: puedes agregar un temporizador para ocultar el cuadro emergente después de un tiempo determinado
        setTimeout(function() {
            cerrarModal();
        }, 3000); // 3000 milisegundos = 3 segundos

        // Envía el formulario después de un breve retraso (si es necesario)
        setTimeout(function() {
            form.submit();
        }, 1000); // 1000 milisegundos = 1 segundo
    });

    // Verificar si hay un error al cargar la página y mostrar el modal de error si es necesario
    var errorDiv = document.querySelector('.error-message');
    if (errorDiv) {
        // Si hay un error, mostrar el modal de error
        var errorMessage = errorDiv.textContent.trim();
        mostrarModalError(errorMessage);
    }
});

// Función para mostrar el modal de error
function mostrarModalError(errorMessage) {
    var modal = document.getElementById("modal-error");
    var mensajeError = document.getElementById("error-message-modal");
    mensajeError.textContent = errorMessage;
    modal.style.display = "block";
}

// Función para cerrar el modal de error
function cerrarModalError() {
    var modal = document.getElementById("modal-error");
    modal.style.display = "none";
}

// Función para mostrar el cuadro emergente de confirmación
function mostrarModal() {
    var modal = document.getElementById("modal-confirmacion");
    modal.style.display = "block";
}

// Función para cerrar el cuadro emergente de confirmación
function cerrarModal() {
    var modal = document.getElementById("modal-confirmacion");
    modal.style.display = "none";
}


