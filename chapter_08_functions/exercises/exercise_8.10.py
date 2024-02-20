def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    for index, magician in enumerate(magicians):
        magicians[index] += " the Great"

magicians = ['harry potter', 'denis', 'sarah']
make_great(magicians=magicians)
show_magicians(magicians=magicians)
