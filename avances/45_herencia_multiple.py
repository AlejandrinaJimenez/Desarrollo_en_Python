class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hora =h
        self.minuto = m
        self.segundo = s

    def getTime(self):
        res = str(self.hora) + ":"
        res += str(self.minuto) + ":"
        res += str(self.segundo)
        return  res

class Calendar:
    def __init__(self, d, m, a):
        self.d =d
        self.m = m
        self.a = a

    def getToday(self):
        res = str(self.d) + "/"
        res += str(self.m) + "/"
        res += str(self.a)
        return res


class Clock(Time, Calendar):
    def __init__(self ,
               hora, minuto, segundo,
               dia, mes, anio,
               marca, **kwars):
        Time.__init__(self, hora, minuto, segundo)
        Calendar.__init__(self, dia, mes, anio)
        self.marca = marca

    def getTime(self):
        res = self.marca + "\t"
        res += Time.getTime(self) + "\t"
        res += Calendar.getToday(self)
        return res

clock = Clock(12, 42, 28,
              25, 1, 2019,
              marca = "SAMSUNG")
print(clock.getTime())
