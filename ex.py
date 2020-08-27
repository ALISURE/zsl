# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# def deleteDuplicates(head: ListNode) -> ListNode:
#     head1 = ListNode(0)
#     head1.next = head
#     last = head
#     pre = head1
#     while last:
#         if last.next and last.val == last.next.val:
#             while last.next and last.val == last.next.val:
#                 last = last.next
#             pre.next = last.next
#             last = last.next
#         else:
#             pre = pre.next
#             last = last.next
#     return head1.next
#
# node = ListNode(1)
# node.next = ListNode(1)
# node.next.next = ListNode(2)
# root = deleteDuplicates(node)
# while root:
#     print(root.val)
#     root = root.next
# n, m, k = [int(i) for i in input().split()]
# nums = [int(i) for i in input().split()]
# res = []
# for i in range(m):
#     item = [int(j) for j in input().split()]
#     new_nums = nums[item[0] - 1:item[1]]
#     new_nums.sort()
#     left = 0
#     right = len(new_nums) - 1
#     count = 0
#     while left < right:
#         sum_ = new_nums[left] * new_nums[right] + new_nums[left] + new_nums[right]
#         if sum_ == k:
#             count += 1
#             left += 1
#             right -= 1
#         elif sum_ < k:
#             left += 1
#         else:
#             right -= 1
#     res.append(count)
#
# for i in res:
#     print(i)

def test(s, ends):
    s = sorted(s)
    ends = sorted(ends)
    s, e =0, 0
    min_rooms, cnt_rooms = 0, 0
    while s<len(s):
        if s[s]<=ends[e]:
            cnt_rooms+=1
            min_rooms = max(min_rooms, cnt_rooms)
            s+=1
        else:
            cnt_rooms -=1
            e+=1
    return min_rooms
t = int(input())
for j in range(t):
    num = int(input())
    arr = []
    start = []
    end = []
    for i in range(num):
        s, e = list(map(int, input().split()))
        start.append(s)
        end.append(e)
    print(test(start, end))