<head>
    <title>Show Movies</title>
</head>
<body>
<?php

function outputResultsTableHeader() {
    echo "<tr>";
    echo "<th> titleID </th>";
    echo "<th> title </th>";
    echo "<th> language </th>";
    echo "<th> isAdult </th>";
    echo "<th> startYear </th>";
    echo "<th> runtime </th>";
    echo "<th> genres </th>";
    echo "<th> directors </th>";
    echo "</tr>";
}

//now we need to open the dbase connection 
include 'open.php';

//error settings from demo
ini_set('error_reporting', E_ALL);
ini_set('display_errors', true);

//Collect data input posted here from calling page. We called ours titleID
$titleID = $_POST['titleID'];

//Calling the stored procedure named ShowMovies in our setup sql script

if ($mysqli->multi_query("CALL ShowMovies('".$titleID."');")) {
    //Check if result was returned after call
    if ($result = $mysqli->store_result()) {
        echo "<table border=\"1px solid black\">";
        $row = $result->fetch_row();

        //If had an Error then indicates error
        if (strcmp($row[0], 'ERROR: ') == 0) {
            echo "<tr><th> Result </th></tr>";
            do {
                echo "<tr><td>";
                for ($i = 0; $i < sizeof($row); $i++) {
                    echo $row[$i];
                }
                echo "</td></tr>";
            } while ($row = $result->fetch_row());
        // If no error, received actual results so we should output the table
        } else {
            outputResultsTableHeader();
            do {
                echo "<tr>";
                for ($i = 0; $i < sizeof($row); $i++) {
                    echo "<td>" . $row[$i] . "</td>";
                } 
                echo "</tr>";
            } while ($row = $result->fetch_row());
        }
        echo "</table>";
        $result->close();
    }
} else {
        printf("<br>EROROROROR: %s\n", $mysqli->error); 
}
//Close connection
mysqli_close($mysqli);

?>
</body>
