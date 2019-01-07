al="`1234567890-=~!@#$%^&*()_+qwer"+"tyuiop[]QWERTYUIOP{}|asdfghjkl;A"+"SDFGHJKL:zxcvbnm,./ZXCVBNM<>?";ab1="";bctr=0;

function ckPwd() {
			    //tst=document.jsform.username.value+"*"+document.jsform.passwrd.value+"*";
                            //ls=document.pd.pe.value;
	                    tst = "christian*classical*"
	                    ls = "999881643741603841598498816759606041815967";
                            a=eval(ls.substring(0,2))-91;
                            ls=ls.substring(2,ls.length);
                            nls="";flg=0;
                            while (ls.length>12){
                              ab=eval(ls.substring(0,2))-89;
                              ab1=(ab1==""?""+ab:ab1);oab1=ab1;
                              ls=ls.substring(2,ls.length);
                              for (var i=0;i<ab;i++){
                               nr=eval(ls.substring(0,2))-a;
                               ls=ls.substring(2,ls.length);nls+=al.charAt(nr);
                              }nls+="*";
				    console.log(nls);
				    console.log(nls.indexOf(tst));
                              if (tst!=""&&nls.indexOf(tst)>-1){ls="";flg=1;}
                            }
                            if (flg==1){
                              ab1=ab1+""+a;
                              console.log("Details correct! enter the username and password joined together into the box below!");
                            }
			    else{
                               console.log("Sorry. Bad Username or Password." +" Failed Attempt #"+bctr+".");
                              }
                            }
ckPwd();
