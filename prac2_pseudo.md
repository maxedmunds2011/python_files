START

DISPLAY "Choose Rock, Paper, or Scissors:"
INPUT Rock
INPUT Paper
INPUT Scissors

Rock is 1
Paper is 2
Scissors is 3

SET computer_choice TO Rock, Paper, Scissors

IF player_choice = computer_choice THEN
    DISPLAY Draw

ELSE IF player_choice = 2 computer_choice = 1 THEN
    DISPLAY Win

ELSE IF player choice = 3 computer_choice = 2 THEN
    DISPLAY Win

ELSE IF player_choice = 1 computer_choice = 3 THEN
    DISPLAY Win

ELSE IF player_choice = 1 computer_choice = 2 THEN
    DISPLAY Lose

ELSE IF player_choice = 2 computer_choice = 3 THEN
    DISPLAY Lose

ELSE
    DISPLAY Lose

END
