import time
from logging_setup import setup_logger

logger = setup_logger()

def calculate_fare(seconds_stopped, seconds_moving):
    """
    función para calcular la tarifa total en euros
    stopped:0.02€/s moving:0.05€/s
    """
    fare = seconds_stopped * 0.02 + seconds_moving * 0.05
    print(f"Este es el total: {fare}€")
    
    """
    log para registrar la tarifa calculada
    """
    logger.info(f"fare clculated: stopped={seconds_stopped:.1f}s, moving={seconds_moving:.1f}s, total={fare:.2f}€")
    
    return fare


def taximeter():
    print("WELCOME TO THE TAXIMETER")
    print("Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n")

    trip_activate = False
    stopped_time = 0
    moving_time = 0
    state = None
    state_start_time = 0

    while True:
        command = input("> ").strip().lower()

        
        if command == "start":
            if trip_activate:
                print("Error: a trip is already in progress.")
                
                #log para cuando el usuario intenta iniciar un viaje  cuando ya hay un viaje en curso
                logger.warning("Start command received but trip already active.")
                
                continue

            trip_activate = True
            stopped_time = 0
            moving_time = 0
            state = "stopped"
            state_start_time = time.time()
            print("Trip started. Initial state: 'stopped'")
            
            #log del inicio del trayecto
            logger.info("trip started. State: stopped")

        
        elif command in ("stop", "move"):
            if not trip_activate:
                print("Error: No active trip. Please start first.")
                
                #log de advertencia para cuando el usuario  ingresa un comando invalido si no hay un viaje
                logger.warning(f"Command '{command}'received but trip nop active.")
               
                continue

            duration = time.time() - state_start_time

            if state == "stopped":
                stopped_time += duration
            else:
                moving_time += duration

            state = "stopped" if command == "stop" else "moving"
            state_start_time = time.time()
            print(f"State changed to '{state}'.")
            
            #logs de cambio de estado.
            logger.info(f"State changed to: {state}.")

      
        elif command == "finish":
            if not trip_activate:
                print("Error: No active trip to finish.")
                
                #log de finish invalido, ej: si no hay viaje
                
                logger.warning("finish command received but no active trip.")
                
                continue

            duration = time.time() - state_start_time

            if state == "stopped":
                stopped_time += duration
            else:
                moving_time += duration

            print("\n--- Trip Summary ---")
            print(f"Stopped time: {stopped_time:.1f} seconds")
            print(f"Moving time: {moving_time:.1f} seconds")

            total_fare = calculate_fare(stopped_time, moving_time)
            print(f"Total fare: €{total_fare:.2f}")
            print("---------------------\n")
            
            # log fin del trayecto
            logger.info(f"Trip finished. Stopped={stopped_time:.1f}s, Moving={moving_time:.1f}s, fare={total_fare:.2f}€")

            trip_activate = False
            state = None

       
        elif command == "exit":
            print("Exiting the program, goodbye!")
            
            #log de salida del programa 
            logger.info("Program exited by user.")
            
            break

        
        else:
            print("Unknown command. Use: 'start', 'stop', 'move', 'finish', or 'exit'")
            
            #log de comando invalido
            
            logger.warning(f"Invalid command received: {command}")


if __name__ == "__main__":
    taximeter()
