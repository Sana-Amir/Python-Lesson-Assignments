class Mathematician:
    def square_nums(self, numbers):
        return [n*n for n in numbers]

    def remove_positives(self, numbers):
        remove_positives = [number for number in numbers if number<0]
        return remove_positives

    def filter_leaps(self, numbers):
        filter_leaps = [number for number in numbers if number %4==0]
        return filter_leaps

m = Mathematician()


# m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
print(m.square_nums([7, 11, 5, 4]))

#m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
print(m.remove_positives([26, -11, -8, 13, -90]))

#m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))