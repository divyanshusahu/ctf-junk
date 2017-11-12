bin = ''
for (i=0;i<750000;i++)
{
	if (arrOriginal[i]!=arrInfected[i])
	{
		if (arrInfected[i]%2==0)
			bin += '0';
		else
			bin += '1';
	}
}
flag = ''
c = ''
for (i=0;i<bin.length;i++)
{
	c = c + bin[i]
	if (i%8 == 7)
	{
		x = parseInt(c,2)
		flag = flag +String.fromCharCode(x)
		c = ''
	}
}

console.log(flag)