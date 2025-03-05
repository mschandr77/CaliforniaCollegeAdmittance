import history
import english
import math
import elective
import otherlang
import science
import visualart
from history import combinedHistory
from english import combinedEnglish
from math import combinedMath
from elective import elGPA
from otherlang import combinedother_lang
from science import combinedScience
from visualart import vGPA


def calculate_gpa():
    calculatedGPA = 15 / (combinedHistory + combinedEnglish + combinedMath + combinedScience + combinedother_lang + vGPA + elGPA)
    print("Your calculated UC GPA is: ", str(calculatedGPA) + ".")