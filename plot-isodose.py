nY, nX = dose_grid.shape  # Dimensions de la grille de dose
X = np.array(range(nX))  # Coordonnées X
Y = np.array(range(nY))  # Coordonnées Y

#Définir la police à utiliser
plt.rcParams['font.family'] = 'Arial'

# Configuration initiale de la figure
plt.figure(figsize=(8, 6))
contour_levels = [10, 20, 30, 50, 70, 95]  # Niveaux d'isodose à tracer

# Délimitez l'axe des x et y avec des intervalles
plt.xlim(-25, 25)
plt.ylim(-25, 25)

# Tracé des courbes d'isodose pour Gamma Knife
cs1 = plt.contour(X - 52, Y - 52, dose_grid_gk, levels=contour_levels, colors='gray', linestyles='--')
plt.clabel(cs1, inline=1, fontsize=10, fmt='%1.1f')

# Tracé des courbes d'isodose pour iARC
cs2 = plt.contour(X - 52, Y - 52, dose_grid, levels=contour_levels, colors='black')
plt.clabel(cs2, inline=1, fontsize=10, fmt='%1.1f')

# Ajout d'une légende 
gray_line = plt.Line2D([0], [0], color='gray', linestyle='--', lw=2, label='Gamma Knife')
black_line = plt.Line2D([0], [0], color='black', lw=2, label='iArc')
plt.legend(handles=[gray_line, black_line])



# Titre du graphique et  des axes
plt.title("Comparaison des courbes d'isodose")
plt.xlabel('X [mm]',fontsize=20)
plt.ylabel('Y [mm]',fontsize=20)

# Retirer les bordures du haut et de droite 
ax = plt.gca()  # obtenir l'objet axes actuel
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Affichage du graphique

plt.show()
