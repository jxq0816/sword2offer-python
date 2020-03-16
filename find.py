# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array)
        cols = len(array[0])
        for i in range(rows):
            for j in range(cols):
                if target == array[i][j]:
                    return True
        return False

if __name__ =='__main__':
    target = 15
    array = [[1,2,3],[4,5,6],[7,8,9],[10,12,13]]
    answer = Solution()
    print(answer.Find(target,array))