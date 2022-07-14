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

$(document).ready(
    function(){
        $("#errorRegister").hide();

        $("#formRegister").submit(
            function(){
                let register_email     = $("#emailRegister").val();
                let register_nombre    = $("#nameRegister").val();
                let register_contraseña = $("#passRegister").val();

                let mensaje_error_register = '<h5>Faltan los siguientes Datos</h5>';
                mensaje_error_register += "<ul>";

                if (register_email.trim() == '') {
                    mensaje_error_register += "<li>Ingrese su email </li>";
                }
                
                if (register_nombre.trim() == '') {
                    mensaje_error_register += "<li>Ingrese su nombre </li>";
                }

                if (register_contraseña.trim() == '') {
                    mensaje_error_register += "<li>Ingrese una contraseña </li>";
                }
                    
                mensaje_error_register += "</ul>";

                console.log(mensaje_error_register.length)
                if (mensaje_error_register.length > 46){
                    $("#errorRegister").html(mensaje_error_register);
                    $("#errorRegister").show();
                }else{
                    $("#errorRegister").hide();
                }

                event.preventDefault();
            }
        )
    }
);

$(document).ready(
    function(){
        $("#errorLogin").hide();

        $("#formLogin").submit(
            function(){
                let emailLogin    = $("#emailLogin").val();
                let passLogin     = $("#passLogin").val();

                let mensaje_error_login = '<h5>Ingrese los siguientes Datos</h5>';
                mensaje_error_login += "<ul>";

                if (emailLogin.trim() == '') {
                    mensaje_error_login += "<li>Ingrese email </li>";
                }
                
                if (passLogin.trim() == '') {
                    mensaje_error_login += "<li>Ingrese contraseña </li>";
                }
                    
                mensaje_error_login += "</ul>";

                console.log(mensaje_error_login.length)
                if (mensaje_error_login.length > 46){
                    $("#errorLogin").html(mensaje_error_login);
                    $("#errorLogin").show();
                }else{
                    if(emailLogin.trim() == 'admin@duoc.cl'){
                        if (passLogin.trim() == 'admin123'){
                            url = "/login-admin";
                            $(location).attr('href',url);
                        
                        }else{
                            mensaje_error_login += "<li>La contraseña es erronea</li>";
                        }
                    }
                    if(emailLogin.trim() == '{{}}'){
                        if (passLogin.trim() == 'user123'){
                            url = "/usuario";
                            $(location).attr('href',url);
                        
                        }else{
                            mensaje_error_login += "<li>La contraseña es erronea</li>";
                        }
                    }else{
                        mensaje_error_login += "<li>Verificar email y contraseña</li>";
                    }
                    console.log(mensaje_error_login.length)
                    if (mensaje_error_login.length > 46){
                        $("#errorLogin").html(mensaje_error_login);
                        $("#errorLogin").show();
                    }else{
                        $("#errorLogin").hide();
                    }
                    event.preventDefault();
                }  
                event.preventDefault();
            
            }
        )
    }
);