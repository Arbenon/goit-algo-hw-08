import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    
    total_cost = 0

    while len(cables) > 1:
        # Витягнути два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Витрати на з'єднання
        cost = first + second
        
        # Всі витрат
        total_cost += cost
        
        # Помістити новий кабель назад в купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [8, 4, 6, 12, 123, 11, 2]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))
