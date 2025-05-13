"""
modify in place
it's intuitive to understand, how do I communicate this to code
matrix is square, this is helpful actually
outer layer rotates cw
inner later rotates cw also
repeat until inner layer has 1 or 0 values
if it's in place then how do we manage overwritting values
we need to use the single line move operation?
recursivley go over the entire grid, one layer at a time
I cant move one row at a time because we need to modify in place
we need to swap one value at a time?

"""


class Solution:
    def rotate(self, matrix):
        def get_matrix_val(pos):
            return matrix[pos[0]][pos[1]]

        def set_matrix_val(pos, val):
            matrix[pos[0]][pos[1]] = val

        def swap_four(positions):
            print(positions)
            tmp = get_matrix_val(positions[0])
            for i in range(4):
                j = (i + 1) % 4
                curr = tmp
                tmp = get_matrix_val(positions[j])
                set_matrix_val(positions[j], curr)

        def swap_layer(start, end):
            # [0,0+i] [0+i, end] [end, end - i] [end - i,0]
            if end - start < 0:
                return
            i = 0
            for j in range(start, end):
                swap_four(
                    [
                        [start, start + i],
                        [start + i, end],
                        [end, end - i],
                        [end - i, start],
                    ]
                )
                i += 1
            swap_layer(start + 1, end - 1)

        swap_layer(0, len(matrix) - 1)


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
sol = Solution()
sol.rotate(matrix)
print(matrix)
