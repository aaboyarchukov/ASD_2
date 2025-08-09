package main

import "testing"

func TestPow(t *testing.T) {
	tests := []struct {
		name string
		n    int
		m    int
		want int
	}{
		{"Test1", 1, 2, 1},
		{"Test2", 1, 0, 1},
		{"Test3", -1, 3, -1},
		{"Test4", -1, 4, 1},
		{"Test5", 0, 0, 1},
		{"Test6", 0, 1, 0},
		{"Test7", 2, 5, 32},
	}

	for _, test := range tests {
		var resultNumber int = Pow(test.n, test.m)

		if resultNumber != test.want {
			t.Errorf("%s failed: wrong answer, want: %d, result is: %d", test.name, test.want, resultNumber)
		}
	}
}

func TestSumOfNumberDigits(t *testing.T) {
	tests := []struct {
		name   string
		number int
		want   int
	}{
		{"Test1", 1, 1},
		{"Test2", 10, 1},
		{"Test3", 0, 0},
		{"Test4", 123, 6},
	}

	for _, test := range tests {
		var resultNumber int = SumOfNumberDigits(test.number)

		if resultNumber != test.want {
			t.Errorf("%s failed: wrong answer, want: %d, result is: %d", test.name, test.want, resultNumber)
		}
	}
}
