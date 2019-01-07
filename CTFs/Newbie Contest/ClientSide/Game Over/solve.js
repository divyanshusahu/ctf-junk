var tabc = "3696619";
var tab = "                   azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789_$&#@";
var password = "souris";
var login = "~";

for (var no = 0; no < 1 /*tabc.length*/ ; no++) {
    checksum = tabc[no];
    var nblog = login.length;
    var nbpass = password.length;
    var sum = 1;
    var n = Math.max(nblog, nbpass)
    for (var i = 0; i < n; i++) {
        var index1 = tab.indexOf(login.substring(i, i + 1)) + 10;
        var index2 = tab.indexOf(password.substring(i, i + 1)) + 10;
        sum = sum + (index1 * n * (i + 1)) * (index2 * (i + 1) * (i + 1));
        console.log(index2, index1);
    }
    //console.log(sum);
    //console.log(checksum);
}
/*

	var total_erreur=0;
	function Check() {
	var tabc=Check.arguments; var ok=0;
	var tab="                   azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789_$&#@";
	for (var no=0;no<tabc.length;no++) {
		checksum=tabc[no];
		var login=document.forms["flog"].elements["login"].value;
		var password="souris";
		var nblog=login.length;
		var nbpass=password.length;
		var sum=1;
		var n=Math.max(nblog,nbpass)
		for (var i=0;i<n;i++) {
			var index1=tab.indexOf(login.substring(i,i+1))+10;
			var index2=tab.indexOf(password.substring(i,i+1))+10;
			sum=sum+(index1*n*(i+1))*(index2*(i+1)*(i+1));
		}
        if (sum==checksum) {
			window.location="/epreuves/javascript/"+login+".php"; ok=1; no=100;
		}

	}
	if (ok==0) {
		total_erreur++;
		alert("Mauvais login ou mot de passe");
		if (total_erreur>2) {
			alert("Vous avez atteint les 3 essais !\nAu revoir");
			window.location="index.php";
		}
	}
	}
	function Verifie() {
	Check(3696619)
	}

*/