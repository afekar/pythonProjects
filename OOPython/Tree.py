class DecisionTree:

    @classmethod
    def predict(cls, root, x):
        current = root
        while current.indx != -1:
            if x[current.indx]:
                current = current.left
            else:
                current = current.right
            if not hasattr(current, 'indx'):
                break
        return current.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node is None:
            return obj
        if left:
            node.left = obj
        else:
            node.right = obj
        return obj


class TreeObj:

    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right


tr = TreeObj(0)
root = DecisionTree.add_obj(tr)
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом
print(res)