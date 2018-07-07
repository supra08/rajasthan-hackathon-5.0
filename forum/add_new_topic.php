<?php
 
$host="localhost"; // Host name 
$username="root"; // Mysql username 
$password="Arp31121997"; // Mysql password 
$db_name="myforum"; // Database name 
$tbl_name="fquestions"; // Table name 
 
// Connect to server and select database.
	$conn = new mysqli($host, $username, $password, $db_name);//for connection to databse via php
    if($conn->connect_error) {
	die("Connection failed :".$conn->connect_error);
}
 
// get data that sent from form 
$topic=$_POST['topic'];
$detail=$_POST['detail'];
$name=$_POST['name'];
$email=$_POST['email'];
 
$datetime=date("d/m/y h:i:s"); //create date time
 
$sql="INSERT INTO $tbl_name(topic, detail, name, email, datetime)VALUES('$topic', '$detail', '$name', '$email', '$datetime')";
$result=$conn->query($sql);
 
if($result){
echo "Successful<BR>";
echo "<a href=main_forum.php>View your topic</a>";
}
else {
echo "ERROR";
}
?>