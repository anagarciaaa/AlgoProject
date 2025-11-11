import time
import subprocess
import matplotlib.pyplot as plt

sizes = [10, 12, 14, 16, 18]
runtimes = []

for n in sizes:
    print(f"Running Program 3 for n={n} ...")
    start = time.time()

    # Run your program3.py on the generated input
    subprocess.run(
        ["python", "program3.py"],
        input=open(f"input_{n}.txt").read(),
        text=True,
        stdout=subprocess.DEVNULL
    )

    elapsed = time.time() - start
    runtimes.append(elapsed)

# Save results
plt.plot(sizes, runtimes, marker="o", color="red", label="Program 3 (Θ(2ⁿ))")
plt.xlabel("Input size n")
plt.ylabel("Runtime (seconds)")
plt.title("Plot 3 – Runtime of Program 3 vs Input Size")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plot3_program3_runtime.png", dpi=300)
plt.show()
