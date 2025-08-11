package main

import (
	"errors"
	"fmt"
)

// 1. возведение числа N в степень M
// mem = O(m), t = O(m)
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
// mem = O(len(number)), t = O(len(number)), len(number) - amount of digits
func SumOfNumberDigits(number int) int {
	if number < 10 {
		return number
	}

	return int(number%10) + SumOfNumberDigits(int(number/10))
}

type Node struct {
	next  *Node
	value int
}

type LinkedList struct {
	head *Node
	tail *Node
}

func (l *LinkedList) AddInTail(item Node) {
	if l.head == nil {
		l.head = &item
	} else {
		l.tail.next = &item
	}
	l.tail = &item
}

func (l *LinkedList) Count() int {
	var count int
	tempNode := l.head
	for tempNode != nil {
		count++
		tempNode = tempNode.next
	}
	return count
}

func (l *LinkedList) Find(n int) (Node, error) {
	tempNode := l.head
	for tempNode != nil {
		if tempNode.value == n {
			return *tempNode, nil
		}
		tempNode = tempNode.next
	}
	return Node{value: -1, next: nil}, errors.New("node is not finding")
}

func (l *LinkedList) FindAll(n int) []Node {
	var nodes []Node
	tempNode := l.head
	for tempNode != nil {
		if tempNode.value == n {
			nodes = append(nodes, *tempNode)
		}
		tempNode = tempNode.next
	}
	return nodes
}

func (l *LinkedList) Delete(n int, all bool) {
	if l.head == nil {
		return
	}

	tempNode := l.head
	var prev *Node

	if l.Count() == 1 && tempNode.value == n {
		l.Clean()
		return
	}

	for tempNode != nil {
		deleted := false
		if tempNode.value == n && tempNode == l.head {
			l.head = tempNode.next
			deleted = true
		} else if tempNode.value == n && tempNode == l.tail {
			prev.next = nil
			l.tail = prev
			deleted = true
		} else if tempNode.value == n {
			prev.next = tempNode.next
			deleted = true
		}
		if !all && deleted {
			return
		}
		if !deleted {
			prev = tempNode
		}
		tempNode = tempNode.next
	}
}

func (l *LinkedList) Insert(after *Node, add Node) {
	if l.head == nil {
		l.InsertFirst(add)
		return
	}
	tempNode := l.head
	// if node will not exists, then we have to finding it first
	for tempNode.value != after.value {
		tempNode = tempNode.next
	}
	if tempNode == l.tail {
		l.AddInTail(add)
	} else {
		nextNode := tempNode.next
		tempNode.next = &add
		add.next = nextNode
	}

}

func (l *LinkedList) InsertFirst(first Node) {
	if l.head == nil {
		l.tail = &first
	} else {
		first.next = l.head
	}
	l.head = &first

}

func (l *LinkedList) Clean() {
	l.head = nil
	l.tail = nil
}

func (l *LinkedList) Pop() {
	l.head = l.head.next
}

func GetLinkedList(values []int) LinkedList {
	var resultLL LinkedList // resulting linked list
	for _, value := range values {
		resultLL.AddInTail(Node{
			value: value,
		})
	}
	return resultLL
}

// 3. расчёт длины списка,
// для которого разрешена только операция удаления первого элемента pop(0)
// (и получение длины конечно)
// mem = O(len(list)), t = O(len(list)), len(list) - size of list

// можно сделать с помощью связного списка, тогда получится без функции len()
func LenOfLinkList(linkedList LinkedList) int {
	if linkedList.head == nil {
		return 0
	}

	linkedList.Pop()

	return 1 + LenOfLinkList(linkedList)

}

func LenOfList(list []int) int {
	if len(list) == 0 {
		return 0
	}

	return 1 + LenOfList(list[1:])
}

// 4. проверка, является ли строка палиндромом
// mem = O(len(word) / 2) ~ O(len(word)), t = O(len(word) / 2) ~ O(len(word)),
// len(word) - size of word
func IsPallindrom(word string) bool {
	return ProcessingWord(word, 0, len(word)-1)
}

func ProcessingWord(word string, begin, end int) bool {
	if begin >= end {
		return true
	}
	if word[begin] != word[end] {
		return false
	}

	return ProcessingWord(word, begin+1, end-1)
}

// 5. печать только чётных значений из списка
// mem = O(len(nums)), t = O(len(nums)),
// len(nums) - size of nums
func PrintEvenNumbers(nums []int) {
	if len(nums) == 0 {
		return
	}

	if nums[0]%2 == 0 {
		fmt.Println(nums[0])
	}

	PrintEvenNumbers(nums[1:])
}

// 6. печать элементов списка с чётными индексами
// mem = O(len(nums)), t = O(len(nums)),
// len(nums) - size of nums
func PrintNumbersWithEvenIndexes(nums []int) {
	ProcessingEvenIndex(nums, 0)
}

func ProcessingEvenIndex(nums []int, index int) {
	if index > len(nums)-1 {
		return
	}

	if index%2 == 0 {
		fmt.Println(nums[index])
	}

	ProcessingEvenIndex(nums, index+1)
}

// 7. нахождение второго максимального числа в списке
// (с учётом, что максимальных может быть несколько, если они равны).

// 8. поиск всех файлов в заданном каталоге, включая файлы,
// расположенные в подкаталогах произвольной вложенности.
// Для хождения по директориям используйте стандартную функцию.
// Результат выдавайте списком, List например.
