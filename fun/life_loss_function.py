def life_loss(stress, progress, snacks):
    return stress - (progress * 2) - snacks

loss = life_loss(stress=8, progress=3, snacks=2)

print(f"Life Loss Value: {loss}")
print("Conclusion: Increase snacks or progress. Preferably both.")
