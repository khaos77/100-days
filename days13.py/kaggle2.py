def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    worst = teams[-1]
    return worst[1]
    pass


stin = input().split()
print(stin)
print(losing_team_captain(stin))

