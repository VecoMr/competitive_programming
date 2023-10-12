s = ""
d = {}
while (s := input()) != "-1":
    time, team, state = s.split()
    if not team in d:
        d[team] = {"state": state, "time": time, "try": int(state == "wrong")}
    else:
        if d[team]["state"] == "right":
            continue
        if state == "right":
            d[team]["state"] = state
            d[team]["time"] = time
        else:
            d[team]["try"] += 1
r = [0, 0]
for i in d:
    if d[i]["state"] == "right":
        r[0] += 1
        r[1] += int(d[i]["time"]) + int(d[i]["try"]) * 20

print(*r)