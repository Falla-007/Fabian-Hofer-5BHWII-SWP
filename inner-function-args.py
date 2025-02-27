def demo_args(*args):
    print("\n*args Beispiel:")
    for i, arg in enumerate(args):
        print(f"Argument {i+1}: {arg}")

def demo_kwargs(**kwargs):
    print("\n**kwargs Beispiel:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def args_kwargs_mixed(a, b, *args, key1="default1", key2="default2", **kwargs):
    print("\nGemischte *args und **kwargs Beispiel:")
    print(f"Erste zwei Argumente: a={a}, b={b}")
    print("Zusätzliche args:", args)
    print(f"Keyword-Argumente mit Standardwerten: key1={key1}, key2={key2}")
    print("Weitere kwargs:", kwargs)

def nested_functions_demo(x):
    print("\nInnere Methoden Beispiel:")
    
    def inner_function(y):
        return y * 2
    
    def another_inner_function(y):
        return y + 10
    
    result1 = inner_function(x)
    result2 = another_inner_function(x)
    print(f"inner_function verdoppelt: {result1}")
    print(f"another_inner_function addiert 10: {result2}")

def callback_function_demo(x, func):
    print("\nCallback-Funktion Beispiel:")
    print(f"Wert vor Callback: {x}")
    print(f"Wert nach Callback: {func(x)}")

def main():
    demo_args(1, 2, 3, "Hallo", 5.5)
    
    demo_kwargs(name="Hasan", alter=30, beruf="Ingenieur")
    
    args_kwargs_mixed(10, 20, 30, 40, key1="Geändert", extra1="Daten", extra2=99)
    
    nested_functions_demo(5)
    
    callback_function_demo(7, lambda x: x**2)
    
    def custom_multiplier(value):
        return value * 3
    
    callback_function_demo(4, custom_multiplier)

if __name__ == "__main__":
    main()
