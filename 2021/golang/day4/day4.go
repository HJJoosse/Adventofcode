package day4

import (
	"aoc21/utils"
	"fmt"
	"strconv"
)

func SolveDay4() {
	fmt.Println(part1("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d4_test.txt"))
}

func part1(path string) ([]string, [][][]int) {
	bingonumbers, bingocards := utils.ReadBingoCards(path)
	possibilities := makepossibilities(bingocards)
	drawnnumbers := []int{}
	for {
		number, err := strconv.Atoi(bingonumbers[0])
		if err != nil {
			fmt.Println(err)
		}
		drawnnumbers = append(drawnnumbers, number)
		bingonumbers = bingonumbers[1:]
		for _, card := range bingocards {

			println(card)

		}
	}
	return bingonumbers, bingocards
}

func makepossibilities(bingocards [][][]int) [][][]int {

}
