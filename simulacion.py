import random
import matplotlib.pyplot as plt

def simular_y_graficar_monty_hall(num_partidas=20000):
    exitos_quedarse = 0
    exitos_cambiar = 0
    
    # Listas para guardar la evolución del porcentaje de victorias
    historial_quedarse = []
    historial_cambiar = []
    
    for partida in range(1, num_partidas + 1):
        puerta_premio = random.randint(0, 2)
        eleccion_jugador = random.randint(0, 2)
        
        # Si la elección inicial coincide con el premio, gana quedándose
        if eleccion_jugador == puerta_premio:
            exitos_quedarse += 1
        else:
            # Si no coincide, la puerta restante tras abrir el presentador tendrá el premio
            exitos_cambiar += 1
            
        # Calcular porcentajes acumulados hasta esta partida
        historial_quedarse.append((exitos_quedarse / partida) * 100)
        historial_cambiar.append((exitos_cambiar / partida) * 100)

    # Configuración estética del gráfico para LinkedIn
    plt.figure(figsize=(10, 5), dpi=150)
    plt.plot(historial_cambiar, label="Estrategia: Cambiar de Puerta", color="#2ca02c", linewidth=2)
    plt.plot(historial_quedarse, label="Estrategia: Quedarse", color="#d62728", linewidth=2)
    
    # Líneas de convergencia teórica
    plt.axhline(y=66.66, color="#2ca02c", linestyle="--", alpha=0.6)
    plt.axhline(y=33.33, color="#d62728", linestyle="--", alpha=0.6)
    
    # Etiquetas y diseño limpio
    plt.title("El dilema de Monty Hall: Simulación de Convergencia Estadística", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Número de partidas simuladas", fontsize=11)
    plt.ylabel("Porcentaje de victorias (%)", fontsize=11)
    plt.xlim(0, num_partidas)
    plt.ylim(0, 100)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="upper right", fontsize=11, frameon=True)
    
    # Mostrar resultados en consola y guardar imagen limpia
    print(f"Resultado final tras {num_partidas} iteraciones:")
    print(f"  Cambiar: {historial_cambiar[-1]:.2f}% | Quedarse: {historial_quedarse[-1]:.2f}%")
    
    plt.tight_layout()
    plt.savefig("monty_hall_simulacion.png")
    plt.show()

if __name__ == "__main__":
    # 20,000 iteraciones son suficientes para mostrar una convergencia visual limpia
    simular_y_graficar_monty_hall(20000)
