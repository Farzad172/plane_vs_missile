import pygame as p
import sys
import random as r

p.init()

#screen
display = p.display.set_mode((0,0),p.FULLSCREEN)

#font
p.font.init()
font = p.font.SysFont('Comic Sans MS',30)

#background
pic1 = p.image.load(r"starfield.png")
pic1 = p.transform.scale(pic1,(1023,765))

#clock
clock = p.time.Clock()

#transparant(invisible)
transparent = (0,0,0,0)

#welcome
welcome = '''Welcome to MFA Gaming Zone presents KEEP YOUR PLANE ALIVE'''
loading = "Loading..."

#welcome screen
welcome = font.render(welcome,True,(199,133,22))
loading = font.render(loading,False,(13,222,21))

display.blit(pic1,(0,0))
display.blit(welcome,(20,766/2))
p.display.flip()
p.time.delay(3000)

display.fill(transparent)

display.blit(pic1,(0,0))
display.blit(loading,(1022/2,766/2))
p.display.flip()
p.time.delay(3000)

#score,life
SCORE = 0
LIFE = 3
font = p.font.SysFont("Segoe UI",20)
Life = font.render('LIFE:',True,(202,23,192))
Score = font.render('SCORE:',True,(202,23,192))

#image
plane = p.image.load(r"plane.png")
plane = p.transform.scale(plane,(170,200))
missile = p.image.load(r"missile.png")
missile = p.transform.scale(missile,(20,100))
firebox = p.image.load(r"firebox.png")
firebox = p.transform.scale(firebox,(190,220))
gameover = p.image.load(r"gameover.png")
gameover = p.transform.scale(gameover,(550,400))
life = p.image.load(r"heart.png")
life = p.transform.scale(life,(20,20))

#plane choose
infinite = True


#b_move_var
x = 0
y = 0
w,h = pic1.get_size()
pic1_rect = pic1.get_rect()
x1 = 0
y1 = -h
px = 420
py = 500
mx = r.randint(100,800)
my = -100
fy = 500

#life animation
def l(LIFE):
 if LIFE == 3:
   display.blit(life,(920,15))
   display.blit(life,(950,15))
   display.blit(life,(980,15))
   p.display.flip()
 elif LIFE == 2:
   display.blit(life,(920,15))
   display.blit(life,(950,15))
   p.display.flip()
 elif LIFE == 1:
   display.blit(life,(920,15))
   p.display.flip()
 else:
   display.blit(life,(-30,-20))

#score
def sc(SCORE):
  s = font.render("%d"%SCORE,True,(202,23,192))
  display.blit(s,(90,10))
  p.display.flip()

while infinite:

  p.display.set_caption("KEEP ALIVE YOUR PLANE")
  
  if my != 500:
    my+=30

  else:
    my = -100
    mx = r.randint(100,800)
    SCORE+=10
    
  for event in p.event.get():
    if event.type == p.KEYDOWN:
      if event.key == p.K_q:
        p.quit()
        sys.exit()
        infinite = False
        
      elif event.key == p.K_RIGHT:
        px+=60
        if px >= 900:
          px = 420
          event.key == False
     
      elif event.key == p.K_LEFT:
        px-=60
        if px <= 0:
          px = 420
          event.key == False
   
  y1+=5
  y+=5
  
  display.blit(pic1,(x,y))
  display.blit(pic1,(x1,y1))
  display.blit(plane,(px,py))
  display.blit(missile,(mx,my))
  display.blit(Life,(880,10))
  l(LIFE)
  display.blit(Score,(20,10))
  sc(SCORE)
  

  if (y > h):
       y = -h
  if y1 > h:
       y1 = -h

  if py == my and px<= mx and (px+160)>= mx:
    if LIFE == 0:
      SCORE-=20
      display.blit(firebox,(px,fy))
      p.display.flip()
      p.time.delay(3000)
      display.blit(pic1,(0,0))
      display.blit(gameover,(225,130))
      p.display.flip()
      p.time.delay(5000)
      p.quit()
      sys.exit()
      infinite = False
    else:
      LIFE-=1
      SCORE-=20
      display.blit(firebox,(px,fy))
      p.display.flip()
      p.time.delay(2000)
      
  p.display.update()
  p.display.flip()
  clock.tick(60)


