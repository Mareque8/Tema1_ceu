def ordenar(c):
  return c["prioridad"]
cola = [
  {"tarea4": "estudiar", "prioridad":"4" },
  {"tarea3": "comer", "prioridad":"3"},
  {"tarea2": "dormir", "prioridad":"2"},
  {"tarea1": "beber", "prioridad":"1"},
]

cola.sort(key=ordenar)
print(cola[0]["tarea1"],cola[1]["tarea2"],cola[2]["tarea3"],cola[3]["tarea4"])  
