#!/usr/bin/env bash
# make an executable script checking for the sytesl of it

if [ $# -ne 1 ]; then
	echo "Usage: <./make_script.h> <script name>"
	exit
fi

if [ -e "$1" ]; then
	echo "File exists already"
	exit
fi
echo "#!/usr/bin/env bash" > "$1"
vi "$1"
chmod +x "$1"
shellcheck "$1"
./$1
