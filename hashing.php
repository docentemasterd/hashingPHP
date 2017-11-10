<?php
/* Get the posted value of the form if there is one */
$p = empty($_POST['p']) ? null : $_POST['p'];
?>
<html>
<head><title>Hash testing</title></head>
<style type="text/css">
    h1, h2, p {font-family: arial;}
    form {margin-left: 2%;}
    table {border-collapse: collapse; font-family: monospace; margin-left: 2%;}
    table, td, th {border: solid 1px #ccc;}
    th {background: #e1e1e1;border-color: #999;}
    td, th {padding: 0.25em;}
    td.algo {font-weight: bold;}
    tr.on td {background: #f0f0f0;}
</style>

<body>
    <h1>:: String hashing ::</h1>
    <form id="form" method="post" action="<?php echo basename(__FILE__) ?>">
        <p><label for="p">Introduce una cadena:</label><br /><input id="p" type="text" name="p" value="<?php echo $p ?>" /></p>
        <p><input type="submit" name="submit" value="Hash It!" /> &nbsp; <input type="reset" name="reset" value="Limpia" onClick="this.form.reset()" /></p>
        
    </form>
    
    <?php /* If there is a posted value use it */ ?>
    <?php if ($p): ?>
    <hr />
    <h2> [ Tabla de valores Hash para <em><?php echo $p ?></em> basada en algoritmos ]</h2>
    <table>
        <tr>
            <th>Algoritmo</th>
            <th>Valor del Hash de <em><?php echo $p ?></em></th>
        </tr>
        <?php /* Loop through each hash algorithm, colorizing every other row */ ?>
        <?php $on = false; foreach (hash_algos() as $algo): ?> 
        <tr<?php if ($on): ?> class="on"<?php endif; ?>>
            <td class="algo"><?php echo $algo ?></td>
            <td class="hash"><?php echo hash($algo, $p) ?></td>
        </tr>
    <?php $on = !$on; endforeach; ?> 
    </table>
    <?php endif; ?>
</body>
</html>
