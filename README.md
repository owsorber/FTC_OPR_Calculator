# FTC OPR Calculator
This repository was built to efficiently calculate FTC team statistics such as OPR, Autonomous OPR, and CCWM at an FTC event.

 * OPR (Offensive Power Rating): Attempts to find each team’s robot’s average scoring contribution per match.
 * Autonomous OPR: Attempts to find each team's robot's average autonomous scoring contribution per match.
 * CCWM (Calculated Contribution to Winning Margin): On average, how many more/fewer points each team's robot scored than their opponents per match.

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
OPR.py is a Python program that parses data from teams.txt and matches.txt and loads the data into four different matrices. 

 * M: Matrix of alliances x teams where each item represents whether or not a team is in the alliance specified by the row.
 * Scores, Autos, and Margins: Single-column matrices of alliances x 1 with the scores of each alliance (Scores), autonomous scores of each alliance (Autos), and winning/losing margins for each alliance (Margins).
 
Finding the match statistics (OPR, Auto OPR, CCWM) for each team sets up a system of equations:
    Mx = R
where M is the matrix M, x is the statistic matrix of 1 x teams that we are solving for, and R is the results matrix, either Scores, Autos, or Margins.

Since the system is overdetermined with more equations (alliances) than variables (teams), the Python program multiplies the results matrix by the pseudo inverse of M to find the matrix x.

Math used inspired by: https://blog.thebluealliance.com/2017/10/05/the-math-behind-opr-an-introduction/

Then the program ranks the teams by OPR and outputs them to the screen.

@TODO: Load data into HTML file to nicely display data in browser?

