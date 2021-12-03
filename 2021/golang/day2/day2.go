package day2

import (
	"aoc21/utils"
	"fmt"
	"strconv"
	"strings"
)

func SolveDay2() {
	fmt.Println(part1("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d2.txt"))
	fmt.Println(part2("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d2.txt"))
}

func part1(path string) int {
	stringArray := utils.ReadStringArray(path)
	post := [2]int{0, 0}
	for _, s := range stringArray {
		x := strings.Split(s, " ")
		i, err := strconv.Atoi(x[1])
		if err == nil {
			if x[0] == "forward" {
				post[0] += i
			} else if x[0] == "up" {
				post[1] -= i
			} else {
				post[1] += i
			}
		}

	}
	return post[0] * post[1]
}

func part2(path string) int {
	stringArray := utils.ReadStringArray(path)
	post := [3]int{0, 0, 0}
	for _, s := range stringArray {
		x := strings.Split(s, " ")
		i, err := strconv.Atoi(x[1])
		if err == nil {
			if x[0] == "forward" {
				post[0] += i
				post[1] += i * post[2]
			} else if x[0] == "up" {
				post[2] -= i
			} else {
				post[2] += i
			}
		}
	}
	return post[0] * post[1]
}
