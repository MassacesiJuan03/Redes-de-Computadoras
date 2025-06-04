<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Formulario Web</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <h1>Bienvenido a mi Formulario</h1>

    <!-- Logo de la UNCuyo -->
    <img src="https://www.uncuyo.edu.ar/assets/imgs/marca-uncuyo.svg" alt="Logo UNCuyo" width="200">

    <!-- Formulario -->
    <form id="miFormulario" method="POST" action="procesar.php" onsubmit="return validarFormulario(event)">
        <label for="email">Ingresá tu email:</label>
        <input type="text" id="email" name="email" required><br><br>

        <p>Elegí tu equipo favorito:</p>

        <label>
            <input type="radio" name="equipo" value="Boca">
            Boca Juniors 
            <img src="https://i.pinimg.com/736x/05/ac/17/05ac17fb09440e9071908ef00efef134.jpg" alt="Boca" class="img-equipo">
        </label><br>

        <label>
            <input type="radio" name="equipo" value="River">
            River Plate 
            <img src="https://www.cariverplate.com.ar/images/logo-river.png?cache=a57" alt="River" class="img-equipo">
        </label><br>

        <label>
            <input type="radio" name="equipo" value="Independiente">
            Independiente 
            <img src="https://i.pinimg.com/564x/1c/d6/7a/1cd67a933be1fd830dd1c9e0cbb6bb4e.jpg" alt="Independiente" class="img-equipo">
        </label><br>

        <label>
            <input type="radio" name="equipo" value="Racing">
            Racing Club 
            <img src="https://www.racingclub.com.ar/img/escudo/escudo2014.png" alt="Racing" class="img-equipo">
        </label><br>

        <label>
            <input type="radio" name="equipo" value="Estudiantes">
            Estudiantes de La Plata 
            <img src="https://images.seeklogo.com/logo-png/37/2/club-estudiantes-de-la-plata-buenos-aires-2019-logo-png_seeklogo-374424.png" alt="Estudiantes" class="img-equipo">
        </label><br>

        <label>
            <input type="radio" name="equipo" value="Otros">
            Otros
        </label><br><br>

        <button type="submit">Enviar</button>

        <div id="error"></div>
    </form>
    <script language="JavaScript">
    function validarFormulario(event) {
    	event.preventDefault(); // Evita que se envíe el formulario si hay errores

    	const email = document.getElementById("email").value.trim();
    	const opciones = document.getElementsByName("equipo");
    	const mensajeError = document.getElementById("error");
    	let errores = [];

    	// Validaciones del email
    	if (email.length < 7) {
        	errores.push("El email debe tener al menos 7 caracteres.");
    	}
    	if (!email.includes("@") || email.startsWith("@") || email.endsWith("@")) {
        	errores.push("El email debe contener '@' pero no al principio ni al final.");
    	}
    	if (!email.includes(".") || email.startsWith(".") || email.endsWith(".")) {
        	errores.push("El email debe contener un punto '.' pero no al principio ni al final.");
    	}
    	if (/[^a-zA-Z0-9@._\-]/.test(email)) {
        	errores.push("El email no debe contener caracteres especiales como #, !, %, $.");
    	}

    	// Validación de opción seleccionada
    	let selecciono = false;
    	for (let i = 0; i < opciones.length; i++) {
        	if (opciones[i].checked) {
            		selecciono = true;
            		break;
        	}
    	}
    	if (!selecciono) {
        	errores.push("Debe seleccionar una de las opciones.");
    	}

    	// Mostrar errores o enviar el formulario
    	if (errores.length > 0) {
        	mensajeError.innerHTML = errores.join("<br>");
        	mensajeError.style.color = "red";
    	} else {
        	mensajeError.innerHTML = "";
        	alert("Formulario enviado correctamente."); // solo para mostrar éxito
        	document.getElementById("miFormulario").submit(); // Envía el formulario
    	}
    }
    </script>
</body>
</html>
