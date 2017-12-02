package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "math"
    "strconv"
    "os"
)

func main() {
    dat, err := ioutil.ReadFile("01.input")
    
    if err != nil {
        panic(err)
    }

    //fmt.Print(string(dat))

    items := strings.Split(strings.TrimSpace(string(dat)),", ")

    //fmt.Print(items)

    var heading int
    var fwd int
    var side int

    var places map[string]int
    places = make(map[string]int)

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

    	//need to add every step of the way (block) to the map
    	switch heading {
    		case 0:
    			//for i:=0; i<blocks;i++ {
    			//	fwd=fwd+1
    			//	places[strconv.Itoa(fwd)+":"+strconv.Itoa(side)]=1
    			//}
    			fwd=fwd+blocks
    		case 90:
    			side=side+blocks
    		case 180:
    			fwd=fwd-blocks
    		case 270:
    			side=side-blocks
    	}

    	if val, ok := places[strconv.Itoa(fwd)+":"+strconv.Itoa(side)]; ok {
    		val=val+1
    		//do something here
    		//fmt.Println(val)
    		fmt.Println(">>>>> ", el, " ", dir, " ", blocks, " ", heading, " ", fwd, " ", side, "\n")

    		fmt.Print("blocks away: ", fwd+side, "\n")
    		os.Exit(0)

		}

		places[strconv.Itoa(fwd)+":"+strconv.Itoa(side)]=1

		fmt.Println(strconv.Itoa(fwd)+":"+strconv.Itoa(side))

    	//fmt.Print("> ", el, " ", dir, " ", blocks, " ", heading, " ", fwd, " ", side, "\n")

    }

    fmt.Print(heading, " ", fwd, " ", side, "\n")

    fmt.Print("blocks away: ", fwd+side, "\n")
}
