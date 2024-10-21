def avg(marks):
    # assert len(marks)!=0
    assert len(marks)!=0,"Length is zero"
    return sum(marks)/len(marks)

marks1 = []
print("Average of marks1: ",avg(marks1))