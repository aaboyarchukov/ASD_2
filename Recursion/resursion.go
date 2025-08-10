package main

// 1. возведение числа N в степень M
// mem = O(1), t = O(m)
func Pow(n, m int) int {
	if m == 0 {
		return 1
	}

	if m == 1 {
		return n
	}

	return n * Pow(n, m-1)
}

// 2. вычисление суммы цифр числа
// mem = O(1), t = O(len(number)), len(number) - amount of digits
func SumOfNumberDigits(number int) int {
	if number < 10 {
		return number
	}

	return int(number%10) + SumOfNumberDigits(int(number/10))
}
