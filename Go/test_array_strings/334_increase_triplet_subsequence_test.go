// I KNOW THAT IT IS NOT NECESARY TO USE GOROUTINES IN THIS CASE, BUT I JUST WANTED TO PRACTICE WITH THEM
package array_strings_test

import (
	"proCode/Go/array_strings"
	"sync"
	"testing"
)

func TestIncreasingTriplet(t *testing.T) {
	tests := []struct {
		nums     []int
		expected bool
	}{
		{[]int{1, 2, 3, 4, 5}, true},
		{[]int{5, 4, 3, 2, 1}, false},
		{[]int{2, 1, 5, 0, 4, 6}, true},
		{[]int{10, 9, 8, 1, 2}, false},
		{[]int{10, 1, 5, 3, 4, 6}, true},
		{[]int{-3, -2, -1, 0, 1}, true},
		{[]int{2, 2, 3, 1, 4}, true},
		{[]int{1, 2}, false},
		{listOfIntegers(100), true},
		{[]int{10, 9, 2, 3, 5}, true},
		{[]int{1000000, 2000000, 3000000}, true},
		{[]int{int(^uint(0) >> 1), int(^uint(0) >> 1), int(^uint(0) >> 1)}, false},
	}

	var wg sync.WaitGroup

	for _, tt := range tests {
		// Incrementa el contador del WaitGroup por cada caso de prueba
		wg.Add(1)

		// Ejecuta cada caso de prueba en una gorutina
		go func(tt struct {
			nums     []int
			expected bool
		}) {
			defer wg.Done() // Decrementa el contador al finalizar la gorutina
			result := array_strings.IncreasingTriplet(tt.nums)
			if result != tt.expected {
				t.Errorf("IncreasingTriplet(%v) = %v; want %v", tt.nums, result, tt.expected)
			}
		}(tt)
	}

	// Espera a que todas las gorutinas finalicen
	wg.Wait()
}

// listOfIntegers genera una lista creciente de enteros desde 0 hasta n-1
func listOfIntegers(n int) []int {
	nums := make([]int, n)
	for i := 0; i < n; i++ {
		nums[i] = i
	}
	return nums
}
