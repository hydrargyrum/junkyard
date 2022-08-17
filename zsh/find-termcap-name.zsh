read -r "unk?Press ^V then press desired key: " && for k (${(k)termcap}) {
	if [[ "$unk" = "$termcap[$k]" ]] {
		echo "$k"
		return 0
	}
}
return 1
