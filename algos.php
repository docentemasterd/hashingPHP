<!DOCTYPE html>
<html>
<head>
<title>Hashes PHP</title>
<style>
p{
        font-family: monospace;
        font-size: 10px;
        margin-left: 30px;
}
</style>
<head>
<body>
        <h1>Hash de la cadena "Hola"</h1>
        <p class="parrafo">

        <?php
        $data = "Hola";

        foreach (hash_algos() as $v) {
                $r = hash($v, $data, false);
                printf("%-12s %3d %s \n", $v, strlen($r), $r);
                echo "<br />";
        }
        ?>

        </p>
</body>
</html>
