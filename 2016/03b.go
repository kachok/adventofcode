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

    for i:=0; i<len(items)/3;i++ {
		//fmt.Print(items[i], len(items[i]))
		
		for j:=0;j<3;j++{
			a,err:=strconv.Atoi(strings.TrimSpace(items[i*3][j*5+0:j*5+5]))    
			if err != nil {
				panic(err)
			}		
			b,err:=strconv.Atoi(strings.TrimSpace(items[i*3+1][j*5+0:j*5+5]))
			if err != nil {
				panic(err)
			}		
			c,err:=strconv.Atoi(strings.TrimSpace(items[i*3+2][j*5+0:j*5+5]))
			if err != nil {
				panic(err)
			}		
				
			tri:=[]int{a,b,c}
			sort.Ints(tri)
			
			fmt.Print(tri[0],tri[1],tri[2],"\n")
			if tri[0]+tri[1]>tri[2]{
				count=count+1
			}
		}


    }


    fmt.Print("answer is: ", count, "\n")
}
