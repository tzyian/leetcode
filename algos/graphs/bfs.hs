{- Taken from: https://doisinkidney.com/posts/2018-06-03-breadth-first-traversals-in-too-much-detail.html


-- foldl threads the accumulator through the list from the left
foldl g z [x1, x2, x3]
= g (g (g z x1) x2) x3

-- So substituting g with (foldr f) gives:
foldl (foldr f) b [q1, q2, q3]
= foldr f (foldr f (foldr f b q1) q2) q3

data Tree a = Node a [Tree a]
type K = [Tree a] -- i.e. a tree of children, so [K] is a forest

f :: K -> ([K] -> [a]) -> [K] -> [a]
b :: [K] -> [a]
qs :: [K]

foldr :: (x -> acc -> acc) -> acc -> [x] -> acc
  sub:
    x   = Tree a
    acc = ([K] -> [a])
  becomes:
foldr f
  :: Tree a                     -- x, the current node being processed
  -> ([K] -> [a])               -- acc, a function which takes in the future forest and returns the values
  -> ([K] -> [a])               -- result, a function which takes in the future forest and returns the values including this node's values


foldl :: (x -> acc -> acc) -> acc -> [x] -> acc
  sub: 
    acc = [K] -> [a]
    x   = K
  becomes:
foldl (foldr f)
  :: ([K] -> [a])       -- b, takes the forest from the current level and eventually returns the values
  -> [K]                -- qs, the existing forest which needs to be traversed
  -> ([K] -> [a])       -- a function which takes in [], an empty queue to be populated with this level's children(s)



fw is a function transformer
bw forms the queue for the next level

fw (xs : bw) is the recursive call the children to the queue
(xs : bw) prepends to front; use foldr to be queue
pass b to fw, and b

foldl because we process level by level
foldr because we process each node's children left to right


-- Example expansion:
t =
  Node 1
    [ Node 2 []
    , Node 3 [Node 4 []]
    ]

breadthFirstEnumerate t
= f (Node 1 [n2, n3]) b []
= 1 : b ([[n2, n3]])              -- [n2, n3] : []
= 1 : foldl (foldr f) b [[n2, n3]] []
= 1 : (foldr f b [n2, n3]) []
= 1 : f n2 (f n3 b) []            
= 1 : 2 : (f n3 b) ([] : [])      -- f n2 _ [] because n2 has no children
= 1 : 2 : 3 : b ([n4] : [[]])
= 1 : 2 : 3 : b [[n4], []]
= 1 : 2 : 3 : foldl (foldr f) b [[n4], []] []   -- foldl has 2 elements, which are tree n4 and children of n2
= 1 : 2 : 3 : (foldr f (foldr f b []) [n4]) []  -- the inner foldr becomes b [] = []
= 1 : 2 : 3 : (f n4 (foldr f b [])) []
= 1 : 2 : 3 : 4 : (foldr f b []) ([] : [])
= 1 : 2 : 3 : 4 : b [[]]
= 1 : 2 : 3 : 4 : foldl (foldr f) b [[]] []
= 1 : 2 : 3 : 4 : (foldr f b []) []
= 1 : 2 : 3 : 4 : b []
= 1 : 2 : 3 : 4 : []
= [1, 2, 3, 4]


 - }


breadthFirstEnumerate :: Tree a -> [a]
breadthFirstEnumerate ts = f ts b []
  where
    f (Node x xs) fw bw = x : fw (xs : bw)

    b [] = []
    b qs = foldl (foldr f) b qs []
