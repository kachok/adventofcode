package main

import "fmt"

func next(sa, sb int) (na, nb int) {
	var fa, fb = 16807, 48271
	var v = 2147483647

	na = (sa * fa) % v
	nb = (sb * fb) % v

	return
}

func main() {
	var a int = 516
	var b int = 190

	//a = 65
	//b = 8921

	count := 0
	for i := 0; i < 40000000; i++ {
		a, b = next(a, b)

		if (a % 65536) == (b % 65536) {
			count = count + 1
		}
	}

	fmt.Println("answer is: %d\n", count)

}
