function redirigirIndex() {
    document.getElementById("page1").classList.add("fade-out");
    
    setTimeout(function() {
        // Ocultar la página 1
        document.getElementById("page1").style.display = "none";
        
        // Cargar la página 2 usando AJAX
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                // Insertar el contenido de la página 2 en el DOM
                document.getElementById("page-container").innerHTML = this.responseText;
                
                // Aplicar la animación de entrada a la página 2
                document.getElementById(window.location.href = '/index').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = '/index', true);
        xhttp.send();
    }, 500);
}

function redirigirPrincipal() {
    document.getElementById("page1").classList.add("fade-out");
    
    setTimeout(function() {
        // Ocultar la página 1
        document.getElementById("page1").style.display = "none";
        
        // Cargar la página 2 usando AJAX
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                // Insertar el contenido de la página 2 en el DOM
                document.getElementById("page-container").innerHTML = this.responseText;
                
                // Aplicar la animación de entrada a la página 2
                document.getElementById(window.location.href = '/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = '/', true);
        xhttp.send();
    }, 500);
}

function redirigirGestion() {
    document.getElementById("page1").classList.add("fade-out");
    
    setTimeout(function() {
        // Ocultar la página 1
        document.getElementById("page1").style.display = "none";
        
        // Cargar la página 2 usando AJAX
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                // Insertar el contenido de la página 2 en el DOM
                document.getElementById("page-container").innerHTML = this.responseText;
                
                // Aplicar la animación de entrada a la página 2
                document.getElementById(window.location.href = 'gestion/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'gestion/', true);
        xhttp.send();
    }, 500);
}

function redirigirServiciosAsignacion() {
    document.getElementById("page1").classList.add("fade-out");
    
    setTimeout(function() {
        // Ocultar la página 1
        document.getElementById("page1").style.display = "none";
        
        // Cargar la página 2 usando AJAX
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                // Insertar el contenido de la página 2 en el DOM
                document.getElementById("page-container").innerHTML = this.responseText;
                
                // Aplicar la animación de entrada a la página 2
                document.getElementById(window.location.href = 'servicios_asignacion/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'servicios_asignacion/', true);
        xhttp.send();
    }, 500);
}

function redirigirRegistro() {
    document.getElementById("page1").classList.add("fade-out");
    
    setTimeout(function() {
        // Ocultar la página 1
        document.getElementById("page1").style.display = "none";
        
        // Cargar la página 2 usando AJAX
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                // Insertar el contenido de la página 2 en el DOM
                document.getElementById("page-container").innerHTML = this.responseText;
                
                // Aplicar la animación de entrada a la página 2
                document.getElementById(window.location.href = '/register_us').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = '/register_us', true);
        xhttp.send();
    }, 500);
}

function redirigirNuevoPrograma() {
    document.getElementById("page1").classList.add("fade-out");
    
    setTimeout(function() {
        // Ocultar la página 1
        document.getElementById("page1").style.display = "none";
        
        // Cargar la página 2 usando AJAX
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                // Insertar el contenido de la página 2 en el DOM
                document.getElementById("page-container").innerHTML = this.responseText;
                
                // Aplicar la animación de entrada a la página 2
                document.getElementById(window.location.href = 'nuevoprograma/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'nuevoprograma/', true);
        xhttp.send();
    }, 500);
}

function redirigirRegistrarMateria() {
    document.getElementById("page1").classList.add("fade-out");
    
    setTimeout(function() {
        // Ocultar la página 1
        document.getElementById("page1").style.display = "none";
        
        // Cargar la página 2 usando AJAX
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                // Insertar el contenido de la página 2 en el DOM
                document.getElementById("page-container").innerHTML = this.responseText;
                
                // Aplicar la animación de entrada a la página 2
                document.getElementById(window.location.href = 'registroMateria/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'registroMateria/', true);
        xhttp.send();
    }, 500);
}

function redirigirRegistrarProfesor() {
    document.getElementById("page1").classList.add("fade-out");
    
    setTimeout(function() {
        // Ocultar la página 1
        document.getElementById("page1").style.display = "none";
        
        // Cargar la página 2 usando AJAX
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                // Insertar el contenido de la página 2 en el DOM
                document.getElementById("page-container").innerHTML = this.responseText;
                
                // Aplicar la animación de entrada a la página 2
                document.getElementById(window.location.href = 'registroProfesor/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'registroProfesor/', true);
        xhttp.send();
    }, 500);
}

function redirigirServiciosAsignaciondesdeRegistro() {
    document.getElementById("page1").classList.add("fade-out");
    
    setTimeout(function() {
        // Ocultar la página 1
        document.getElementById("page1").style.display = "none";
        
        // Cargar la página 2 usando AJAX
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                // Insertar el contenido de la página 2 en el DOM
                document.getElementById("page-container").innerHTML = this.responseText;
                
                // Aplicar la animación de entrada a la página 2
                document.getElementById(window.location.href = '/index/servicios_asignacion').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = '/index/servicios_asignacion', true);
        xhttp.send();
    }, 500);
}