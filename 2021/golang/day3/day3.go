package day3

import (
	"aoc21/utils"
	"fmt"
	"math"
	"strconv"
)

func SolveDay3() {
	fmt.Println(part1("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d3.txt"))
	fmt.Println(part2("/Users/hjjoosse/Documents/UMCU/Adventofcode/2021/data/input_d3.txt"))
}

func part1(path string) int {
	hexabins := utils.ReadStringArray(path)
	gamma := ""
	epsilon := ""
	for i := 0; i < len(hexabins[0]); i++ {
		if getmostCommon(hexabins, i) == "1" {
			epsilon += "0"
		} else {
			epsilon += "1"
		}
		gamma += getmostCommon(hexabins, i)

	}
	gamma_int := bintoint(gamma)
	epsilon_int := bintoint(epsilon)

	return gamma_int * epsilon_int
}

func part2(path string) int {
	hexabins := utils.ReadStringArray(path)
	oxygen := bintoint(gettosingle(hexabins, true))
	cotwo := bintoint(gettosingle(hexabins, false))
	return oxygen * cotwo

}

func gettosingle(input []string, same bool) string {
	input_cop := input
	i := 0
	for len(input_cop) > 1 {
		var temp_list []string
		most_common := getmostCommon(input_cop, i)
		search := getsearch(most_common, same)
		for _, s := range input_cop {
			if string(s[i]) == search {
				temp_list = append(temp_list, s)
			}
		}
		i += 1
		input_cop = temp_list
	}
	return input_cop[0]
}

func getsearch(most_common string, same bool) string {
	var search string
	if same {
		search = string(most_common)
	} else {
		if string(most_common) == "1" {
			search = "0"
		} else {
			search = "1"
		}
	}
	return search
}

func getmostCommon(array []string, index int) string {
	tot := 0
	for _, s := range array {
		if string(s[index]) == "1" {
			tot += 1
		}
	}
	if float64(tot) >= float64(len(array))/2 {
		return "1"
	} else {
		return "0"
	}

}

func bintoint(bitcode string) int {
	var intedbin int
	for i := 0; i < len(bitcode); i++ {
		bit, err := strconv.Atoi(string(bitcode[len(bitcode)-1-i]))
		if err != nil {
			fmt.Println(err)
		}
		intedbin += bit * int(math.Pow(float64(2), float64(i)))
	}
	return intedbin
}
