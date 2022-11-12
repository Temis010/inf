def q(a):
    if len(a)<=1:
        return a
    else:
        b = a[1]
        s = []
        m = []
        e = []
        for i in a:
            if i < b:
                s.append(i)
            elif i>b:
                m.append(i)
            else:
                e.append(i)
        return q(s) + e + q(m)

