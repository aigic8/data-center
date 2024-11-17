########### SOURCE: https://doi.org/10.1016/j.enbuild.2014.10.058


def main():
    for u_cpu in range(0, 110, 10):
        print(f"u_cpu = {u_cpu}, heat = {calc_heat(u_cpu, 70)}")


# PIT = 1.566 × 10^−5 + 42.29u_cpu + 0.379T_die + 0.03002T^2_die
def calc_heat(u_cpu: float, t_die: float):
    return 1.566e-5 * 42.29 * u_cpu * 0.379 * t_die * 0.03002 * t_die**2


if __name__ == "__main__":
    main()
