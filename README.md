## FTC_OPR_Calculator
This repository was built to efficiently calculate FTC team statistics such as OPR, Autonomous OPR, and CCWM at an FTC event.

# teams.txt
A plain text file where every team at an FTC event can be entered. For simplicity, teams are entered in the form:
  teamNum, teamName
The Python program OPR.py then instantiates a Team object for each team entered.

# matches.txt
A plain text file where the match data from an FTC event can be manually entered by scouts. Each match's data is 
represented with a new line, in the form:
  redTeam1, redTeam2, redScore, redAuto, blueTeam1, blueTeam2, blueScore, blueAuto
The Python program OPR.py then instantiates a Match object for each team entered.

# OPR.py
