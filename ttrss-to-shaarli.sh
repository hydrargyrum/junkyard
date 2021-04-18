#!/bin/sh -e
# import TinyTinyRSS starred articles into Shaarli

get_atom_page () {
	page=$1
	offset=$((page * 30))
	curl \
		-s \
		"${TTRSS_URL%/}/public.php?op=rss&id=-1&key=$TTRSS_TOKEN&limit=30&offset=$offset"
}

atom_extract () {
	xmlstarlet \
		sel \
		-N A=http://www.w3.org/2005/Atom \
		-t \
		-m //A:entry \
		-v A:title -n \
		-v A:link/@href -n
}

generate_jwt () {
	python3 <<- EOF
		import os
		from time import time
		from jose import jwt
		print(jwt.encode(
			{"iat": int(time())},
			os.environ["SHAARLI_TOKEN"],
			algorithm="HS512"
		))
	EOF
}


post_shaarli () {
	url=$1
	title=$2

	json=$(cat <<- EOF
		{
			"url": "$url", "title": "$title",
			"private": true
		}
		EOF
	)

	curl \
		-s \
		-H "Authorization: Bearer $(generate_jwt)" \
		"${SHAARLI_URL%/}/api/v1/links" \
		-d "$json" \
		-H 'Accept: application/json' \
		-H 'Content-Type: application/json'
}

check () {
	which xmlstarlet 2>/dev/null >&2 || {
		printf "please install xmlstarlet\n" >&2
		exit 1
	}
	which curl 2>/dev/null >&2 || {
		printf "please install curl\n" >&2
		exit 1
	}
	python3 -c "import jose" 2>/dev/null >&2 || {
		printf "please install PyJWT\n" >&2
		exit 1
	}

	for var in SHAARLI_TOKEN SHAARLI_URL TTRSS_URL TTRSS_TOKEN
	do
		env | grep -q "^$var=" || {
			printf "please set %s\n" "$var" >&2
			exit 1
		}
	done
}

main () {
	for i in $(seq 0 300)
	do
		printf "extracting page %s\n" "$i"
		get_atom_page "$i" \
			| atom_extract \
			| while read -r title
			do
				read -r url
				printf "%s\n" "$url"
				post_shaarli "$url" "$title"
			done \
			| grep .
	done
}

check
main
