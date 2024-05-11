// https://leetcode.com/problems/destination-city

func destCity(paths [][]string) string {
    sources := make(map[string]struct{})
    dests := make(map[string]struct{})
    for _, path := range paths {
        src, dst := path[0], path[1]
        sources[src] = struct{}{}
        dests[dst] = struct{}{}
    }
    for dst := range dests {
        if _, ok := sources[dst]; !ok {
            return dst
        }
    }
    return ""
}