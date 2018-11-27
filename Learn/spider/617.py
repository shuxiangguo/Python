# encoding: utf-8
"""
@author: shuxiangguo
@file: 617.py
@time: 2018-11-27 19:06:03
"""

class TreeNode():
	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None

	def printInfo(self):
		# 先序遍历
		if self is not None:
			print(self.val)
		if self.left is not None:
			self.left.printInfo()
		if self.right is not None:
			self.right.printInfo()


class Solution(object):
	def mergeTrees(self, t1, t2):
		"""
		:type t1: TreeNode
		:type t2: TreeNode
		:rtype: TreeNode
		"""
		if not t1:
			return t2
		if not t2:
			return t1

		t1.val += t2.val
		t1.left = self.mergeTrees(t1.left, t2.left)
		t1.right = self.mergeTrees(t1.right, t2.right)
		return t1


def main():
	t1 = TreeNode(1)
	t1.left = TreeNode(3)
	t1.right = TreeNode(2)
	t1.left.left = TreeNode(5)

	t2 = TreeNode(2)
	t2.left = TreeNode(1)
	t2.right = TreeNode(3)
	t2.left.right = TreeNode(4)
	t2.right.right = TreeNode(7)

	s = Solution()
	res = s.mergeTrees(t1, t2)
	res.printInfo()




if __name__ == '__main__':
    main()