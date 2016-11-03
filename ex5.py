my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

def kg(lbs):
    kg = lbs / 2.2046
    return kg

def cm(inch):
    cm = inch * 2.54
    return cm

print "Let's talk about %s" % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# This line is trichy, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

print "My weight %d in kg is %d" % (my_weight, kg(my_weight))
print "hy height %d in cm is %d" % (my_height, cm(my_height))
