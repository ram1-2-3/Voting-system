candidates = ['A', 'B', 'C']
votes = {'A': 0, 'B': 0, 'C': 0}
voters = []
total_voters = 15
print("---- Voting System ----")
print("Candidates: A, B, C")
for i in range(1, total_voters + 1):
    print(f"\nVoter {i}")
    name = input("Enter voter name: ")
    voter_id = input("Enter voter ID: ")
    while True:
        choice = input("Vote (A/B/C): ").upper()
        if choice in candidates:
            break
        else:
            print("Invalid choice! Please vote A, B, or C.")
    voters.append({
        'name': name,
        'id': voter_id,
        'vote': choice
    })
    votes[choice] += 1
print("\n---- Voting Details ----")
for v in voters:
    print(f"Name: {v['name']}, ID: {v['id']}, Voted: {v['vote']}")
print("\n---- Vote Count ----")
for c in candidates:
    print(f"Candidate {c}: {votes[c]} votes")
winner = max(votes, key=votes.get)
print("\n---- Result ----")
print(f"Winner is Candidate {winner} with {votes[winner]} votes")