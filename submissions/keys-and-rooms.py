// https://leetcode.com/problems/keys-and-rooms

class Solution:
    def canVisitAllRooms(self, rooms):
        length = len(rooms)
        visited = [0] * length      #0 means not visited, 1 means visited
        keys = [0] * length         #0 means no key, 1 means have key


        
        
        def extractKeys(self, roomIndex):
            if visited[roomIndex] == 0:         #if room not visited before
                visited[roomIndex] = 1
                for i in rooms[roomIndex]:      #extract keys inside
                    if keys[i] == 0:            #if keys not found yet 
                        keys[i] = 1            #set key to found
                        extractKeys(self, i)    #recurse
        
        extractKeys(self, 0)
        return 0 not in visited


x = [[1],[2],[3],[]]
y = Solution()
z = y.canVisitAllRooms(x)
print(z)
