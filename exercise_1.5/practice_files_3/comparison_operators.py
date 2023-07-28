class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
    
    def __str__(self):
        output = str(self.feet) + ' feet, ' + str(self.inches) + ' inches'
        return output
    
    def __gt__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        return height_A_inches > height_B_inches
    
    def __ge__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        return height_A_inches >= height_B_inches
    
    def __ne__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        return height_A_inches != height_B_inches
    
print(Height(4, 6) > Height(4, 5))
print(Height(4, 5)>= Height(4, 5))
print(Height(5, 9) != Height(5, 10))

