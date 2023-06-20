from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from truss import Truss

class MemberWidget(QDialog):
    def
    import numpy as np

def calculate_stiffness_matrix(nodes, elements, elasticity):
    num_nodes = len(nodes)
    num_elements = len(elements)

    stiffness_matrix = np.zeros((2 * num_nodes, 2 * num_nodes))

    for element in elements:
        node_indices = element[:3]
        x_coords = nodes[node_indices, 0]
        y_coords = nodes[node_indices, 1]

        area = 0.5 * (x_coords[1] * y_coords[2] - x_coords[2] * y_coords[1] +
                      x_coords[2] * y_coords[0] - x_coords[0] * y_coords[2] +
                      x_coords[0] * y_coords[1] - x_coords[1] * y_coords[0])

        b_matrix = np.array([[y_coords[1] - y_coords[2], 0, y_coords[2] - y_coords[0], 0, y_coords[0] - y_coords[1], 0],
                             [0, x_coords[2] - x_coords[1], 0, x_coords[0] - x_coords[2], 0, x_coords[1] - x_coords[0]],
                             [x_coords[2] - x_coords[1], y_coords[1] - y_coords[2], x_coords[0] - x_coords[2], y_coords[2] - y_coords[0], x_coords[1] - x_coords[0], y_coords[0] - y_coords[1]]]) / (2 * area)

        element_stiffness = elasticity * area * np.dot(b_matrix.T, b_matrix)

        for i in range(3):
            for j in range(3):
                stiffness_matrix[2 * node_indices[i], 2 * node_indices[j]] += element_stiffness[2 * i, 2 * j]
                stiffness_matrix[2 * node_indices[i] + 1, 2 * node_indices[j]] += element_stiffness[2 * i + 1, 2 * j]
                stiffness_matrix[2 * node_indices[i], 2 * node_indices[j] + 1] += element_stiffness[2 * i, 2 * j + 1]
                stiffness_matrix[2 * node_indices[i] + 1, 2 * node_indices[j] + 1] += element_stiffness[2 * i + 1, 2 * j + 1]

    return stiffness_matrix


# Exemplo de uso
# Definindo os nós (coordenadas x, y)
nodes = np.array([[0, 0],
                  [1, 0],
                  [1, 1],
                  [0, 1]])

# Definindo os elementos (índices dos nós que formam cada elemento)
elements = np.array([[0, 1, 2],
                     [0, 2, 3]])

# Propriedades do material (elasticidade)
elasticity = 1.0

# Calculando a matriz de rigidez
stiffness_matrix = calculate_stiffness_matrix(nodes, elements, elasticity)

print("Matriz de Rigidez:")
print(stiffness_matrix)
