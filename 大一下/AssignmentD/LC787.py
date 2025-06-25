class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        connect = defaultdict(dict)
        for a, b, c in flights:
            connect[a][b] = c

        @lru_cache(None)
        def dfs(city, remain):
            if city == dst:
                return 0
            if not remain:
                return inf
            remain -= 1
            ans = inf
            for nxt in connect[city]:
                ans = min(ans, dfs(nxt, remain) + connect[city][nxt])
            return ans
        
        res = dfs(src, k + 1)
        return res if res != inf else -1