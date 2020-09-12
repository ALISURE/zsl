# 首先将box按照任一维度排序，初始化辅助数组为box每个元素的高度。从头开始遍历box，对于每个box[i]，从0遍历到i-1，依次判断box[j]的三个维度是否均小于box[i]，如果是则尝试更新辅助数组第i个元素。最后返回辅助数组中最大元素即可。


class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        if len(box) == 0:
            return 0
        box.sort()
        height = [box[i][2] for i in range(len(box))]
        for i in range(1, len(box)):
            cur_box = box[i]
            for j in range(i):
                if box[j][0] < cur_box[0] and box[j][1] < cur_box[1] and box[j][2] < cur_box[2]:
                    height[i] = max(height[i], height[j] + cur_box[2])
        return max(height)
        
