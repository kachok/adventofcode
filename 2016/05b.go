package main

import (
	"crypto/md5"
	"fmt"
	"strconv"
	"encoding/hex"
	"strings"
)



func main() {

	i:=0
	//input:="abc"
	input:="reyedfim"

	answer:="________"

	for {
		text:=input+strconv.Itoa(i)
		hasher := md5.New()
		hasher.Write([]byte(text))

		hash:=hex.EncodeToString(hasher.Sum(nil))

		//fmt.Print(text, " ",hash,"\n")

		i=i+1
		if hash[0:5]=="00000" {
			fmt.Print(">",hash[5]," " ,hash[6],"\n")
			if hash[5]<8+48 {
				fmt.Print(hash[5]," ",hash[6],"\n")
				out := []rune(answer)
				if out[hash[5]-48]==95 {
					out[hash[5]-48] = rune(int(hash[6]))
					answer=string(out)
					fmt.Print(answer,"\n")
				}
			}
		}

		if strings.Contains(answer,"_")==false {break}
	}
	

    fmt.Print("answer is: ",answer,"\n")
}

