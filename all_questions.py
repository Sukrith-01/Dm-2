# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------

def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] = 0.27801

    level1["cough"] = - 1.0
    level1["cough_info_gain"] = 0.2364

    level1["radon"] = - 1.0
    level1["radon_info_gain"] = 0.0348

    level1["weight_loss"] = - 1.0
    level1["weight_loss_info_gain"] = 0.0290

    level2_left["smoking"] = - 1.0
    level2_left["smoking_info_gain"] = 0.0
    level2_right["smoking"] = - 1.0
    level2_right["smoking_info_gain"] = 0.0

    level2_left["radon"] = - 1.0
    level2_left["radon_info_gain"] = 0.07290

    level2_left["cough"] = 1.0
    level2_left["cough_info_gain"] = 0.72192

    level2_left["weight_loss"] = - 1.0
    level2_left["weight_loss_info_gain"] = 0.1709

    level2_right["radon"] = 1.0
    level2_right["radon_info_gain"] = 0.7219

    level2_right["cough"] = - 1.0
    level2_right["cough_info_gain"] = 0.32192

    level2_right["weight_loss"] = - 1.0
    level2_right["weight_loss_info_gain"] = 0.17095

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("smoking")  # MUST STILL CREATE THE TREE *****
    A = tree.insert_left("cough")
    B = tree.insert_right("radon")
    A.insert_left("Yes")
    A.insert_right("No")
    B.insert_left("Yes")
    B.insert_right("No")
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0  

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    answer["(a) entropy_entire_data"] = 1.4253642047367425

    answer["(b) x <= 0.2"] = 0.17739286055515824
    answer["(b) x <= 0.7"] = 0.3557029418697566
    answer["(b) y <= 0.6"] = 0.34781842724338197

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "y=0.6"  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("y <= 0.6")
    left = tree.insert_left("x <= 0.7")
    right = tree.insert_right("x <= 0.2")

    left.insert_left("B")
    
    y_03 = left.insert_right("y <= 0.3")
    y_03.insert_left("A")
    y_03.insert_right("C")

    right.insert_right("A")
    y_08 = right.insert_left("y <= 0.8")
    y_08.insert_right("B")
    y_08.insert_left("C")

    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    

    # float
    answer["(a) Gini, overall"] = 0.5

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.1625
    answer["(e) Gini, Shirt type"] = 0.4914

    answer["(f) attr for splitting"] = "Car type"

    # Explanatory text string
    answer["(f) explain choice"] = "The attribute 'Car type' demonstrates the lowest Gini index, suggesting superior subset purity post-split, thus making it the most favorable selection for the root node."
    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ['binary','qualitative','ordinal']

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = "The binary qualitative attribute 'Time' denotes either AM or PM, encompassing two distinct categories."
    answer["b"] = ['continuous','quantitative','ratio']
    answer["b: explain"] = "The brightness, as assessed by a light meter, is a continuous quantitative attribute that can be measured on a ratio scale."

    answer["c"] = ['discrete','qualitative','ordinal']
    answer["c: explain"] = "Judgments of brightness by individuals can be viewed as a qualitative attribute that is continuous and ordinal, reflecting subjective perceptions arranged based on intensity."

    answer["d"] = ['continuous','quantitative','ratio']
    answer["d: explain"] = "Angles, ranging from 0 to 360 degrees, are quantitative attributes that are continuous and represent ratios on a scale."
    answer["e"] = ['discrete','qualitative','ordinal']
    answer["e: explain"] = "Medals awarded at the Olympics, such as Bronze, Silver, and Gold, are discrete qualitative attributes arranged according to rank."

    answer["f"] = ['continuous','quantitative','interval']
    answer["f: explain"] = "Elevation above sea level is a continuous quantitative attribute, possibly falling into the interval or ratio scale if sea level is regarded as an arbitrary starting point, with meaningful ratios between elevations."
    answer["g"] = ['discrete','quantitative','ratio']
    answer["g: explain"] = "The count of patients in a hospital represents a discrete quantitative attribute, quantifiable on a ratio scale."

    answer["h"] = ['discrete','qualitative','nominal']
    answer["h: explain"] = "ISBN numbers assigned to books are qualitative attributes that are discrete, serving as unique identifiers without any inherent order."

    answer["i"] = ['discrete','qualitative','ordinal']
    answer["i: explain"] = "The capacity to transmit light, classified as opaque, translucent, or transparent, is a qualitative attribute with discrete categories arranged based on increasing light transmission."
    answer["j"] = ['discrete','qualitative','ordinal']
    answer["j: explain"] = "Within the military, ranks represent a discrete qualitative attribute organized in a hierarchical order, ranging from lower to higher positions."
    answer["k"] = ['continuous','quantitative','ratio']
    answer["k: explain"] = "The distance from the center of campus is a continuous quantitative attribute, possibly falling into the interval or ratio scale if the center is considered an arbitrary reference point, and meaningful ratios can be derived between distances."

    answer["l"] = ['discrete','quantitative','ratio']
    answer["l: explain"] = "The density of a substance, measured in grams per cubic centimeter, is a continuous quantitative attribute that can be assessed on a ratio scale."
    answer["m"] = ['discrete','qualitative','nominal']
    answer["m: explain"] = "The coat check number is a qualitative attribute that is discrete, representing distinct categories without any inherent order."
    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Model 2 is anticipated to exhibit enhanced performance on unseen instances due to its consistent accuracies across both datasets, implying superior generalization in contrast to Model 1. In Model 1, the decline in accuracy from Dataset A to B indicates potential overfitting."
    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "Although there is a minor decrease in accuracy, Model 2 is still favored because of its superior generalization, which reduces the risk of overfitting. This stands in contrast to Model 1, which experienced a notable decline in accuracy specifically on Dataset B."
    explain["c similarity"] = "Regularization Approach to Avoid Overfitting"
    explain["c similarity explain"] = "Both methods apply penalties to mitigate overfitting of the training data. MDL penalizes the complexity of the model by considering encoding costs, while Pessimistic error accounts for complexity by adjusting errors."
    explain["c difference"] = "Model Optimization Criterion"
    explain["c difference explain"] = "MDL seeks to reduce description length, preferring simpler models that encode data more succinctly. On the other hand, Pessimistic error aims to minimize the penalized error rate directly by adjusting errors higher for more complex models."



# ----------------------------------------------------------------------
    
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = "x <= 0.5"
    answer["a, level 2, right"] ="A"
    answer["a, level 2, left"] = "y <= 0.4"
    answer["a, level 3, left"] = "A"
    answer["a, level 3, right"] = "x <= 0.2"

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.58

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("x <= 0.5")

    A = tree.insert_right("A")
    B = tree.insert_left("y <= 0.4")
    B.insert_left("A")
    B.insert_right("x <= 0.2")
    answer["c, tree"] = tree
    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

  
    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.531

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.231
    answer["e, gain ratio, Handedness"] = 0.531

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer

z

# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

