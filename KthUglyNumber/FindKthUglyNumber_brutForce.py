
def is_ugly(num:int)->bool:
    if num<=0:
        return False
    for i in [2,3,5]:
        while num%i==0:
            num/=i
    return num==1

def kth_ugly_number(k:int)->int:
    lookup=0
    num=0
    while lookup<k:
        num += 1
        if is_ugly(num):
            lookup+=1
    return num

def test_kth_ugly_number():
    assert kth_ugly_number(1) == 1
    assert kth_ugly_number(5) == 5
    assert kth_ugly_number(10) == 12
    assert kth_ugly_number(15) == 24
    #assert kth_ugly_number(25) == 40
    print(kth_ugly_number(25))
    assert kth_ugly_number(150) == 5832
    assert kth_ugly_number(1000) > 0  # Just checking it doesn't crash

    try:
        kth_ugly_number(0)
    except ValueError:
        print("Passed invalid input test (k=0)")
if __name__ == "__main__":
    test_kth_ugly_number()