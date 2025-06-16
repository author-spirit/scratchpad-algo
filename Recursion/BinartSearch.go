package main

import "fmt"

func search(arr [8]int, low int, high int, target int) int {
	// base case
	if low > high {
		return -1
	}

	mid := int((low + high) / 2)
	if arr[mid] == target {
		return mid
	}

	if arr[mid] > target {
		high = mid - 1
	} else {
		low = mid + 1
	}

	return search(arr, low, high, target)
}

func main() {
	arr := [8]int{-1, 0, 3, 5, 9, 12}
	res := search(arr, 0, len(arr)-1, 9)
	fmt.Print(res)
}
