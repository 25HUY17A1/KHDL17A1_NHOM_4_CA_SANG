import math
def piecewise_probability_distribution(x):
    if x > 0:
        return lambda x: lambda l: l * math.exp(-l * x)
    else:
        return lambda x: 0

def calculate_lambda():
    xbreak = 1
    f_xbreak = piecewise_probability_distribution(xbreak)(xbreak)
    return 1 / f_xbreak(1)

def calculate_probability(x):
    l = calculate_lambda()
    f_x = piecewise_probability_distribution(x)(x)
    p_0_to_x = 0
    p_0_to_theta = 0
    delta_x = 0.001  # Small interval for numerical integration
    xi = 0
    while xi < x:
        p_0_to_x += f_x(xi) * delta_x
        xi += delta_x
    xi = 0
    while xi < xbreak:
        p_0_to_theta += f_x(xi) * delta_x
        xi += delta_x
    return p_0_to_x, p_0_to_theta

x = 1.5
xbreak = 1
p_0_to_x, p_0_to_theta = calculate_probability(x)

print(f"Hệ số λ: {calculate_lambda():.6f}")
print(f"P(0 < X ≤ {x}): {p_0_to_x:.6f}")
print(f"P(0 < X ≤ {xbreak}): {p_0_to_theta:.6f}")
