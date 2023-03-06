if __name__ == '__main__':
    sum=0
    student_marks = {
        "alpha":[10,67,89],
        "beeta":[10,57,99]
    }

    query_name = "alpha"
    if query_name  in student_marks:
        a=student_marks[query_name]
    for item in a:
        sum=sum+item
    avg=sum/3
    avg=round(avg,2)
    print(avg)