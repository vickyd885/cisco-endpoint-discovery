<?php
# Author: German Cheung

include_once('axl.class.php');
error_reporting(0);

/*
* First get a list of devices from AXL API
*/


// if (isset($argc)) {
// 	for ($i = 0; $i < $argc; $i++) {
// 		echo "Argument #" . $i . " - " . $argv[$i] . "\n";
// 	}
// }
// 	else {
// 	echo "argc and argv disabled\n";
// }

$username = $argv[1] ;
$password = $argv[2] ;
$server = $argv[3] ;

// The query, adjust as needed
$DEVICES_SQL = '
	SELECT device.name AS devicename, typemodel.name AS model, device.description as description FROM device
	JOIN typemodel ON device.tkmodel=typemodel.enum
	WHERE typemodel.name LIKE "Cisco TelePresence MX%"
';

// Get AXL client and run the sql query
$_axl = new AXL($username, $password, $server);
$axl_result = $_axl->doRequest('ExecuteSQLQuery', array('sql' => $DEVICES_SQL));

print_r(json_encode($axl_result->return->row));
