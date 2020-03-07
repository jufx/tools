from numpy import array as npar, asmatrix

TRY=[
  [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
  [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
  [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
  [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
  [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
  [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
  [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
  [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
  [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1]
]


TRY=[[11, 12],
     [21, 22]]

ACCEPTED_VALUES=[0, 1]

"""
R -1 Une cellule peut avoir un état vivante ou morte. -> type(cell) is Bool 
R -2 Chaque cellule a plusieurs voisines, en horizontal, vertical et diagonale. => 
#todo check_neighbors(i,j) => self.current_neighbors = (alive_number, dead_number)
R -3 Tous les changements de cellules doivent se faire de façon simultané. => buffer rafraîchi à chaque itération

PRIORITES: dérouler de R1 à R4
R1 -    Chaque cellule vivante qui a moins de 2 voisins vivants meurt, 
R2 -    Chaque cellule vivante qui a 2 ou 3 voisins vivants continue de vivre,
R3 -    Chaque cellule avec plus de 3 voisins vivants meurt,
R4 -    Chaque cellule morte avec exactement 3 voisins vivants devient vivante.


stratégie de routine:
0-init : 
0.0-basic checks: 
    0.0.1 - si tableau avec longueur|largeur = 0 -> raise IndexError("please provide a valid tab")
            ou si largeur variable -> raise IndexError("please provide a tab as list of same lenghts lists")
            sinon :
            - self.X_SIZE, self.Y_SIZE = len(tab[0]), len(tab)
            - convertir le tableau en array-> np.array
    0.0.2 - si NaN dans le tab => put rule, default is NaN_conversion_value = 0




"""
def routine():




def from_array_to_numpy_array(tab):
    """
    :param tab: list
    :return: numpy array
    """
    pass

def set_death_order((i,j)):
    """
    cell(i, j) will be set to 0 on next iteration
    :return: None
    """
    pass

def check_neighbors((i,j)):
    """
     :param:
     (i, j)
     type: tuple
     value: coordinates
    :return:
    type: tuplefrom tools.aggregator import Aggregator
from re import findall

PATHS = ["/home/meb/PycharmProjects/", "/home/meb/Bureau/"]
EXT = ['**/*.py', '**/*.ipynb']
RESULTS_URLS=[]



# gather files
for PATH in PATHS:
    for extension in EXT:
        A = Aggregator(path_to_files=PATH, pattern=extension)
        for result in A.matching_list:
            RESULTS_URLS.append(result)
print(len(RESULTS_URLS))

JUICY_LINES = []
RE_PATTERNS = ['from', 'import']
files_done = 0

# gather lines
for file_url in RESULTS_URLS:
    with open(file_url, mode='r') as py_script:
        for lines in py_script:
            for pattern in RE_PATTERNS:
                brute=findall(pattern=pattern,string=lines)
                if brute:
                    brute=brute[0].strip('"').replace('\n', '').replace('"', '').replace(',', '')
                    if pattern == brute[0:len(pattern)] : # and lines.replace('\n', '').replace('"', '').replace(',', '').replace('.', ' ').replace(RE_PATTERNS[0], '').replace(RE_PATTERNS[1], '').replace ('  ', ' ') not in JUICY_LINES
                        JUICY_LINES.append(lines.replace('\n', '').replace('"', '').replace(',', '').replace('.', ' ').replace(RE_PATTERNS[0], '').replace(RE_PATTERNS[1], '').replace ('  ', ' '))
        files_done += 1
        print(100 * files_done / len(RESULTS_URLS))

for line in JUICY_LINES:
    print(line.replace('\n', ''))
    value: (alive_number, dead_number)
    """
    pass

  
  
  
  
import sys, time, numpy
from random import randrange

TRY=numpy.array(TRY)
MAXx=len(TRY)
MAXy=len(TRY[0])
for i in range(5):
    stri = ""
    for j in range(MAXx):
        for k in range(MAXy):
            stri += str(TRY[k][j])+ " "
        stri+="\n"
            #sys.stdout.write("\n")
    sys.stdout.write("\r%s\n\r" % stri)
    #assert MAXx ==MAXy
    TRY[randrange(0,MAXx), randrange(0,MAXy)] +=1
    time.sleep(1)
    #sys.stdout.flush()
sys.stdout.write("\n")



#---------------SKINNER
import numpy
import sys


class Printer:
    def __init__(self, obj, iteration):
        TRY = numpy.array(obj)
        MAXx = len(TRY)
        MAXy = len(TRY[0])
        for i in range(iteration):
            stri = ""
            for j in range(MAXx):
                for k in range(MAXy):
                    stri += str(TRY[k][j]) + " "
                stri += "\n"
                # sys.stdout.write("\n")
            sys.stdout.write("\r%s\n\r" % stri)


class Skinner:
