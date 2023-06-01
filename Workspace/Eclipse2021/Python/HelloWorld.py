print("Hello World")
print(7+6)

# from alive_progress.styles import showtime
# showtime()

from progress.bar import Bar

bar = Bar('Processing', max=20)
for i in range(20):
    # Do some work
    bar.next()
bar.finish()