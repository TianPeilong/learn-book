package main

import (
	"fmt"
	"math"
)

func Sqrt(x, d float64) float64 {
	z := 1.0
	for math.Abs(x-z*z) > d {
		fmt.Println(z)
		z -= (z*z - x) / (2 * z)
	}
	return z
}

func main() {
	x := 6573923.0
	fmt.Println(Sqrt(x, 0.00000000001))
	fmt.Println(math.Sqrt(x))
}
