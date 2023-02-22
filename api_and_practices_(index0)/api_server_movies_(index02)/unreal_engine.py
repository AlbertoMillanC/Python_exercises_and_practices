# Importar el módulo de Unreal Engine
import UnrealEngine as UE

# Obtener una instancia del mundo actual
world = UE.World.GetWorld()

# Buscar un actor en el mundo
actor = world.FindActorByName("MyActor")

# Si se encuentra el actor, cambiar su posición en el mundo
if actor:
    actor.SetActorLocation(UE.FVector(100, 200, 300))
