package array_strings_test

import (
	"proCode/Go/array_strings"
	"sync"
	"testing"
)

func TestGcdOfStrings(t *testing.T) {
	tests := []struct {
		str1     string
		str2     string
		expected string
	}{
		{"ABCABC", "ABC", "ABC"},
		{"ABABAB", "ABAB", "AB"},
		{"LEET", "CODE", ""},
		{"A", "A", "A"},
		{"AAAA", "AA", "AA"},
		{"ABCDEF", "ABC", ""},
		{"ABAB", "ABABAB", "AB"},
	}

	var wg sync.WaitGroup

	// Iteramos sobre todos los casos de prueba
	for _, tt := range tests {
		wg.Add(1) // Incrementamos el contador del WaitGroup
		go func(tt struct {
			str1     string
			str2     string
			expected string
		}) {
			defer wg.Done() // Decrementamos el contador cuando la goroutine termine

			// Ejecutamos la prueba
			result := array_strings.GcdOfStrings(tt.str1, tt.str2)

			// Verificamos si el resultado es correcto
			if result != tt.expected {
				t.Errorf("GcdOfStrings(%q, %q) = %q; want %q", tt.str1, tt.str2, result, tt.expected)
			}
		}(tt) // Pasamos la estructura de prueba como argumento a la goroutine
	}

	wg.Wait() // Esperamos a que todas las goroutines terminen
}
