import sys

# 🎯 ONE LINE TO RULE THEM ALL
input = sys.stdin.readline

def main():
    # 🎯 FOR SINGLE INTEGER:
    n = int(input())
    
    # 🎯 FOR SPACE-SEPARATED INTEGERS (MOST COMMON):
    arr = list(map(int, input().split()))
    
    # 🎯 FOR MULTIPLE INTEGERS ON ONE LINE:
    a, b, c = map(int, input().split()) 
    # 🎯 FOR STRING:
    s = input().strip()
    
    # Your solution here
    result = sum(arr)
    
    # 🎯 FOR OUTPUT:
    print(result)
    print(s, n)
    print(a, b, c)

if __name__ == "__main__":
    main()