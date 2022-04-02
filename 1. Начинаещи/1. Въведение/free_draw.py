import turtle

edges = input("Enter # of edges (Default 5): ")
edges = edges or "5"
edges = int(edges)


angle = 360 / edges

turtle.left(angle)
turtle.forward(150)

count = 0
while count < edges:
    turtle.right(angle * 2)
    turtle.forward(150)
    count += 1

turtle.done()