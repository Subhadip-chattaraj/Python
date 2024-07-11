def find_runner_up_score(scores):
    # Remove duplicates and sort the scores in descending order
    unique_scores = sorted(set(scores), reverse=True)
    print(unique_scores)
    # Check if there is a runner-up
    if len(unique_scores) > 1:
        runner_up_score = unique_scores[1]
        return runner_up_score
    else:
        return "There is no runner-up, as there are not enough participants."

# Example usage:
if __name__ == "__main__":
    # Replace this list with the actual scores
    n = int(input("Number of Perticipents:"))
    arr = map(int, input("Enter score:").split())

    runner_up_score = find_runner_up_score(arr)

    print("Runnerup score is:",runner_up_score)
