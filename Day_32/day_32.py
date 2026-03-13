def basic_recap():
    dictA = {"car1":"Audi","car2":"BMW","car3":"TATA","car4":"Mahindra"}
    print(type(dictA))
    print(dictA)
    dictA["car5"]="Mercedes"
    print(dictA["car2"])
    print(dictA)

from collections import defaultdict, Counter

def optimize_logs(logs):
    user_actions = defaultdict(Counter)
    user_metadata_keys = defaultdict(set)
    user_leaders = {}
    for log in logs:
        uid = log['user_id']
        act = log['action']
        ts = log['timestamp']
        meta = log['metadata']
        user_actions[uid][act] += 1
        user_metadata_keys[uid].update(meta.keys())
        current_count = user_actions[uid][act]
        if uid not in  user_leaders:
            user_leaders[uid] = (current_count, ts, act)
        else:
            leader_count, leader_ts, leader_act = user_leaders[uid]
            if current_count > leader_count or (current_count == leader_count and ts > leader_ts):
                user_leaders[uid] = (current_count, ts, act)
    return{
            uid: {
                "top_action": user_leaders[uid][2],
                "unique_metadata_count":len(user_metadata_keys[uid])
            } for uid in user_actions
        }
logs = [
    {'user_id': 1, 'action': 'login', 'timestamp': 100, 'metadata': {'ip': '1.1.1.1'}},
    {'user_id': 1, 'action': 'click', 'timestamp': 105, 'metadata': {'btn': 'buy'}},
    {'user_id': 1, 'action': 'login', 'timestamp': 110, 'metadata': {'ip': '1.1.1.1', 'device': 'mobile'}}
]
print(optimize_logs(logs))
