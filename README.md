# COP4533 - Algorithm Abstraction & Design Programming Project
Milestone 1: 
Ana - Currently Working on Algorithm 1 Problem S1 
---

## 🧩 Problem S1 – Monotonically Non-Decreasing Values

### 💡 Greedy Idea

Since the vault values always go up or stay the same (they never go down), the vaults on the right side will always be as good or better than the ones on the left.  
That means it makes the most sense to **start picking from the end**. The vaults at the far right have the highest values, and you don't lose anything by skipping the smaller ones on the left.

However, when you pick a vault, you can’t pick any other vault within `k` positions on either side. So after picking one vault, you skip `k` vaults to the left and keep repeating that until you run out of vaults.  

Basically, you're dividing the vaults into groups of size `k + 1`, and you always take the **rightmost vault** from each group because that's the one with the highest value in that group.

**The algorithm picks:**
n, n-(k+1), n-2(k+1), …
until you reach the beginning.  
It’s a simple one-pass process, which is why it runs in **Θ(n)** time.

---

### ✅ Correctness Proof

In this problem, all the vault values go up or stay the same as we move to the right, meaning every vault on the right side is at least as valuable as the ones before it. Because of that, picking vaults farther to the right will never give a smaller total value.

Each time we pick a vault, we're not allowed to pick any other vault within `k` positions on either side. This means that one vault **“uses up”** a total of `k + 1` spots (itself and its `k` neighbors). So, at most, we can pick around one vault for every `k + 1` positions.  

If we think of the vaults as being split into groups of `k + 1`, then every valid solution can take at most one vault per group. Now, because the values never decrease, the **rightmost vault** in each group will always be the most valuable one.  

The greedy algorithm takes advantage of this by starting from the end of the list and always picking that rightmost vault, then skipping `k` positions to the left and repeating.  

To see why this is always optimal, imagine there was another solution that gave a higher total value. Look at the first group (from the right) where that solution did **not** choose the rightmost value. If we move their chosen vault to the rightmost position of that group, two things happen:

1. ✅ The spacing rule is still valid because moving a vault to the right only increases the distance from previous picks.  
2. 💰 The total value doesn’t go down since the rightmost vault’s value is greater than or equal to the one it replaced.  

If we keep applying this idea to every group, we can gradually transform any other valid solution into the greedy one without lowering its total value.  

This means the greedy solution must already be optimal.  
Therefore, **Algorithm 1 always finds the best possible total value for Problem S1.**

---

### 🕒 Time Complexity
**Θ(n)** – the algorithm only passes through the vaults once.

---

### 🧠 Summary
- **Type:** Greedy algorithm  
- **Special Case:** Monotonically non-decreasing vault values  
- **Key Idea:** Always pick the rightmost available vault  
- **Why It Works:** Later vaults are never worse than earlier ones, so picking right-to-left guarantees the best result.

