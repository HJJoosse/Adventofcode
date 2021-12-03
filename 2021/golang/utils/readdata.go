package utils

import (
	"bufio"
	"log"
	"os"
	"strconv"
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
