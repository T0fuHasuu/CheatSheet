class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        index, step = 0, 1
        
        for char in s:
            rows[index] += char
            
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
            print(rows)
            
        return "".join(rows)
    


"""Running Case"""
    
case = [("PAYPALISHIRING", 3),("PAYPALISHIRING", 4), ("A", 1)]
anss = ["PAHNAPLSIIGYIR", "PINALSIGYAHRPI", "A"]

for i,j in zip(case, anss):
    print(f"Case {i[0]} {i[1]} rows : {Solution().convert(*i)==j}")