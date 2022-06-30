"""https://leetcode.com/problems/course-schedule/
"""

# Approach 1 dfs
# Time Limit Exceeded
class Solution_1:
    def canFinish(self, numCourses, prerequisites):
        # 利用 dict 紀錄依賴關係
        deps_dict = {}
        for take, need in prerequisites:
            if need in deps_dict:
                deps_dict[need].append(take)
            else:
                deps_dict[need] = [take]
        
        # 輪流從每個節點開始，紀錄走過的 path，每個節點開始就清掉 path
        path = set()
        for target in range(numCourses):
            path.clear()
            if not self.dfs(target, deps_dict, path):
                return False
        return True

    def dfs(self, target, deps_dict, path):
        if target in path:
            return False
        if target not in deps_dict:
            return True
            
        # 輪流加入 dep dfs，但這樣走過的還會再走一次。
        for course in deps_dict[target]:
            path.add(course)
            if not self.dfs(course, deps_dict, path):
                return False
            path.remove(course)
        return True

# Approach 2 dfs - improved
class Solution_2:
    def canFinish(self, numCourses, prerequisites):
        checked = set()
        deps_dict = {}
        for target, need in prerequisites:
            if target in deps_dict:
                deps_dict[target].append(need)
            else:
                deps_dict[target] = [need]
                
        checking = set()
        for target in range(numCourses):
            checking.clear()
            if not self.dfs(target, deps_dict, checking, checked):
                return False
        return True

    def dfs(self, target, deps_dict, checking, checked):
        if target in checked:
            return True
        if target not in deps_dict:
            checked.add(target)
            return True
        if target in checking:
            return False
    
        checking.add(target)
        for dep_course in deps_dict[target]:
            if not self.dfs(dep_course, deps_dict, checking, checked):
                return False
        # 紀錄已經走進去的點，下次就無需再走一次了。
        checked.add(target)
        return True

# Approach 3 bfs
class Solution_3:
    def canFinish(self, numCourses, prerequisites):
        # deps == dependences, deped == depended
        deps = [ [] for _ in range(numCourses)]
        deped_count = [0 for _ in range(numCourses)]

        # 紀錄被依賴的次數 edge
        for target, need in prerequisites:
            deps[target].append(need)
            deped_count[need] += 1

        # 從沒有被依賴的節點開始
        queue = []
        for course, count in enumerate(deped_count):
            if count == 0:
                queue.append(course)
        
        while queue:
            target = queue.pop(0)
            for dep in deps[target]:
                deped_count[dep] -= 1
                if deped_count[dep] == 0:
                    queue.append(dep)

        # 有刪不掉的 edge 代表存在 cycle
        for count in deped_count:
            if count != 0:
                return False
        return True
            