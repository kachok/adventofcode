package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    //"math"
	"strconv"
	"sort"
)

func main() {
    dat, err := ioutil.ReadFile("03.input")
    
    if err != nil {
        panic(err)
    }

    //fmt.Print(string(dat))

	items := strings.Split(string(dat),"\n")
	
    var count int

    count=0

    for i:=0; i<len(items);i++ {
		//fmt.Print(items[i], len(items[i]))
		
		a,err:=strconv.Atoi(strings.TrimSpace(items[i][0:5]))    
		if err != nil {
			panic(err)
		}		
		b,err:=strconv.Atoi(strings.TrimSpace(items[i][5:10]))
		if err != nil {
			panic(err)
		}		
		c,err:=strconv.Atoi(strings.TrimSpace(items[i][10:15]))
		if err != nil {
			panic(err)
		}		
			
		tri:=[]int{a,b,c}
		sort.Ints(tri)
		
		//fmt.Print(tri[0],tri[1],tri[2],"\n")
		if tri[0]+tri[1]>tri[2]{
			count=count+1
		}

    }


    fmt.Print("answer is: ", count, "\n")
}
