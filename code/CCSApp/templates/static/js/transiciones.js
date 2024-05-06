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

function redirigirIndextoEditarMateria() {
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
                document.getElementById(window.location.href = 'buscar_materia/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'buscar_materia/', true);
        xhttp.send();
    }, 500);
}

function redirigirIndextoEditarProfesor() {
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
                document.getElementById(window.location.href = 'buscar_profesor/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'buscar_profesor/', true);
        xhttp.send();
    }, 500);
}

function redirigirIndextoCrearEvento() {
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
                document.getElementById(window.location.href = 'crear_evento/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'crear_evento/', true);
        xhttp.send();
    }, 500);
}

function redirigirIndextoCrearActividad() {
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
                document.getElementById(window.location.href = 'crear_actividad/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'crear_actividad/', true);
        xhttp.send();
    }, 500);
}

function redirigirListaEspaciosDesdeEditarEspacio() {
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
                document.getElementById(window.location.href = '/index/servicios_asignacion/lista_edificios').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = '/index/servicios_asignacion/lista_edificios', true);
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

function redirigirGestionEliminarPrograma() {
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
                document.getElementById(window.location.href = 'eliminar_programa_academico/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'eliminar_programa_academico/', true);
        xhttp.send();
    }, 500);
}

function redirigirGestiondesdeNuevoPrograma() {
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
                document.getElementById(window.location.href = '/index/gestion').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = '/index/gestion', true);
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

function redirigirBuscarProfesor() {
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
                document.getElementById(window.location.href = 'buscar_profesor/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'buscar_profesor/', true);
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

function redirigirServiciosAsignaciondesdeAsignarHorario() {
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
                document.getElementById(window.location.href = '/index/programacion').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = '/index/programacion', true);
        xhttp.send();
    }, 500);
}

function redirigirAsignarHorario() {
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
                document.getElementById(window.location.href = 'asignar_horario/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'asignar_horario/', true);
        xhttp.send();
    }, 500);
}

function redirigirConsultarHorario() {
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
                document.getElementById(window.location.href = 'consultar_horarios/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'consultar_horarios/', true);
        xhttp.send();
    }, 500);
}

function redirigirServiciosAsignaciondesdeConsultarHorarios() {
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

function redirigirModificarHorario() {
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
                document.getElementById(window.location.href = 'modificar_horarios/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'modificar_horarios/', true);
        xhttp.send();
    }, 500);
}

function redirigirCrearEspacio() {
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
                document.getElementById(window.location.href = 'crear_espacio/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'crear_espacio/', true);
        xhttp.send();
    }, 500);
}

function redirigirEmpezarProgramacion() {
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
                document.getElementById(window.location.href = 'programacion/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'programacion/', true);
        xhttp.send();
    }, 500);
}

function redirigirIndexDesdeProgramacion() {
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

function redirigirListaEdificio() {
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
                document.getElementById(window.location.href = '/index/servicios_asignacion/lista_edificios').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = '/index/servicios_asignacion/lista_edificios', true);
        xhttp.send();
    }, 500);
}

function redirigirBuscarPrograma() {
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
                document.getElementById(window.location.href = 'buscar_programa_academico/').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = 'buscar_programa_academico/', true);
        xhttp.send();
    }, 500);
}

function redirigirBuscarDesdeEditarPrograma() {
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
                document.getElementById(window.location.href = '/index/gestion/buscar_programa_academico').classList.add("fade-in");
            }
        };
        xhttp.open("GET", window.location.href = '/index/gestion/buscar_programa_academico', true);
        xhttp.send();
    }, 500);
}