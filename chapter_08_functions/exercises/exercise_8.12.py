def sandwich_order(*items):
    print("\nSandwich items:")
    for item in items:
        print("  - " + item)

sandwich_order('cheese', 'tomatoes')
sandwich_order('cheese', 'ham', 'mushrooms', 'tomatoes')
sandwich_order('cheese')