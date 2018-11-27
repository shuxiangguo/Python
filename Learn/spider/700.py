# encoding: utf-8
"""
@author: shuxiangguo
@file: 700.py
@time: 2018-11-27 20:57:09
"""


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

	def printInfo(self):
		# 先序遍历
		if self is not None:
			print(self.val)
		if self.left is not None:
			self.left.printInfo()
		if self.right is not None:
			self.right.printInfo()


class Solution:
	def searchBST(self, root, val):
		"""
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
		if not root:
			return None
		if root.val == val:
			return root
		elif root.val < val:
			return self.searchBST(root.right, val)
		else:
			return self.searchBST(root.left, val)


def main():
	t1 = TreeNode(4)
	t1.left = TreeNode(2)
	t1.right = TreeNode(7)
	t1.left.left = TreeNode(1)
	t1.left.right = TreeNode(3)

	s = Solution()
	# res = s.searchBST(t1, 2)
	res = s.searchBST(t1, 7)
	res.printInfo()


if __name__ == '__main__':
	main()
