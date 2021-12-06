package day4

import (
	"aoc21/utils"
	"fmt"
	"strings"
)

func SolveDay4() {
	fmt.Println(part1("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d4.txt"))
}

func part1(path string) []string {
	arr := utils.ReadStringArray(path)
	arr_split := strings.Split(arr[2], "\n\n")
	return arr_split
}
