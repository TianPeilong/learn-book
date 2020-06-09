package main

import (
	"fmt"
	"unicode/utf8"
)

func test1() {
	for i := 0; i < 5; i++ {
		defer fmt.Println(i)
	}
}

func test2() {
	s := "hello, 世界"
	fmt.Println(len(s))
	fmt.Println(utf8.RuneCountInString(s))
	for i := 0; i < len(s); {
		r, size := utf8.DecodeRuneInString(s[i:])
		fmt.Printf("%d\t%c\n", i, r)
		i += size
	}
}

func main() {
	test1()
}
