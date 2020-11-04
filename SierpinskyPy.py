import turtle
turtle.tracer(0,0)
turtle.screensize(1000,1000)
turtle.pu()
turtle.goto(-0,0)
turtle.pd()


def dessiner(courbe, longueur, angle):
    for caractere in courbe:
        if caractere == '+': turtle.left(angle)
        elif caractere == 'F': turtle.forward(longueur)

def DefinitionA(longueur, angle): 
  SequenceA = 'FF++FF++FF++F+F++F++F+'
  dessiner(SequenceA,longueur,angle)

def DefinitionB(longueur, angle):
  SequenceB = 'F++FF'
  dessiner(SequenceB,longueur,angle)

def DefinitionC(counter,longueur, angle):
  DefinitionA(longueur,angle)
  for i in range(3):
    if counter>1:
      DefinitionC(counter-1,longueur*0.5,angle)
  DefinitionB(longueur,angle)
  return counter-1

longueur = 128
angle = 60
niter = 5

counter = niter;

if counter >= 0:
  counter = DefinitionC(counter, longueur, angle)

turtle.update()      # accélération du tracé
turtle.exitonclick() # permet la fermeture de la fenêtre graphique
