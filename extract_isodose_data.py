def extract_isodose_data(data, plane, plane_index, dose_isocentre):
     """
    Extrait les données pour tracer des courbes d'isodose dans un plan spécifié.

    Parameters:
    data (numpy.ndarray): Le tableau de données contenant les doses.
    plane (str): Le plan dans lequel extraire les données ('X', 'Y', ou 'Z').
    plane_index (int): L'indice du plan (par exemple, 52 pour le centre du mesh).
    dose_isocentre (float): La dose au centre utilisée pour normaliser les valeurs de dose.

    Returns:
    numpy.ndarray: Une grille 2D contenant les pourcentages de dose normalisés par rapport à la dose d'isocentre.
    """

     # Mapping pour déterminer les axes à utiliser selon le plan
    axis_map = {'X': 0, 'Y': 1, 'Z': 2}
    plan_coord = {'X': (1, 2), 'Y': (0, 2), 'Z': (0, 1)}

    # Filtrer les données pour ne garder que les lignes correspondant au plan spécifié
    plan_data = data[data[:, axis_map[plane]] == plane_index]

    # Déterminer la taille de la grille 2D
    grid_size = int(np.max(plan_data[:, other_axes[plane]]) + 1)
    dose_grid = np.zeros((grid_size, grid_size))

    # Remplir la grille avec les doses normalisées
    for row in plan_data:
        coord1 = int(row[plan_coord[plane][0]])
        coord2 = int(row[plan_coord[plane][1]])
        dose = row[3]
        dose_grid[coord1, coord2] = (dose / dose_isocentre) * 100
    
    return dose_grid
