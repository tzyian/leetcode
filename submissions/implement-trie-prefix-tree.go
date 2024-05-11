// https://leetcode.com/problems/implement-trie-prefix-tree

type Trie struct {
    children [26]*Trie
    isEnd bool
}


/** Initialize your data structure here. */
func Constructor() Trie {
    return Trie{}
}


/** Inserts a word into the trie. */
func (this *Trie) Insert(word string)  {
    curr := this
    for _, ch := range word {
        idx := ch - 'a'
        if curr.children[idx] == nil {
            curr.children[idx] = &Trie{}
        }
        curr = curr.children[idx]
    }
    curr.isEnd = true
}


/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
    curr := this
    for _, ch := range word {
        idx := ch - 'a'
        if curr.children[idx] == nil {
            return false
        }
        curr = curr.children[idx]
    }
    return curr.isEnd
}


/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
    curr := this
    for _, ch := range prefix {
        idx := ch - 'a'
        if curr.children[idx] == nil {
            return false
        }
        curr = curr.children[idx]
    }
    return true
}





// type Trie struct {
//     val  map[rune]*Trie
//     flag bool
// }

// func Constructor() Trie {
//     return Trie{
//         val:  make(map[rune]*Trie),
//         flag: false,
//     }
// }

// func (this *Trie) Insert(word string) {
//     currTrie := this
//     for i, v := range word {
//         if currTrie.val == nil {
//             currTrie.val = make(map[rune]*Trie)
//         }
//         _, ok := currTrie.val[v]
//         if !ok {
//             currTrie.val[v] = &Trie{}
//         }
//         if i == len(word)-1 {
//             currTrie.flag = true
//             return
//         }
//         currTrie = currTrie.val[v]
//     }
//     currTrie.flag = true
// }

// func (this *Trie) Search(word string) bool {
//     currTrie := this
//     for i, v := range word {
//         if i == len(word)-1 {
//             _, ok := currTrie.val[v]
//             if !ok {
//                 return false
//             }
//             return currTrie.flag
//         }
//         _, ok := currTrie.val[v]
//         if !ok {
//             return false
//         }
//         currTrie = currTrie.val[v]
//     }
//     return currTrie.flag
// }

// func (this *Trie) StartsWith(prefix string) bool {
//     currTrie := this
//     for i, v := range prefix { // Fix variable name here from "word" to "prefix"
//         if i == len(prefix)-1 {
//             _, ok := currTrie.val[v]
//             if !ok {
//                 return false
//             }
//             return true
//         }
//         _, ok := currTrie.val[v]
//         if !ok {
//             return false
//         }
//         currTrie = currTrie.val[v]
//     }
//     return true
// }

// // Example usage:
// // obj := Constructor()
// // obj.Insert(word)
// // param_2 := obj.Search(word)
// // param_3 := obj.StartsWith(prefix)
