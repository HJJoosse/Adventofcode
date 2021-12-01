package main

import (
	"fmt"
)

func main() {

	fmt.Println(part1())
	fmt.Println(part2())
}

func part1() int {
	contArray := utils.readArray("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d1.txt")
	s := 0
	for i := 0; i < len(contArray)-1; i++ {
		if contArray[i] < contArray[i+1] {
			s += 1
		}
	}
	return s
}

func part2() int {
	contArray := utils.readArray("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d1.txt")
	s := 0
	for i := 0; i < len(contArray)-3; i++ {
		if sum(contArray[i:i+3]) < sum(contArray[i+1:i+4]) {
			s += 1
		}
	}
	return s
}

func sum(data []int) int {
	s := 0
	for _, v := range data {
		s += v
	}
	return s
}
