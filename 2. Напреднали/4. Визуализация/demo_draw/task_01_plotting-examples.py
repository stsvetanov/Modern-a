from matplotlib.pyplot import *
# import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [5,4,3,2]

figure()

# divide the figure into a 2 by 3 grid using a subplot(231) call. We could call this
# using subplot(3, 2, 1), where the first parameter is the number of rows, the second is
# the number of columns, and the third represents the plot number.
subplot(231)
plot(x, y)

subplot(232)
bar(x, y)

subplot(233)
barh(x, y)

subplot(234)
bar(x, y)
y1 = [7,8,5,3]
bar(x, y1, bottom=y, color = 'r')

subplot(235)
boxplot(x)

subplot(236)
scatter(x,y)

show()
