############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless= is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    
    musk = MelonType('Muskmelon', 'musk', 1998, 'green',
                     True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('Casaba', 'cas', 2003, 'orange',
                     True, False)
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    all_melon_types.append(cas)

    cren = MelonType('Crenshaw', 'cren', 1996, 'green',
                     True, False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('Yellow Watermelon', 'yw', 2013, 'yellow',
                     True, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)


    # Fill in the rest
    print(all_melon_types)
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest

    for melon in melon_types:
        print("{} pairs with".format(melon.name))

        for pairing in melon.pairings:
            print("- {}".format(pairing))


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_dict = {}

    for melon in melon_types:
        key = melon.code
        melon_dict[key] = melon

    return melon_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(self, code, shape_rating, color_rating, field, harvester):
        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester
        self.sellable = bool()

    def is_sellable(self):
        if self.shape_rating > 5 && self.color_rating > 5 && self.field != 3:
            self.sellable = True
        else:
            self.sellable = False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    all_melon_types = []
    melon_1 = Melon('yw',8,7,2,'Sheila')
    melon_2 = Melon('yw',3,4,2,'Sheila')
    melon_3 = Melon('yw',9,8,3,'Sheila')
    melon_4 = Melon('cas',10,6,35,'Sheila')
    melon_5 = Melon('cren',8,9,35,'Michael')
    melon_6 = Melon('cren',8,2,35,'Michael')
    melon_7 = Melon('cren',2,3,4,'Michael')
    melon_8 = Melon('musk',6,7,4,'Michael')
    melon_9 = Melon('yw',7,10,3,'Sheila')

    all_melon_types.append(melon_1)
    all_melon_types.append(melon_2)
    all_melon_types.append(melon_3)
    all_melon_types.append(melon_4)
    all_melon_types.append(melon_5)
    all_melon_types.append(melon_6)
    all_melon_types.append(melon_7)
    all_melon_types.append(melon_8)
    all_melon_types.append(melon_9)

    return all_melon_types




def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



