package array_strings

func IncreasingTriplet(nums []int) bool {
	min1, min2 := int(^uint(0)>>1), int(^uint(0)>>1) // Inicializar a infinito (max int)
	for _, n := range nums {
		if n <= min1 {
			min1 = n
		} else if n <= min2 {
			min2 = n
		} else {
			return true
		}
	}
	return false
}
