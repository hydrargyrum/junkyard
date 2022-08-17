for k (${(k)termcap}) {
	printf "-----\n%s\n" "$k"
	printf %s "${termcap[$k]}" | xxd
}
