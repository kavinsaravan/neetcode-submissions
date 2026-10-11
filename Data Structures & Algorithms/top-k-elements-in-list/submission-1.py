class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        counts = Counter(nums)
        freq_vals = [(v, k) for k, v in counts.items()]
        heapq.heapify_max(freq_vals)
        return [heapq.heappop_max(freq_vals)[1] for _ in range(k)]
        


            

        






         
        



        