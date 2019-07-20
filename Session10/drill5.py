nhanvien = [
    {
        "Name":"Huy",
        "Role":"Waiter",
        "Hours": 12,
        "Slary per hour": 0.8
    },
    {
        "Name":"Tung",
        "Role":"cooker",
        "Hours": 24,
        "Slary per hour": 1.5
    },
    {
        "Name": "M.Duc",
        "Role":"Manager",
        "Hours": 20,
        "Slary per hour": 2.0
    }
]
a={
"Name":"Don",
"Role": "Waiter",
"Hours": 12,
"Salary per hour": 0.9
}
b={
"Name":"H.Duc",
"Role": "Waiter",
"Hours": 14,
"Salary per hour": 0.7
}
nhanvien.append(a)
nhanvien.append(b)
for i in range(len(nhanvien)):
    # print(i,":",nhanvien[i])
    for j in nhanvien[i]:
        print(j,":",nhanvien[i][j])
    print("="*100)