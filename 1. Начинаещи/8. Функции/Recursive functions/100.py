def power(base, stepen):
    if stepen == 0:
        result = 1
    else:
        result = base * power(base, stepen - 1)
    
    return result

# Main
# Пресмятане на число на някаква степен
# 
# Base- числото
# 
# Stepen- степенния показател
print("Въведете основа(число): ")
base = int(input())
print("Въведете степен: ")
stepen = int(input())
print("Резултатът е: " + str(power(base, stepen)))
