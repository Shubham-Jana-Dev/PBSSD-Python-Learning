def basic_recap():
    dictA = {"car1":"Audi","car2":"BMW","car3":"TATA","car4":"Mahindra"}
    print(type(dictA))
    print(dictA)
    dictA["car5"]="Mercedes"
    print(dictA["car2"])
    print(dictA)

'''
The Challenge: The "Audit Log" Optimizer
​You are building a high-frequency trading system. You receive a list of transactions (logs) as a list of dictionaries. Each dictionary contains: {'user_id': int, 'timestamp': int, 'action': str, 'metadata': dict}.
​Your Task:
Write a function that processes 100,000 logs and returns a Nested Dictionary Summary that maps:
​Each user_id to their most frequent action.
​Each user_id to the total number of unique keys present in all of their metadata dictionaries combined.
​⚔️ The Constraints (Technical Brutality):
​Time Complexity: You must achieve O(N + U \cdot M), where N is the number of logs, U is the number of unique users, and M is the average number of unique metadata keys. If you use a nested loop that results in O(N^2), you’ve failed.
​Memory Efficiency: Do not create redundant copies of the log list. Use collections.defaultdict or collections.Counter to keep the logic lean.
​Architect Optimization: Handle the case where a user has a "tie" for the most frequent action. How do you decide which one to return? (Hint: Use the most recent one based on timestamp).
'''
