import turtle as tl





def courbeVonKoch(  n, cote  ) :
	if n == 0 :
		tl.forward(cote)
	else :

		courbeVonKoch(n-1, cote/3)
		tl.left(60)
		courbeVonKoch(n-1, cote/3)
		tl.left(-120)
		courbeVonKoch(n-1, cote/3)
		tl.left(60)
		courbeVonKoch(n-1, cote/3)

tl.setheading(0) # orientation intiale de la tête : vers la droite de l'écran
tl.hideturtle() # on cache la tortue
tl.speed(0)	 # on accélère la tortue
tl.color('pink')
courbeVonKoch(  n = 9, cote = 20000 )
tl.exitonclick() # pour  garder ouverte la fenêtre
