// https://leetcode.com/problems/asteroid-collision


func asteroidCollision(asteroids []int) []int {
	stack := make(Stack[int], 0)
	for _, rock := range asteroids {
		for {
			if stack.Len() == 0 {
				stack.Push(rock)
				break
			}
			old := stack.Peek()
			if (old < 0 && rock < 0) || (old > 0 && rock > 0) || (old < 0 && rock > 0) {
				stack.Push(rock)
				break
			} else if old < abs(rock) {
				// old explode
				stack.Pop()
				//stack.Push(rock) // this will cause problems. should only push at end
			} else if old > abs(rock) {
				// new explode
				break
			} else if old == abs(rock) {
				stack.Pop()
				break
			}
		}
	}
	return stack
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

type Stack[T any] []T

func (s *Stack[T]) Len() int {
	return len(*s)
}

func (s *Stack[T]) IsEmpty() bool {
	return s.Len() == 0
}

func (s *Stack[T]) Push(x T) {
	*s = append(*s, x)
}

func (s *Stack[T]) Peek() T {
	if s.IsEmpty() {
		log.Fatal("Stack is empty")
	}
	t := (*s)[s.Len()-1]
	return t
}

func (s *Stack[T]) Pop() T {
	if s.IsEmpty() {
		log.Fatal("Stack is empty")
	}
	t := (*s)[s.Len()-1]
	*s = (*s)[:s.Len()-1]
	return t
}
