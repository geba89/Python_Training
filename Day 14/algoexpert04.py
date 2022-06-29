from contextlib import nullcontext


def tournamentWinner(competitions, results):
    teams = {}
    # get team names
    for team in competitions:
        for names in team:
            if names not in teams:
                teams[names] = 0
    
    #iterate through matches and add points to winning teams
    for i in range(0, len(results)):
        if results[i] == 0:
            teams[competitions[i][1]] += 1
        else:
            teams[competitions[i][0]] += 1
    
    #find winner
    winning_team = ""
    points = 0
    for team in teams:
        if teams[team] > points:
            winning_team = team
            points = teams[team]
    return winning_team

comp = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"]]
results = [0,1,1]

win = tournamentWinner(comp, results)
print(win)