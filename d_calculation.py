G = 79.3e9  # Shear modulus in Pascals
d = 0.01  # Wire diameter in meters
k = 20  # Spring constant in Newtons per meter
N = 20  # Number of active coils

D = ((G * d**4) / (8 * k * N))**(1/3)
print(D)
