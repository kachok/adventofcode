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
    dat, err := ioutil.ReadFile("04.input")
    
    if err != nil {
        panic(err)
    }

    //fmt.Print(string(dat))

	items := strings.Split(string(dat),"\n")
	
    var sum int

    sum=0

    for i:=0; i<len(items);i++ {
		//fmt.Print(items[i], len(items[i]))
		checksum:=items[i][len(items[i])-7:][1:6]
		items[i]=items[i][0:len(items[i])-7]
		letters:=strings.Split(items[i],"-")
		
		id,err:=strconv.Atoi(letters[len(letters)-1])
		if err != nil {
			panic(err)
		}	
		letters=letters[:len(letters)-1]
		sort.Strings(letters)
		
		abc:=strings.Join(letters,"")

		m := make(map[string]int)

		abc2:=strings.Split(abc,"")

		for _, ch := range abc2 {

			if _, ok :=m[ch];ok {
				m[ch]=m[ch]+1
			} else {
				m[ch]=1
			}


		}

		vs := rankByWordCount(m)

		//fmt.Print("\n >>>>",m," -- ",vs,"\n")

		result:=""
		for v,_ := range vs {
			result=result +vs[v].Key
		}

		//result:="abcde"
		
		if checksum[0:5]==result[0:5] {
			sum=sum+id
		}
		//fmt.Print(checksum[0:5]," ",abc," >",result," ",id,"\n")
    }


    fmt.Print("answer is: ", sum, "\n")
}

func rankByWordCount(wordFrequencies map[string]int) PairList{
	pl := make(PairList, len(wordFrequencies))
	i := 0
	for k, v := range wordFrequencies {
	  pl[i] = Pair{k, v}
	  i++
	}
	sort.Sort(sort.Reverse(pl))
	return pl
  }
  
  type Pair struct {
	Key string
	Value int
  }
  
  type PairList []Pair
  
  func (p PairList) Len() int { return len(p) }
  func (p PairList) Less(i, j int) bool { 
	  return p[i].Value < p[j].Value || p[i].Value == p[j].Value && p[i].Key > p[j].Key
	}
  func (p PairList) Swap(i, j int){ p[i], p[j] = p[j], p[i] }