# Creating sets
empty_set = set()
s_literal = {1, 2, 3}
s_from_list = set([3, 4, 5])
s_range = set(range(10))

print("empty_set:", empty_set)
print("s_literal:", s_literal)
print("s_from_list:", s_from_list)
print("s_range:", s_range)
print()

# Set methods
m = {1, 2, 3}
m.add(4)
m.update([5, 6])
print("after add/update:", m)
print("-----------------------")

print(m)
print(m.remove(6))
print("after remove 6:", m)

popped = m.pop()
print("after remove/discard/pop:", m, "popped:", popped)

m_copy = m.copy()
m.clear()
print("m cleared:", m, "m_copy:", m_copy)

