import random, time, numpy as np, matplotlib.pyplot as plt
from program3 import program3
from program4A import program4A
from program4B import program4B
from program5 import program5

def avg_runtime(func, n_values, k, repeats=5):
    results = []
    for n in n_values:
        vals = [random.randint(1, 1000) for _ in range(n)]
        times = []
        for _ in range(repeats):
            start = time.perf_counter()
            func(n, k, vals)
            times.append(time.perf_counter() - start)
        results.append(sum(times)/repeats)
    return results

def run_experiment():
    k = 2
    print("\nRunning Plot 7 (Safe Origin Alignment)…\n")

    # realistic per-program ranges
    n3  = [10, 12, 14, 16, 18, 22]
    n4  = [10, 22, 60, 100, 150, 200, 300, 400]
    n5  = [10, 22, 60, 100, 150, 200, 300, 400, 500, 1000, 2000, 4000, 8000, 16000]

    t3  = avg_runtime(program3,  n3, k)
    t4A = avg_runtime(program4A, n4, k)
    t4B = avg_runtime(program4B, n4, k)
    t5  = avg_runtime(program5,  n5, k)

    # Instead of (0,0), add small anchor values so it looks like origin in log scale
    epsilon_n = 1
    epsilon_t = 1e-6

    n3,  t3  = [epsilon_n] + n3,  [epsilon_t] + t3
    n4A, t4A = [epsilon_n] + n4,  [epsilon_t] + t4A
    n4B, t4B = [epsilon_n] + n4,  [epsilon_t] + t4B
    n5,  t5  = [epsilon_n] + n5,  [epsilon_t] + t5

    plt.figure(figsize=(9,6))
    plt.xscale("log")
    plt.yscale("log")

    plt.plot(n3,  t3,  "o-", lw=2, color="#1f77b4", label="Program 3 (Θ(2ⁿ))")
    plt.plot(n4A, t4A, "o-", lw=2, color="#ff7f0e", label="Program 4A (Θ(n²), top-down)")
    plt.plot(n4B, t4B, "o-", lw=2, color="#2ca02c", label="Program 4B (Θ(n²), bottom-up)")
    plt.plot(n5,  t5,  "o-", lw=2, color="#d62728", label="Program 5 (Θ(n))")

    plt.title("Plot 7 – Runtime Comparison of Programs 3 to 5 (Aligned at Origin)")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Average Runtime (seconds)")
    plt.grid(True, which="both", linestyle="--", alpha=0.6)
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.savefig("Plot7_origin_aligned_fixed.png", dpi=400)
    plt.show()

    print("\nSaved Plot7_origin_aligned_fixed.png")

if __name__ == "__main__":
    run_experiment()

