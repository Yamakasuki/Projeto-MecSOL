from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from truss import Truss  


class GraphWidget(QWidget):
    def __init__(self, truss: Truss):
        super().__init__()
        self.truss = truss
        # list to store the plotted points
        self.points = []
        self.counter = 0
       
        #List to store the plotted lines 
        self.segments = None
        self.Member_counter = 0

        #List to store the plotted forces
        self.forces = None 
        self.Forces_counter = 0 

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Create a matplotlib figure
        fig = Figure()
        self.canvas = FigureCanvas(fig)
        layout.addWidget(self.canvas)

        # Create an axis for the figure
        self.ax = fig.add_subplot(111, projection='3d')

        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title('Treliça')

        # Create a QTimer to periodically update the plot
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # Update every 1 second

        # Update the canvas
        self.canvas.draw()

    def update_plot(self):
        #se tiver que plotar um ponto novo
        if self.truss.getFlag() == True:
            self.plot_data()
            self.truss.setFlag(False)

        #se tiver que plotar uma conexão nova    
        if self.truss.getFlagM() == True:
            #self.plot_segment()
            self.plot_data()
            self.truss.setFlagM(False)
        
        #se tiver que plotar uma força 
        if self.truss.getForceFlag() == True:
            self.plot_data()
            self.truss.setForcesFlag(False)

    def plot_data(self):
        #   Pontos 
        if self.truss.getFlag() == True:
            # Get the coordinates
            self.x = float(self.truss.xp(self.counter))
            self.y = float(self.truss.yp(self.counter))
            self.z = float(self.truss.zp(self.counter))

            # Point name
            id = self.truss.IDp(self.counter)
            self.counter += 1
            self.points.append((self.x, self.y, self.z, id))

        # Conexões
        elif self.truss.getFlagM() == True:
            if self.Member_counter == 0:
                self.segments = []
            #gets the name of the line segment
            self.segment_name = self.truss.getMembersid(self.Member_counter)
            #Gets the coordinates of the starting and ending points
            self.start_x, self.end_x = self.truss.getMembersX(self.Member_counter)
            self.start_y,self.end_y = self.truss.getMembersY(self.Member_counter)
            self.start_z,self.end_z = self.truss.getMembersZ(self.Member_counter)
            
            self.segments.append(((self.start_x, self.start_y, self.start_z), (self.end_x, self.end_y, self.end_z), self.segment_name))
            self.Member_counter +=1
        # Forças 
        elif self.truss.getForceFlag() == True:    
            if self.Forces_counter == 0:
                    self.forces = []
            #Primeiro pegar as coordenadas do ponto pelo id
            print("chorei")
            print(self.Forces_counter)
            #self.force_point = self.truss.getForcesID(self.Forces_counter)
            self.f_x,self.f_y, self.f_z = self.truss.get_coordinates(self.Forces_counter)

            # Pegar os valores das magnitudes 
            self.x_magnitude = float(self.truss.fx(self.Forces_counter))
            self.y_magnitude = float(self.truss.fy(self.Forces_counter))
            self.z_magnitude = float(self.truss.fz(self.Forces_counter))

            # Calcula a resultante 
            self.resultant_magnitude = np.sqrt(self.x_magnitude**2 +self.y_magnitude**2 +self.z_magnitude**2)
            #Coloca na array com as forças 
            self.vector = np.array([self.f_x,self.f_y,self.f_z])
            self.scaled_vector = np.array([self.x_magnitude, self.y_magnitude, self.z_magnitude])

            self.forces.append(self.scaled_vector)

            #incrementar o counter 
            self.Forces_counter +=1

        # Clear the axis before plotting new points
        self.ax.clear()
        # Set scatter point size and disable the wireframe
        self.ax.scatter(self.x, self.y, self.z, color='red', s=50, edgecolors='none')

        # Plot the points and annotations
        for point in self.points:
            x, y, z, id = point
            self.ax.scatter(x, y, z, color='red', s=50, edgecolors='none')
            self.ax.text(x, y, z, id, color='black')
        if(self.segments != None):
            for line in self.segments:
                start, end, name = line
                self.ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], label=name)
                
        if(self.forces != None):
            for vector in self.forces:
                self.ax.quiver(self.truss.xp(self.Forces_counter-1),self.truss.yp(self.Forces_counter-1),self.truss.zp(self.Forces_counter-1), vector[0], vector[1], vector[2], color='r', arrow_length_ratio=0.1)

                
        # Set labels and title
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title('Treliça')

        # Hide the wireframe
        self.ax.grid(False)

        # Adjust the scale of the graph
        max_value = max(max(max(x, y), z) for x, y, z, _ in self.points)
        self.ax.set_xlim(0, max_value)
        self.ax.set_ylim(0, max_value)
        self.ax.set_zlim(0, max_value)

        # Update the plot
        self.canvas.draw()

    def closeEvent(self, event):
        # Stop the QTimer when the widget is closed
        self.timer.stop()
        event.accept()
