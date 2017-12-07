package main

import (
	"crypto/md5"
	"fmt"
	"strconv"
    "encoding/hex"
)



func main() {

	i:=0
	input:="reyedfim"

	answer:=""

	for {
		text:=input+strconv.Itoa(i)
		hasher := md5.New()
		hasher.Write([]byte(text))

		hash:=hex.EncodeToString(hasher.Sum(nil))

		//fmt.Print(text, " ",hash,"\n")

		i=i+1
		if hash[0:5]=="00000" {
			answer=answer+string(hash[5])
		}

		if len(answer)==8 {break}
	}
	

    fmt.Print("answer is: ",answer,"\n")
}

