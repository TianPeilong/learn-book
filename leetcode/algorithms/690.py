# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        dic = {}
        for e in employees:
            dic[e.id] = e
        return self._getImportance(dic, id)
        
    def _getImportance(self, dic, id):
        if id not in dic:
            return 0
        cur = dic[id]
        return cur.importance + sum(map(lambda x:self._getImportance(dic, x), cur.subordinates))

employees = [
    Employee(1, 4, [2, 3]),
    Employee(2, 3, []),
    Employee(3, 3, []),
]
s = Solution()
print(s.getImportance(employees, 1))