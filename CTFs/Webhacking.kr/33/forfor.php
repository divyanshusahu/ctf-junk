<?php

$ip = "103.37.200.100";

for($i=0;$i<=strlen($ip);$i++)
{
	$ip=str_replace($i,ord($i),$ip);
}

$ip=str_replace(".","",$ip);

$ip=substr($ip,0,10);

$answer=$ip*2;
$answer=$ip/2;
$answer=str_replace(".","",$answer);

echo $ip;
echo "\n".$answer;
echo "\n"."answerip/$ip/$answer.$ip"

// 3bfc3838c9244fa00a7c6bb47e19b1f8
?>
