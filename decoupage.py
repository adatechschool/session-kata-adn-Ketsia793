import numpy as np
#lecture du fichier.txt
with open("adn.txt","r",encoding="utf8") as file :
    print(file.readlines())
    array = file.readlines()


#Définir une fonction pour diviser une liste en morceaux d'une taille spécifiée
def split_list(array, chunk_size):

    chunks = []  # Initialiser une liste vide pour stocker des morceaux
    
    # Parcourez la liste avec une étape de chunk_size
    for i in range(0, len(array), chunk_size):
        # Découpez la liste de l'index 'i' à 'i + chunk_size' et ajoutez-la aux morceaux
        chunks.append(array[i:i + chunk_size])
    
    return chunks  # Renvoie la liste des morceaux



my_list = [array, 3]

# Split the list into chunks of size 4 Divisez la liste en morceaux de taille 4 à l'aide de la fonction split_into_chunksusing the split_into_chunks function
chunks = split_list(array, 3)

# Imprimer la liste de morceaux résultante
print(chunks)
