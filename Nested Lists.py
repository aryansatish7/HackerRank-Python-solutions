if __name__ == '__main__':
    scorecard = []
    no_of_students = int(input())
    for i in range(0,no_of_students):
        details = [input(),float(input())]
        scorecard.append(details)

    second_highest = sorted(list(set([marks for name,marks in scorecard])))[1]
    final_result = [name for name,marks in sorted(scorecard) if marks == second_highest]
    print("\n".join(final_result))
