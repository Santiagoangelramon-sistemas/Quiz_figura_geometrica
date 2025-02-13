def es_triangulo(a, b, c):
  """
  Verifica si tres longitudes dadas pueden formar un triángulo.

  Args:
    a: La longitud del primer lado.
    b: La longitud del segundo lado.
    c: La longitud del tercer lado.

  Returns:
    True si las longitudes pueden formar un triángulo, False en caso contrario.
  """
  if a + b > c and a + c > b and b + c > a:
    return True
  else:
    return False

# Ejemplos de uso
lado1 = 5
lado2 = 3
lado3 = 4

if es_triangulo(lado1, lado2, lado3):
  print("¡Sí, es un triángulo!")
else:
  print("¡No, no es un triángulo!")

lado1 = 1
lado2 = 2
lado3 = 5

if es_triangulo(lado1, lado2, lado3):
  print("¡Sí, es un triángulo!")
else:
  print("¡No, no es un triángulo!")