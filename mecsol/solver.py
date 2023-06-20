import numpy as np
from truss import Truss
# Definir as coordenadas dos nós
'''
def getCoords(truss: Truss):
    x_coords = truss.getXpositions()
    y_coords = truss.getYpositions()
    elements = truss.getMembers()
    restrained_node = truss.getSupports()
    return x_coords, y_coords, elements, restrained_node
# Criar matriz de nós
x_coords, y_coords, elemets, restrained_node = getCoords(Truss)
nodes = np.array([x_coords, y_coords]).T
bagre = []
for i in range(len(elements)):
    try:
        bagre.append(elements.index(elements[0][i]))
    except:
        break
# Definir os nós conectados por cada elemento
elements = [(0, 1), (1, 2), (2, 3), (3, 0)]

# Definir as propriedades dos elementos
area = 1.0  # Área da seção transversal dos elementos
elasticity = 200e9  # Módulo de elasticidade dos elementos

# Criar matriz de propriedades dos elementos
element_properties = np.array([[area, elasticity]] * len(elements))
# 
# Imprimir as propriedades dos elementos
for i, element in enumerate(elements):
    print(f"Element {i+1}:")
    print("Nodes:", element)
    print("Area:", element_properties[i, 0])
    print("Elasticity:", element_properties[i, 1])
    print()

# Definir os nós conectados por cada elemento
elements = [(0, 1), (1, 2), (2, 3), (3, 0)]

# Definir o número de graus de liberdade por nó
dofs_per_node = 2

# Inicializar a matriz de rigidez global
num_nodes = len(nodes)
num_dofs = num_nodes * dofs_per_node
global_stiffness = np.zeros((num_dofs, num_dofs))

# Montar a matriz de rigidez global
for element in elements:
    node_i, node_j = element

    # Obter as coordenadas dos nós
    x_i, y_i = nodes[node_i]
    x_j, y_j = nodes[node_j]

    # Calcular o comprimento e o ângulo do elemento
    length = np.sqrt((x_j - x_i)**2 + (y_j - y_i)**2)
    cos_theta = (x_j - x_i) / length
    sin_theta = (y_j - y_i) / length

    # Montar a matriz de rigidez do elemento
    k_element = (area * elasticity / length) * np.array([
        [cos_theta**2, cos_theta*sin_theta, -cos_theta**2, -cos_theta*sin_theta],
        [cos_theta*sin_theta, sin_theta**2, -cos_theta*sin_theta, -sin_theta**2],
        [-cos_theta**2, -cos_theta*sin_theta, cos_theta**2, cos_theta*sin_theta],
        [-cos_theta*sin_theta, -sin_theta**2, cos_theta*sin_theta, sin_theta**2]
    ])

    # Mapear a matriz de rigidez do elemento para a matriz de rigidez global
    dofs_i = np.array([node_i*dofs_per_node, node_i*dofs_per_node+1])
    dofs_j = np.array([node_j*dofs_per_node, node_j*dofs_per_node+1])

    global_stiffness[np.ix_(dofs_i, dofs_i)] += k_element[:2, :2]
    global_stiffness[np.ix_(dofs_i, dofs_j)] += k_element[:2, 2:]
    global_stiffness[np.ix_(dofs_j, dofs_i)] += k_element[2:, :2]
    global_stiffness[np.ix_(dofs_j, dofs_j)] += k_element[2:, 2:]

# Aplicar as condições de contorno à matriz de rigidez global
for restrained_node in restrained_nodes:
    dof = restrained_node * dofs_per_node  # Grau de liberdade horizontal
    global_stiffness[dof, :] = 0
    global_stiffness[:, dof] = 0
    global_stiffness[dof, dof] = 1  # Atribuir 1 na diagonal principal

# Imprimir a matriz de rigidez global após aplicar as condições de contorno
print("Matriz de Rigidez Global com Condições de Contorno:")
print(global_stiffness)


def is_stable(global_stiffness):
    
    Recebe uma matriz de rigidez e retorna 
    True se a treliça for estável
    False se a treliça for instável
    
    a = np.all(np.linalg.eigvals(global_stiffness) > 0)
    if a:
        return True
    else:
        return False
    
def verificar_estado_membros(element_forces):
    # Lista para armazenar os estados dos membros
    estados_membros = []

    for i, force in enumerate(element_forces):
        area = element_areas[i]

        if force > 0:
            estado = 'Tração'
        elif force < 0:
            estado = 'Compressão'
        else:
            estado = 'Sem carga'

        estados_membros.append((i+1, estado, abs(force)))

    return estados_membros

# Exemplo de forças nos elementos e áreas correspondentes
element_forces = [10.0, -15.0, 20.0, -10.0]

# Verificar o estado dos membros
membros = verificar_estado_membros(element_forces, element_areas)

# Imprimir os resultados
print("Membros da treliça:")
print("Membro\tEstado\t\tForça\t\tÁrea")
for membro in membros:
    membro_id, estado, forca, area = membro
    print(f"{membro_id}\t{estado}\t{forca}\t\t{area}")
'''
