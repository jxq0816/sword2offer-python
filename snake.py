# -*- coding:utf-8 -*-
class Solution:
    def fun(self,n):
        a=[[0]*n for i in range(n)]
        t=0
        half=int(n/2)
        for k in range(0,half):
            i=k
            for j in range(k,n-k-1):
                t=t+1
                a[i][j]=t

            j=n-k-1
            for i in range(k,n-k-1):
                t=t+1
                a[i][j]=t

            i=n-k-1
            for j in range(n-k-1,k,-1):
                t = t + 1
                a[i][j] = t

            j=k
            for i in range(n-k-1,k,-1):
                t = t + 1
                a[i][j] = t

        if n%2 ==1:
            a[half][half]=t+1

        for i in range(n):
            for j in range(n):
                print(a[i][j], end='\t')
            print('\n')

if __name__ =='__main__':
    answer=Solution()
    answer.fun(4)