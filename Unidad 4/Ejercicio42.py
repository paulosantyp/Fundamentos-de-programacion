# -*- coding: utf-8 -*-
"""

Requisitos:
"""

#Comentar cuales son las librerias que se importan y para que funciona cada una 
#

import sys                          #Permite que python interprete variables y funciones del sistema
import platform                     #Sirve para identificar el sistema operativos en el que se ejecuta el programa
import subprocess                   #Permite ejecutar comandos del sistema como (.ping)
#  ----PyQt5-----
from PyQt5.QtCore import Qt         #Contiene funciones y constantes relacionadas al uso de la interfaz grafica
from PyQt5.QtWidgets import (       #Proporciona los elementos necesarios para construir la interfaz grafica
    QApplication,                   #Clase principal que controla la aplicacion y el bucle de eventos
    QWidget,                        #Clase principal para crear ventanas y componentes principales
    QLabel,                         #Widget que muestra un texto
    QLineEdit,                      #Crea un campo donde el usuario puede escribir
    QPushButton,                    #Crea un boton con el que el usuario puede presionar
    QTextEdit,                      #Area de texto grande donde se muestran resultados
    QVBoxLayout,                    #Organiza los widgets verticalmente
    QHBoxLayout,                    #Organiza los widgets horizontalmente
    QMessageBox,                    #Permite mostrar mensajes emergentes (alertas, errores, advertencias)
)


class PingApp(QWidget):
    """Ventana principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ping – PyQt5")
        self.resize(400, 300)

        # ---------- Widgets ----------
        # Entrada de host / IP
        self.host_input = QLineEdit(self)
        self.host_input.setPlaceholderText("Ejemplo: google.com o 8.8.8.8")

        # Botón de ejecutar ping
        self.ping_btn = QPushButton("Enviar ping", self)
        self.ping_btn.clicked.connect(self.ejecutar_ping)

        # Área de texto donde se mostrará la salida
        self.resultado = QTextEdit(self)
        self.resultado.setReadOnly(True)

        # ---------- Layout ----------
        entrada_layout = QHBoxLayout()
        entrada_layout.addWidget(QLabel("Destino:", self))
        entrada_layout.addWidget(self.host_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(entrada_layout)
        main_layout.addWidget(self.ping_btn)
        main_layout.addWidget(QLabel("Resultado:", self))
        main_layout.addWidget(self.resultado)

        self.setLayout(main_layout)

    # -----------------------------------------------------------------
    def ejecutar_ping(self):
        """Construye y ejecuta el comando ping, mostrando la salida."""
        host = self.host_input.text().strip()
        if not host:
            QMessageBox.warning(self, "Entrada vacía", "Introduce una dirección IP o nombre de host.")
            return

        # Determinar parámetros según SO
        sistema = platform.system().lower()
        if "windows" in sistema:
            cmd = ["ping", "-n", "4", host]         
        else:  # Linux, macOS, etc.
            cmd = ["ping", "-c", "4", host]       

        try:
            # Ejecutamos el comando y capturamos stdout + stderr
            proceso = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=10,            
            )
            salida = proceso.stdout if proceso.returncode == 0 else proceso.stderr
            self.resultado.setPlainText(salida)
        except subprocess.TimeoutExpired:
            self.resultado.setPlainText("Error: tiempo de espera agotado.")
        except Exception as e:
            self.resultado.setPlainText(f"Ocurrió un error inesperado:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PingApp()
    ventana.show()
    sys.exit(app.exec_())