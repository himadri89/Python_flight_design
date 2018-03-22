import string


class Aircraft:
    def __init__(self,registration, model, num_rows, num_seats_per_row):
        if num_rows < 0:
            raise ValueError("Number of rows {}cannot be negative".format(num_rows))
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
        
    def registrtration(self):
        return self._registration
    
    def model(self):
        return self._model
    
    def seating_plan(self):
        return (range(1, self._num_rows + 1), string.ascii_uppercase[: self._num_seats_per_row])
    
    def __str__(self):
        return "The aircraft is " + self._registration + " model is " + self._model + " with seats of " + str(self._num_seats_per_row)
    
    def console_card_printer(passenger, seat, flight_num, aircraft):
        op = "| Name: {0}"  \
             "  Flight: {1}" \
             "  Seat: {2}" \
             "  Aircraft: {3}" \
             " |".format(passenger,flight_num,seat, aircraft)
        top = "+" + "-" * (len(op)-2) + "+"
        border = "|" + " " * (len(op)-2) + "|"
        lines = [top, border, op, border, top]
        boarding_pass = '\n'.join(lines)
        print(boarding_pass)
        print()