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

func TestLenOfList(t *testing.T) {
	tests := []struct {
		name string
		list []int
		len  int
	}{
		{"Test1", []int{1, 2, 3, 4}, 4},
		{"Test2", []int{1}, 1},
		{"Test3", []int{1, 2}, 2},
		{"Test4", []int{}, 0},
	}

	for _, test := range tests {
		var resultLen int = LenOfList(test.list)

		if resultLen != test.len {
			t.Errorf("%s failed: wrong answer, want: %d, result is: %d", test.name, test.len, resultLen)
		}
	}
}

func TestLenOfLinkList(t *testing.T) {
	tests := []struct {
		name string
		list LinkedList
		len  int
	}{
		{"Test1", GetLinkedList([]int{1, 2, 3, 4}), 4},
		{"Test2", GetLinkedList([]int{1}), 1},
		{"Test3", GetLinkedList([]int{1, 2}), 2},
		{"Test4", GetLinkedList([]int{}), 0},
	}

	for _, test := range tests {
		var resultLen int = LenOfLinkList(test.list)

		if resultLen != test.len {
			t.Errorf("%s failed: wrong answer, want: %d, result is: %d", test.name, test.len, resultLen)
		}
	}
}

func TestIsPallindrom(t *testing.T) {
	tests := []struct {
		name         string
		word         string
		isPallindorm bool
	}{
		{"Test1", "aba", true},
		{"Test2", "abba", true},
		{"Test3", "a", true},
		{"Test4", "", true},
		{"Test5", "aa", true},
		{"Test6", "ab", false},
	}

	for _, test := range tests {
		var isPallindorm bool = IsPallindrom(test.word)

		if isPallindorm != test.isPallindorm {
			t.Errorf("%s failed: wrong answer, want: %v, result is: %v", test.name, test.isPallindorm, isPallindorm)
		}
	}
}

func TestPrintEvenNumbers(t *testing.T) {
	PrintEvenNumbers([]int{})
}
func TestPrintNumbersWithEvenIndexes(t *testing.T) {
	PrintNumbersWithEvenIndexes([]int{})
}

func TestFindSecondMax(t *testing.T) {
	tests := []struct {
		name      string
		numbers   []int
		secondMax int
	}{
		{"Test1", []int{1, 2, 3, 4}, 3},
		{"Test2", []int{1}, 1},
		{"Test3", []int{1, 1, 1, 1}, 1},
		{"Test4", []int{1, 2, 3, 4, 4}, 4},
		{"Test5", []int{}, -1},
		{"Test6", []int{-1, -2, -1, -3}, -1},
	}

	for _, test := range tests {
		var secondMax int = FindSecondMax(test.numbers)

		if secondMax != test.secondMax {
			t.Errorf("%s failed: wrong answer, want: %v, result is: %v", test.name, test.secondMax, secondMax)
		}
	}
}
func TestFindFiles(t *testing.T) {
	tests := []struct {
		name        string
		files       []interface{}
		fileName    string
		amountFiles int
	}{
		{"Test1", []interface{}{
			"file.txt", []interface{}{
				"file.txt",
				"file.txt",
				"file.txt",
				[]interface{}{
					"file.txt",
					"file.txt",
					"file.txt",
				},
				"file.txt",
				"file.txt",
				"file.txt",
			},
		}, "file.txt", 10},
	}

	for _, test := range tests {
		var arrayOfFiles []string = FindFiles(test.files, test.fileName)

		if len(arrayOfFiles) != test.amountFiles {
			t.Errorf("%s failed: wrong answer, want: %v, result is: %v", test.name, test.amountFiles, len(arrayOfFiles))
		}
	}
}
