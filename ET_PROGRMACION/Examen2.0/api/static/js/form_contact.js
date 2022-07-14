$(document).ready(
    function(){
        $("#error_contacto").hide();

        $("#formulario-ingreso").submit(
            function(){
                let contacto_nombre   = $("#contacto_nombre").val();
                let contacto_email    = $("#contacto_email").val();
                let contacto_telefono = $("#contacto_telefono").val();
                let comentario        = $("#comentario").val();

                let mensaje_error_contacto = '<h3>Ingrese los siguientes Datos</h3>';
                mensaje_error_contacto += "<ul>";

                if (contacto_nombre.trim() == '') {
                    mensaje_error_contacto += "<li>Ingrese su nombre </li>";
                }
                
                if (contacto_email.trim() == '') {
                    mensaje_error_contacto += "<li>Ingrese email </li>";
                }
                
                if (contacto_telefono.trim() != '') {
                    if(contacto_telefono.trim().length < 9 || contacto_telefono.trim().length > 9){
                        mensaje_error_contacto += "<li>Ingrese un numero válido </li>";
                    }
                }

                if (comentario.trim().length < 100) {
                    mensaje_error_contacto += "<li>Ingrese un comentario de al menos 100 caracteres </li>";
                }
                    
                mensaje_error_contacto += "</ul>";

                console.log(mensaje_error_contacto.length)
                if (mensaje_error_contacto.length > 46){
                    $("#error_contacto").html(mensaje_error_contacto);
                    $("#error_contacto").show();
                }else{
                    $("#error_contacto").hide();
                }

                event.preventDefault();
            }
        )
    }
);