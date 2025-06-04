<?php
// Obtener datos del formulario
$email = $_POST['email'];
$equipo = $_POST['equipo'];

// Archivos
$archivoEmails = 'emails.txt';
$archivoVotos = 'votos.json';

// Leer emails existentes
$emailsAnteriores = file_exists($archivoEmails) ? file($archivoEmails, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) : [];

// Leer votos existentes
$votos = file_exists($archivoVotos) ? json_decode(file_get_contents($archivoVotos), true) : [];

// Verificar si ya votó
if (in_array($email, $emailsAnteriores)) {
    echo "<h2>Usted ya votó. No puede votar dos veces.</h2>";
} else {
    // Guardar email
    file_put_contents($archivoEmails, $email . PHP_EOL, FILE_APPEND);

    // Verificar que el equipo este en el array
    if (!isset($votos[$equipo])) {
        $votos[$equipo] = 0;
    }

    // Sumar el voto
    $votos[$equipo]++;

    // Guardar votos
    file_put_contents($archivoVotos, json_encode($votos));
    echo "<h2>¡Gracias por votar!</h2>";
}

// Mostrar resultados
echo "<h3>Resultados actuales:</h3><ul>";
foreach ($votos as $equipo => $cantidadVotos) {
    echo "<li><strong>$equipo:</strong> $cantidadVotos voto(s)</li>";
}
echo "</ul>";

echo '<br><a href="index.php">Volver</a>';
?>

