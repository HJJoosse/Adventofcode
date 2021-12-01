package utils


func sum(data []int) int {
	s := 0
	for _, v := range data {
		s += v
	}
	return s
}
