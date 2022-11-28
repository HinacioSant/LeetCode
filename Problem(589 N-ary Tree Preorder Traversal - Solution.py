# Problem 589:

#  Given the root of an n-ary tree, return the preorder traversal of its nodes'
# values.  Nary-Tree input serialization is represented in their level order
# traversal. Each group of children is separated by the null value (See
# examples)

# Solution:
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        global answer
        answer = []
        if root is None:
            return []
        answer.append(root.val)
        self.recur(root)
        return answer
    def recur(self,root):
        for a in root.children:
            answer.append(a.val)
            for i in a.children:
                answer.append(i.val)
                if len(i.children) > 0:
                    self.recur(i)
