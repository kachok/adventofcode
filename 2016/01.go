package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "math"
    "strconv"
)

func main() {
    dat, err := ioutil.ReadFile("01.input")
    
    if err != nil {
        panic(err)
    }

    fmt.Print(string(dat))

    items := strings.Split(strings.TrimSpace(string(dat)),", ")

    fmt.Print(items)

    var heading int
    var fwd int
    var side int

    heading=0
    fwd=0
    side=0

    for i:=0; i<len(items);i++ {
    	el:=items[i]
    	dir:=string(el[0])
    	blocks, err:=strconv.Atoi(strings.TrimPrefix(el,string(el[0])))
	    if err != nil {
	        panic(err)
	    }

    	switch dir {
    		case "L":
    			heading=int(math.Mod(float64(360+heading-90), 360))
    		case "R":
    			heading=int(math.Mod(float64(360+heading+90), 360))
    	}

    	switch heading {
    		case 0:
    			fwd=fwd+blocks
    		case 90:
    			side=side+blocks
    		case 180:
    			fwd=fwd-blocks
    		case 270:
    			side=side-blocks
    	}

    	fmt.Print("> ", el, " ", dir, " ", blocks, " ", heading, " ", fwd, " ", side, "\n")

    }

    fmt.Print(heading, " ", fwd, " ", side, "\n")

    fmt.Print("blocks away: ", fwd+side, "\n")
}
