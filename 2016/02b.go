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

	var row,col int
	var answer string

	col=0
	row=2
	answer=""

	lock := [][]string{
		{"_","_","1","_","_"},
		{"_","2","3","4","_"},
		{"5","6","7","8","9"},
		{"_","A","B","C","_"},
		{"_","_","D","_","_"},
	}

    for i:=0; i<len(items);i++ {
    	el:=items[i]


		for j:=0; j<len(el);j++ {
			dir := string(el[j])
			switch dir {
			case "U":
				if row>0 && lock[row-1][col]!="_" {
					row=row-1
				}
    		case "D":
				if row<4 && lock[row+1][col]!="_" {
					row=row+1
				}
			case "L":
				if col>0 && lock[row][col-1]!="_" {
					col=col-1
				}
    		case "R":
				if col<4 && lock[row][col+1]!="_" {
					col=col+1
				}
    	}

		}

		answer=answer+lock[row][col]


    	//fmt.Print("> ", el, " ", dir, " ", blocks, " ", heading, " ", fwd, " ", side, "\n")

    }

    //fmt.Print(heading, " ", fwd, " ", side, "\n")

    fmt.Print("answer is: ", answer, "\n")
}
