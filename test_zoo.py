from zoo_bird import Bird
from zoo_lion import Lion
from zoo_reptile import Reptile

# create instances
lion = Lion("Shera", 21)
bird = Bird("Chile", 30)
reptile = Reptile("Seraph", 12)

# lion
lion.describe()
lion.make_sound()
lion.roar()

# bird
bird.describe()
bird.make_sound()
bird.fly()

# reptile
reptile.describe()
reptile.make_sound()
reptile.crawl()