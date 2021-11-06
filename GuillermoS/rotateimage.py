class Solution(object):
    def rotateimage(self, matrix):

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                temp = matrix[i][j]
                matrix [i][j] = matrix[j][i]
                matrix [j][i] = temp
            #matrix[i] = matrix[i][::-1]
            matrix[i].reverse()
        
        print(matrix)



image = []
image.append(['1','2','3'])
image.append(['4','5','6'])
image.append(['7','8','9'])

s = Solution()
s.rotateimage(image)

