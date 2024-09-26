if __name__ == '__main__':
    records = []
    
    # Step 1: Read the number of students
    for _ in range(int(input())):
        name = input()  # Read the student's name
        score = float(input())  # Read the student's score
        records.append([score, name])  # Store them as [score, name] in records
    
    # Step 2: Sort the records by score
    records.sort()

    # Step 3: Get unique scores and find the second lowest
    unique_scores = sorted(set(record[0] for record in records))
    second_lowest_score = unique_scores[1]

    # Step 4: Find students with the second lowest score
    second_lowest_students = [record[1] for record in records if record[0] == second_lowest_score]

    # Step 5: Sort names alphabetically
    second_lowest_students.sort()

    # Step 6: Print each name
    for name in second_lowest_students:
        print(name)
