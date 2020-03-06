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
    type: tuple
    value: (alive_number, dead_number)
    """
    pass


