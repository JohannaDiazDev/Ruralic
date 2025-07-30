import turtle
#Logo Ruralic

#Configuración de la pantalla
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#143959")
screen.title("Ruralic Logo")
#Configuración de la turtle
t = turtle.Turtle()
t.speed(3)
t.color("white")

def draw_logo():
#Linea diagonal izquierda
    t.pensize(14)
    t.penup()
    t.goto(-30, 180)
    t.pendown()
    t.goto(180, -60)
  
    #Linea diagonal derecha
    t.penup()
    t.goto(30, 180)
    t.pendown()
    t.goto(-180, -60)
    
    #linea horizontal techo
    t.penup()
    t.goto(-190, -40)
    t.pendown()
    t.pensize(6)
    t.goto(190, -40)
    
    #primer linea vertical
    t.penup()
    t.goto(-150, -40)
    t.pendown()
    t.goto(-150, -210)
    
    #segunda linea vertical desde la base
    t.penup()
    t.goto(-80, -210)
    t.pendown()
    t.goto(-80, 120)
    
    #tercera linea vertical sobrepasa la diagonal
    t.penup()
    t.goto(100, -210)
    t.pendown()
    t.goto(100, 120)
    
    #cuarta linea vertical desde la base
    t.penup()
    t.goto(160, -210)
    t.pendown()
    t.goto(160, -40)
 
    #segunda linea horizontal
    t.penup()
    t.goto(-190, -210)
    t.pendown()
    t.goto(190, -210)
    
    #primer puerta
    t.penup()
    t.goto(-20, -210)
    t.pendown()
    t.goto(-20, -140)
    t.goto(30, -140)
    t.goto(30, -210)
  
    #segunda puerta
    t.penup()
    t.goto(-10, -210)
    t.pendown()
    t.goto(-10, -148)
    t.goto(40, -148)
    t.goto(40, -210)
   
    #ventana 1
    t.pensize(3)
    t.penup()
    t.goto(-10, -10)
    t.pendown()
    t.goto(-10, 25)
    t.goto(30, 25)
    t.goto(30, -10)
    t.goto(-10, -10)
    
    #cruz linea horizontal
    t.pensize(3)
    t.penup()
    t.goto(10, -10)
    t.pendown()
    t.goto(10, 25)
    
    #cruz linea vertical
    t.pensize(3)
    t.penup()
    t.goto(-10, 7.5)
    t.pendown()
    t.goto(30, 7.5)
    
    #segunda ventana
    t.pensize(3)
    t.penup()
    t.goto(-16.3, -15)
    t.pendown()
    t.goto(-16.3, 30)
    t.goto(23, 30)
    t.goto(23, -15)
    t.goto(-16.3, -15)
    
    #cruz segunda ventana
    t.pensize(3)
    t.penup()
    t.goto(5, -10)
    t.pendown()
    t.goto(5,30)
    
    #cruz segunda ventana 
    t.penup()
    t.goto(-16.3,10)
    t.pendown()
    t.goto(23,10)
    
draw_logo()   
turtle.done()