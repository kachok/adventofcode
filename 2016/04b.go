package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    //"math"
	"strconv"
	//"sort"
)

func main() {
    dat, err := ioutil.ReadFile("04.input")
    
    if err != nil {
        panic(err)
    }

    //fmt.Print(string(dat))

	items := strings.Split(string(dat),"\n")
	

    for i:=0; i<len(items);i++ {
		//fmt.Print(items[i], len(items[i]))
		items[i]=items[i][0:len(items[i])-7]
		letters:=strings.Split(items[i],"-")
		
		id,err:=strconv.Atoi(letters[len(letters)-1])
		if err != nil {
			panic(err)
		}	
		letters=letters[:len(letters)-1]

		abc:=strings.Join(letters," ")
		

		plain:=""
		for _, ch:=range abc{
			if ch!=rune(32) {
				ch=rune((((int(ch)-97)+id) % 26) +97)
			}
			plain=plain+string(ch)
			//fmt.Print(plain," ",index,ch, " ",string(ch), " ",id, "\n")

			
		}
		fmt.Print(plain," ",id, "\n")
    }


    fmt.Print("answer is: northpole object storage 501\n")
}

