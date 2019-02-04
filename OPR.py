#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FTC Team Statistics Calculator
@author: owsorber

OPR = Offensive Power Rating
CCWM = Calculated Contribution to Winning Margin
"""

import numpy # has matrix calculations

class Alliance:
    def __init__(self, team1, team2, score, auto, col):
        self.team1 = team1
        self.team2 = team2
        self.score = score
        self.auto = auto
        self.col = col
        if (self.auto > self.score):
            raise ValueError("Autonomous score cannot be higher than Overall score.")
    
    def __str__(self):
        return self.col + " Alliance: " + str(self.team1) + ", " + (self.team2)

class Match:
    def __init__(self, num, redAlliance, blueAlliance):
        self.num = num
        self.redAlliance = redAlliance
        self.blueAlliance = blueAlliance
    
    def __str__(self):
        return "Match # " + str(self.num) + ": (" + str(self.redAlliance.team1.num) + " & " + str(self.redAlliance.team2.num) + ") " + str(self.redAlliance.score) + " - " + str(self.blueAlliance.score) + " (" + str(self.blueAlliance.team1.num) + " & " +  str(self.blueAlliance.team2.num) + ")"


""" 
Loads the teams of an FTC event into a dictionary from an external txt file.
The dictionary maps a team number to a team name.
"""
def loadTeams(filename):
    teams = {}
    
    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(', ')
        teams[int(line_data[0])] = line_data[1][0:len(line_data[1]) - 1]
    
    return teams

""" 
Loads the match data of an FTC event into a list from an external txt file.
Assumes the format of each line in the txt file is:
red1, red2, redscore, redauto, blue1, blue2, bluescore, blueauto
"""
def loadMatches(filename):
    matches = []
    
    f = open(filename, 'r')
    
    matchNum = 1
    for line in f:
        line_data = line.split(', ')
        red1 = int(line_data[0])
        red2 = int(line_data[1])
        redscore = int(line_data[2])
        redauto = int(line_data[3])
        redAlliance = Alliance(red1, red2, redscore, redauto, "Red")
        
        blue1 = int(line_data[4])
        blue2 = int(line_data[5])
        bluescore = int(line_data[6])
        blueauto = int(line_data[7])
        blueAlliance = Alliance(blue1, blue2, bluescore, blueauto, "Blue")
        
        matches.append(Match(matchNum, redAlliance, blueAlliance))
        matchNum += 1
    
    return matches

# Load teams and matches from txt files
teams = loadTeams("teams-robostorm4.3.txt")
matches = loadMatches("matches-robostorm4.3.txt")

""" 
Build M, a matrix of alliances x teams, where each row indicates the teams in that alliance.
A value of 1 means the team was in that alliance and a value of 0 means the team was not.
First loop through each red alliance and then loop through each blue alliance.
The resulting matrix should have 2 * len(matches) rows.
"""
M = []
for match in matches:
    r = []
    for team in teams:
        if match.redAlliance.team1 == team or match.redAlliance.team2 == team:
            r.append(1)
        else:
            r.append(0)
    M.append(r)
    
    b = []
    for team in teams:
        if match.blueAlliance.team1 == team or match.blueAlliance.team2 == team:
            b.append(1)
        else:
            b.append(0)
    M.append(b)

"""
Build Scores, a matrix of alliances x 1, where each row indicates the score of that alliance.
Build Autos, a matrix of alliances x 1, where each row indicates the autonomous score of that alliance.
Build Margins, a matrix of alliances x 1, where each row indicates the margin of victory/loss 
of that alliance (e.g. if an alliance wins 60-50, the value is +10).
The alliance represented by each row corresponds to the alliance represented by each row
in the matrix M.
"""
Scores = []
Autos = []
Margins = []
for match in matches:
    Scores.append([match.redAlliance.score])
    Scores.append([match.blueAlliance.score])
    Autos.append([match.redAlliance.auto])
    Autos.append([match.blueAlliance.auto])
    Margins.append([match.redAlliance.score - match.blueAlliance.score])
    Margins.append([match.blueAlliance.score - match.redAlliance.score])


# Convert all matrices from type list to type matrix using numpy
M = numpy.matrix(M)
Scores = numpy.matrix(Scores)
Autos = numpy.matrix(Autos)
Margins = numpy.matrix(Margins)

""" 
Find the pseudoinverse of the matrix M. Multiplying this by a results matrix will find the
solution to the overdetermined system of equations.
"""
pseudoinverse = numpy.linalg.pinv(M)
OPRs = numpy.matmul(pseudoinverse, Scores)
AUTOs = numpy.matmul(pseudoinverse, Autos)
CCWMs = numpy.matmul(pseudoinverse, Margins)

# Converts any stat represented by a matrix into a list, used later for sorting
def convertToList(statMatrix):
    l = []
    for val in statMatrix:
        l.append(round(float(val), 3))
    return l

""" Sort the teams by OPR. Created sortedTeams, sortedOPR, and sortedCCWM accordingly. """
teamsList = [] # unsorted list of teams
sortedTeams = []
sortedOPR = []
sortedAuto = []
sortedCCWM = []

for team in teams:
    teamsList.append(team)

while len(sortedTeams) < len(teamsList):
    oprs = convertToList(OPRs)
    autos = convertToList(AUTOs)
    ccwms = convertToList(CCWMs)
    
    # Get the first team not already sorted to compare all the other teams to that team
    for i in range(len(teamsList)):
        if teamsList[i] not in sortedTeams:
            bestTeam = teamsList[i]
            bestOPR = oprs[i]
            bestAUTO = autos[i]
            bestCCWM = ccwms[i]
            break
    
    # Loop through teamsList to find next best team
    for i in range(len(teamsList)):
        if oprs[i] > bestOPR and teamsList[i] not in sortedTeams:
            bestTeam = teamsList[i]
            bestOPR = oprs[i]
            bestAUTO = autos[i]
            bestCCWM = ccwms[i]
    sortedTeams.append(bestTeam)
    sortedOPR.append(bestOPR)
    sortedAuto.append(bestAUTO)
    sortedCCWM.append(bestCCWM)

        
""" Print the data to the screen """
print("\nTEAM\t\tOPR\t\tAuto\t\tCCWM\t\tTeam Name")
for i in range(len(teamsList)):
    teamNum = sortedTeams[i]
    print("Team " + str(teamNum) + "\t" + str(sortedOPR[i]) + "\t\t" + str(sortedAuto[i]) +\
          "\t\t" + str(sortedCCWM[i]) + "\t\t" + str(teams[teamNum]))

