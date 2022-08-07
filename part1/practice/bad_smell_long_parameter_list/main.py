# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

class Unit:

    def __init__(self, state, speed, field):
        self.state = state
        self.speed = speed
        self.field = field

    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Не правильные данные')

    def move(self, direction, x, y):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(x=x, y=y + speed, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(x=x, y=y - speed, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(x=x - speed, y=y, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(x=x + speed, y=y, unit=self)
# class Unit:
#     def move(self, field, x_coord, y_coord, direction, is_fly, crawl, speed = 1):
#
#         if is_fly and crawl:
#             raise ValueError('Рожденный ползать летать не должен!')
#
#         if is_fly:
#             speed *= 1.2
#             if direction == 'UP':
#                 new_y = y_coord + speed
#                 new_x = x_coord
#             elif direction == 'DOWN':
#                 new_y = y_coord - speed
#                 new_x = x_coord
#             elif direction == 'LEFT':
#                 new_y = y_coord
#                 new_x = x_coord - speed
#             elif direction == 'RIGTH':
#                 new_y = y_coord
#                 new_x = x_coord + speed
#         if crawl:
#             speed *= 0.5
#             if direction == 'UP':
#                 new_y = y_coord + speed
#                 new_x = x_coord
#             elif direction == 'DOWN':
#                 new_y = y_coord - speed
#                 new_x = x_coord
#             elif direction == 'LEFT':
#                 new_y = y_coord
#                 new_x = x_coord - speed
#             elif direction == 'RIGTH':
#                 new_y = y_coord
#                 new_x = x_coord + speed




