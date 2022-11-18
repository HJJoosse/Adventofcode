package utils

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

func ReadArray(path string) []int {

	f, err := os.Open(path)

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()
	scanner := bufio.NewScanner(f)

	var contArray []int

	for scanner.Scan() {
		i, _ := strconv.Atoi(scanner.Text())
		contArray = append(contArray, i)
	}
	return contArray
}

func ReadStringArray(path string) []string {
	f, err := os.Open(path)

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()
	var stringArray []string
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		stringArray = append(stringArray, scanner.Text())
	}
	return stringArray
}

func ReadBingoCards(path string) ([]string, [][][]int) {
	f, err := os.Open(path)

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()
	scanner := bufio.NewScanner(f)
	scanner.Scan()
	bingonumbers := strings.Split(scanner.Text(), ",")
	templist := [][]int{}
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), " ")
		line_int := []int{}
		for _, i := range line {
			int_i, err := strconv.Atoi(i)
			if err == nil {
				line_int = append(line_int, int_i)
			}
		}
		if Sum(line_int) > 0 {
			templist = append(templist, line_int)
		}
	}
	bingocards := [][][]int{}
	for i := 0; i < len(templist); i += 5 {
		bingocards = append(bingocards, templist[i:i+5])
	}
	return bingonumbers, bingocards
}
