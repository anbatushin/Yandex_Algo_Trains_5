def ExecReqs(coms):
    teams, players = {}, {}
    t1, t2 = 0, 0

    for i in range(len(coms)):
        s = coms[i].replace("'", '').split()
        code = s[0] + s[1] + s[2] if len(s) >= 3 else ''

        if '-' in s:
            team1, team2 = ' '.join(s[:s.index('-')]), ' '.join(s[s.index('-') + 1:-1])
            t1, t2 = map(int, s[-1].split(':'))
            min_time_1, min_time_2 = 91, 91

            for team in [team1, team2]:
                if team not in teams:
                    teams[team] = [set(), 0, 0]
                teams[team][1] += 1
                for player in teams[team][0]:
                    players[player][0].clear()

        elif code == 'Totalgoalsfor':
            team = ' '.join(s[s.index('for') + 1:])
            print(sum(players[player][1] for player in teams.get(team, [set()])[0]))

        elif code == 'Totalgoalsby':
            player = ' '.join(s[s.index('by') + 1:])
            print(players.get(player, [None, 0])[1])

        elif code == 'Meangoalsper' and len(s) > 5:
            sum_goals = 0
            if s[4] == 'for':
                team = ' '.join(s[s.index('for') + 1:])
                if team in teams:
                    sum_goals = sum(players[player][1] for player in teams[team][0]) / teams[team][1]
            elif s[4] == 'by':
                player = ' '.join(s[s.index('by') + 1:])
                if player in players:
                    for team in teams:
                        if player in teams[team][0]:
                            sum_goals = players[player][1] / teams[team][1]
                            break
            print(sum_goals)

        elif code == 'Goalsonminute':
            minute = int(s[s.index('minute') + 1])
            player = ' '.join(s[s.index('by') + 1:])
            print(players[player][3].get(minute, 0) if player in players else 0)

        elif code == 'Goalsonfirst':
            minute = int(s[s.index('first') + 1])
            player = ' '.join(s[s.index('by') + 1:])
            print(sum(goal for t, goal in players[player][3].items() if t <= minute) if player in players else 0)

        elif code == 'Goalsonlast':
            minute = int(s[s.index('last') + 1])
            player = ' '.join(s[s.index('by') + 1:])
            print(sum(goal for t, goal in players[player][3].items() if t >= 91 - minute) if player in players else 0)

        elif code == 'Scoreopensby':
            name = ' '.join(s[s.index('by') + 1:])
            print((teams.get(name, [None, None, 0])[2] if name in teams else players.get(name, [None, None, 0])[2]))

        elif t1 > 0 or t2 > 0:
            player = ' '.join(s[:-1])
            current_team = team1 if t1 > 0 else team2
            teams[current_team][0].add(player)

            if player not in players:
                players[player] = [set(), 0, 0, {}]
            players[player][0].add(int(s[-1]))
            players[player][3][int(s[-1])] = players[player][3].get(int(s[-1]), 0) + 1
            players[player][1] += 1

            if t1 > 0:
                if min_time_1 == 91:
                    min_player_1, min_time_1 = player, int(s[-1])
                t1 -= 1
            else:
                if min_time_2 == 91:
                    min_player_2, min_time_2 = player, int(s[-1])
                t2 -= 1

            if t1 == 0 and t2 == 0:
                if min_time_1 < min_time_2:
                    teams[team1][2] += 1
                    players[min_player_1][2] += 1
                elif min_time_2 < min_time_1:
                    teams[team2][2] += 1
                    players[min_player_2][2] += 1
                min_time_1, min_time_2 = 92, 92


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    ExecReqs(lines)
