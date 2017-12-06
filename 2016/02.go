package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    //"math"
    //"strconv"
)

func main() {
    dat, err := ioutil.ReadFile("02.input")
    
    if err != nil {
        panic(err)
    }

    fmt.Print(string(dat))

    items := strings.Split(string(dat),"\n")

    fmt.Print("\n>>>>\n")
	
	fmt.Print(len(items))

	fmt.Print("\n>>>>\n")

	var curr int
	var answer int

	curr=0
	answer=0


    for i:=0; i<len(items);i++ {
    	el:=items[i]


		for j:=0; j<len(el);j++ {
			dir := string(el[j])
			switch dir {
			case "U":
				if curr-3>0 {
					curr=curr-3
				}
    		case "D":
				if curr+3<10 {
					curr=curr+3
				}    		
			case "L":
				if (curr-1-1)/3==(curr-1)/3 {
					curr=curr-1
				}    		
    		case "R":
				if (curr-1+1)/3==(curr-1)/3 {
					curr=curr+1
				}    		
    	}

		}

		answer=answer*10+curr


    	//fmt.Print("> ", el, " ", dir, " ", blocks, " ", heading, " ", fwd, " ", side, "\n")

    }

    //fmt.Print(heading, " ", fwd, " ", side, "\n")

    fmt.Print("answer is: ", answer, "\n")
}
