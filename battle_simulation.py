import asyncio
import httpx
import time

async def wizard_attack(client, wizard_name, spell):
    print(f"{wizard_name} comienza a conjurar {spell}...")
    start_time = time.time()
    
    try:
        response = await client.post(
            "http://127.0.0.1:8000/cast",
            params={"spell_name": spell, "is_event": "false"},
            headers={"x-user-id": wizard_name} 
        )
        elapsed = time.time() - start_time
        print(f"{wizard_name} terminó en {elapsed:.2f}s. Resultado: {response.json()['result']}")
    except Exception as e:
        print(f"{wizard_name} falló: {e}")

async def start_battle():
    # Simulamos 3 magos atacando AL MISMO TIEMPO
    async with httpx.AsyncClient(timeout=10.0) as client:
        print("--- INICIO DE LA BATALLA ---")
        start_battle_time = time.time()

        await asyncio.gather(
            wizard_attack(client, "harry", "Flipendo"),
            wizard_attack(client, "elaina", "Fireball"),
            wizard_attack(client, "gandalf", "Protego"),
            wizard_attack(client, "shacklebolt", "Confringo")
        )
        
        total_time = time.time() - start_battle_time
        print(f"--- FIN DE LA BATALLA ---")
        print(f"Tiempo total transcurrido: {total_time:.2f}s")

if __name__ == "__main__":
    asyncio.run(start_battle())