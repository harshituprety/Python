#Set is unordered and Dictionary is ordered.

student1 = {
  1:747,
  2:838,
  3:171,
  4:387
}
student2 = {
  5:637,
  6:839
}

student1.update(student2)
# student1.clear()
student1.pop(2)
student1.popitem()
del student2['6']
print(student2)
