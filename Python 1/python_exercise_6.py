import random

# generate random values for cordinates (x,y)
def random_position():
  x = random.randint(1,8)
  y = random.randint(1,8)
  return [x,y]

# check if cordinates are unique/distinct ((1,1) !== ((1,1)))
def unique_position(position1,position2=[0,0]):
 available_position = random_position()
 if (available_position == position1 or available_position == position2):
  while 1:
   available_position =  random_position()
   if(available_position != position1 and available_position != position2):
    return available_position
 else:
  return available_position

def check_for_rook():
  # checks for rook
  points=0
  axis_x_rook=rook[0]
  axis_y_rook=rook[1]
  while axis_y_rook >0:
    if([axis_x_rook,axis_y_rook]==queen):
      points+=1
    axis_y_rook-=1 
  axis_y_rook=rook[1]

  while axis_y_rook <9:
    if([axis_x_rook,axis_y_rook]==queen):
      points+=1
    axis_y_rook+=1
  axis_y_rook=rook[1]

  while axis_x_rook >0:
    if([axis_x_rook,axis_y_rook]==queen):
      points+=1
    axis_x_rook-=1
  axis_x_rook=rook[0]

  while axis_x_rook <9:
    if([axis_x_rook,axis_y_rook]==queen):
      points+=1
    axis_x_rook+=1
  axis_x_rook=rook[0]
  return points

def check_for_bishop():
  points=0
  #checks for bishop
  axis_x_bishop=bishop[0]
  axis_y_bishop=bishop[1]

  while axis_x_bishop<9 and axis_y_bishop<9:
    if([axis_x_bishop,axis_y_bishop]==queen):
      points+=1
    axis_x_bishop+=1
    axis_y_bishop+=1
  axis_x_bishop=bishop[0]
  axis_y_bishop=bishop[1]

  while axis_x_bishop>0 and axis_y_bishop>0:
    if([axis_x_bishop,axis_y_bishop]==queen):
      points+=1
    axis_x_bishop-=1
    axis_y_bishop-=1
  axis_x_bishop=bishop[0]
  axis_y_bishop=bishop[1]

  while axis_x_bishop>0 and axis_y_bishop<9:
    if([axis_x_bishop,axis_y_bishop]==queen):
      points+=1
    axis_x_bishop-=1
    axis_y_bishop+=1
  axis_x_bishop=bishop[0]
  axis_y_bishop=bishop[1]

  while axis_x_bishop<9 and axis_y_bishop>0:
    if([axis_x_bishop,axis_y_bishop]==queen):
      points+=1
    axis_x_bishop+=1
    axis_y_bishop-=1
  axis_x_bishop=bishop[0]
  axis_y_bishop=bishop[1]
  return points

def check_for_queen():
  points = 0
  # straight attack
  axis_x_queen=queen[0]
  axis_y_queen=queen[1]
  while axis_y_queen >0:
    if([axis_x_queen,axis_y_queen]==bishop or [axis_x_queen,axis_y_queen]==rook):
      points+=1
    axis_y_queen-=1 
  axis_y_queen=queen[1]

  while axis_y_queen <9:
    if([axis_x_queen,axis_y_queen]==bishop or [axis_x_queen,axis_y_queen]==rook):
        points+=1
    axis_y_queen+=1
  axis_y_queen=queen[1]

  while axis_x_queen >0:
    if([axis_x_queen,axis_y_queen]==bishop or [axis_x_queen,axis_y_queen]==rook):
      points+=1
    axis_x_queen-=1
  axis_x_queen=queen[0]

  while axis_x_queen <9:
    if([axis_x_queen,axis_y_queen]==bishop or [axis_x_queen,axis_y_queen]==rook):
      points+=1
    axis_x_queen+=1 
  axis_x_queen=queen[0]
  axis_y_queen=queen[1]

  #diagonal attack 
  while axis_x_queen<9 and axis_y_queen<9:
    if([axis_x_queen,axis_y_queen]==bishop or [axis_x_queen,axis_y_queen]==rook):
      points+=1
    axis_x_queen+=1
    axis_y_queen+=1
  axis_x_queen=queen[0]
  axis_y_queen=queen[1]

  while axis_x_queen>0 and axis_y_queen>0:
    if([axis_x_queen,axis_y_queen]==bishop or [axis_x_queen,axis_y_queen]==rook):
      points+=1
    axis_x_queen-=1
    axis_y_queen-=1
  axis_x_queen=queen[0]
  axis_y_queen=queen[1]

  while axis_x_queen>0 and axis_y_queen<9:
    if([axis_x_queen,axis_y_queen]==bishop or [axis_x_queen,axis_y_queen]==rook):
      points+=1
    axis_x_queen-=1
    axis_y_queen+=1
  axis_x_queen=queen[0]
  axis_y_queen=queen[1]

  while axis_x_queen<9 and axis_y_queen>0:
    if([axis_x_queen,axis_y_queen]==bishop or [axis_x_queen,axis_y_queen]==rook):
      points+=1
    axis_x_queen+=1
    axis_y_queen-=1
  axis_x_queen=queen[0]
  axis_y_queen=queen[1]
  return points


# score for each team
white=0
black=0

# results after 100 games
for i in range(100):
  # initialize's the positions
  queen = random_position()
  bishop = unique_position(queen)
  rook = unique_position(queen,bishop)
  white+=check_for_rook()
  white+=check_for_bishop()
  black+=check_for_queen()


print("total points for black team:",black)
print("total points for white team:",white)


# todo fix the bug if the rook or the bishop is blocking the position
# example: 
# 1   2   3
# 4   5   6
# 7   8   9

# if my queen is at position 1
# bishop is at position 9
# rook is at position 5
# is rook blocking the bishop to check the queen ? 
# reply me if you want to fix it please! :)
