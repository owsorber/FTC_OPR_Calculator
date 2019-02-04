# FTC OPR Calculator
This repository was built to efficiently calculate FTC team statistics such as OPR, Autonomous OPR, and CCWM at an FTC event.

 * OPR (Offensive Power Rating): Attempts to find each team’s robot’s average scoring contribution per match.
 * CCWM (Calculated Contribution to Winning Margin): On average, how many more/fewer points each team's robot scored than their opponents per match.

Math used inspired by: https://blog.thebluealliance.com/2017/10/05/the-math-behind-opr-an-introduction/

## teams.txt
A plain text file where every team at an FTC event can be entered. For simplicity, teams are entered in the form:
  teamNum, teamName
The Python program OPR.py then instantiates a Team object for each team entered.

## matches.txt
A plain text file where the match data from an FTC event can be manually entered by scouts. Each match's data is 
represented with a new line, in the form:
  redTeam1, redTeam2, redScore, redAuto, blueTeam1, blueTeam2, blueScore, blueAuto
The Python program OPR.py then instantiates a Match object for each team entered.

## OPR.py
