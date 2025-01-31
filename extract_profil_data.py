def extract_profil_data(filename, axis, center_index):
   """
   Extrait et organise les données de profils de dose à partir d'un fichier spécifié.
    
    Parameters:
    filename (str): Le chemin du fichier contenant les données de dose.
    axis (str): L'axe spécifique à filtrer ('iX', 'iY', 'iZ').
    center_index (int): L'indice du centre des coordonnées pour l'axe filtré.
    
    Returns:
    tuple: Liste contenant les valeurs des axes, dose total, La somme des carrés de doses et le nombre de hits.
    
    
    """
    # Initialisation des listes pour stocker les valeurs extraites
    axis_values = []
    total_values = []
    total_values2 = []
    hits = []
    
    # Ouverture du fichier pour lecture
    with open(filename, 'r') as file:
        # Lecture de chaque ligne dans le fichier
        for line in file:
            # Ignorer les lignes de commentaire et d'en-tête
            if not line.startswith("#"):
                values = line.strip().split(',')
              # Extraire les valeurs nécessaires
                iX = int(values[0])
                iY = int(values[1])
                iZ = int(values[2])
                total_value = float(values[3])
                total_value2 = float(values[4])
                hit = int(values[5])
                
               # Vérifier si les coordonnées correspondent à l'axe spécifié
                if axis == "iX" and iY == center_index and iZ == center_index:
                    axis_values.append(iX)
                    total_values.append(total_value)
                    total_values2.append(total_value2)
                    hits.append(hit)
                elif axis == "iY" and iX == center_index and iZ == center_index:
                    axis_values.append(iY)
                    total_values.append(total_value)
                    total_values2.append(total_value2)
                    hits.append(hit)
                elif axis == "iZ" and iX == center_index and iY == center_index:
                    axis_values.append(iZ)
                    total_values.append(total_value)
                    total_values2.append(total_value2)
                    hits.append(hit)
                    
    return axis_values, total_values, total_values2, hits
