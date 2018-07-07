<?php
 $targetfolder = "testupload/";
 $targetfolder = $targetfolder . basename( $_FILES['file']['name']) ;
if(move_uploaded_file($_FILES['file']['tmp_name'], $targetfolder))
 {
	 echo "The file ". basename( $_FILES['file']['name']). " is uploaded"."\n";
	 // echo $targetfolder;
	 $aContext = array(
	    'http' => array(
	        'proxy' => 'localhost:5000',
	        'request_fulluri' => true,
	    ),
	);
	$cxContext = stream_context_create($aContext);

	$url = "/imgurl/../".$targetfolder;

	$sFile = file_get_contents("", False, $cxContext);

	echo 'The job search tags are '.$sFile;
 }
 else {
 	echo "Problem uploading file";
 }
 ?>
