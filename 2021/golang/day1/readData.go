package utils

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func readArray(path string) []int {
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
