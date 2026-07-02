class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 0
        j = 0
        max_len = len(temperatures)
        out = []
        
        while i < max_len:
            j = i + 1
            while j < max_len and temperatures[j] <= temperatures[i]:
                j += 1

            if j < max_len and temperatures[j] > temperatures[i]:
                out.append(j-i)
            else:
                out.append(0)
            
            i += 1

        return out

        