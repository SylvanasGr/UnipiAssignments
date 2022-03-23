import random

# generate random values for cordinates (x,y)
def random_position(min=1,max=8):
  x = random.randint(min,max)
  y = random.randint(min,max)
  if(min==0 and max ==0):
   x=random.randint(1,7)
   y=random.randint(1,8)
  return [x,y]

# check if cordinates are unique/distinct ((1,1) !== ((1,1)))
def unique_position(position,min=1,max=8):
 if(min==0 and max ==0):
  available_position = random_position(0,0)
 else:
  available_position = random_position(min,max)
 if (available_position == position):
  while 1:
   available_position =  random_position(min,max)
   if(available_position != position):
    return available_position
 else:
  return available_position

def check_for_rook():
  # checks for rook
  points=0
  axis_x_rook=rook[0]
  axis_y_rook=rook[1]
  while axis_y_rook >0:
    if([axis_x_rook,axis_y_rook]==bishop):
      points+=1
    axis_y_rook-=1 
  axis_y_rook=rook[1]

  while axis_y_rook <9:
    if([axis_x_rook,axis_y_rook]==bishop):
      points+=1
    axis_y_rook+=1
  axis_y_rook=rook[1]

  while axis_x_rook >0:
    if([axis_x_rook,axis_y_rook]==bishop):
      points+=1
    axis_x_rook-=1
  axis_x_rook=rook[0]

  while axis_x_rook <9:
    if([axis_x_rook,axis_y_rook]==bishop):
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
    if([axis_x_bishop,axis_y_bishop]==rook):
      points+=1
    axis_x_bishop+=1
    axis_y_bishop+=1
  axis_x_bishop=bishop[0]
  axis_y_bishop=bishop[1]

  while axis_x_bishop>0 and axis_y_bishop>0:
    if([axis_x_bishop,axis_y_bishop]==rook):
      points+=1
    axis_x_bishop-=1
    axis_y_bishop-=1
  axis_x_bishop=bishop[0]
  axis_y_bishop=bishop[1]

  while axis_x_bishop>0 and axis_y_bishop<9:
    if([axis_x_bishop,axis_y_bishop]==rook):
      points+=1
    axis_x_bishop-=1
    axis_y_bishop+=1
  axis_x_bishop=bishop[0]
  axis_y_bishop=bishop[1]

  while axis_x_bishop<9 and axis_y_bishop>0:
    if([axis_x_bishop,axis_y_bishop]==rook):
      points+=1
    axis_x_bishop+=1
    axis_y_bishop-=1
  axis_x_bishop=bishop[0]
  axis_y_bishop=bishop[1]
  return points

# score for each team
white=0
black=0
for i in range(100):
# initialize's the positions
 rook=random_position()
 bishop=unique_position(rook)
 white+=check_for_rook()
 black+=check_for_bishop()

print("-----------------------------------")
print("total for white for game 8x8:",white)
print("total for black for game 8x8:",black)

white=0
black=0
for i in range(100):
 rook=random_position(1,7)
 bishop=unique_position(rook,1,7)
 white+=check_for_rook()
 black+=check_for_bishop()

print("-----------------------------------")
print("total for white for game 7x7:",white)
print("total for black for game 7x7:",black)

white=0
black=0
for i in range(100):
 rook=random_position(0,0)
 bishop=unique_position(rook,0,0)
 white+=check_for_rook()
 black+=check_for_bishop()

print("-----------------------------------")
print("total for white for game 7x8:",white)
print("total for black for game 7x8:",black)
