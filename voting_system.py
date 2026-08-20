candidates = {
    "A": 0,
    "B": 0,
    "C": 0
}

voters = set()

while True:

    print("\n===== VOTING SYSTEM =====")
    print("Candidates: A, B, C")
    print("Type 'result' to show results.")
    print("Type 'exit' to stop.")

    voter = input("Enter voter ID: ")

    if voter.lower() == "exit":
        break

    if voter.lower() == "result":

        print("\n--- Results ---")

        for candidate, votes in candidates.items():
            print(candidate, ":", votes)

        continue

    if voter in voters:
        print("You have already voted.")
        continue

    vote = input("Enter candidate: ").upper()

    if vote in candidates:

        candidates[vote] += 1
        voters.add(voter)

        print("Vote recorded successfully.")

    else:
        print("Invalid candidate.")
