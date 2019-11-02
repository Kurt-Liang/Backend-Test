<html>
    <head>
        <title>PHP Test</title>
    </head>
    <body>
        <?PHP
            $Link = mysql_connect('localhost', 'root', 'backendtest');
            if (!$Link) {
                $cont = array(
                    "mysql_status" => "ERROR"
                );
                die(json_encode($cont));
            }
            $cont = array(
                "mysql_status" => "OK"
            );
            echo json_encode($cont);
            mysql_close($Link);
        ?>
    </body>
</html>
