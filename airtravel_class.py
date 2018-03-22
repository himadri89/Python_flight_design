from pprint import pprint as pp
from Aircraft import *

class Flight:
    
    def __init__(self,number, aircraft):
        
        if not number[:2].isalpha():
            raise ValueError("NO airline code in  {}".format(number))
            
        if not number[:2].isupper():
            raise ValueError("Invalid code in {}".format(number))
            
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number in {}".format(number))
        
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letters: None for letters in seats} for _ in rows]
        
    def number(self):
        return self._number
    
    def airline(self):
        return self._number[:2]
    
    def aircraft_model(self):
        return self._aircraft.model()
    
    def _parse_seat(self,seat):
        """Parse a seat designator into rows and letter
        Args:
            seat: Aseat like 12F
        Returns:
            A tuple returning seat and row
        """
        row_num, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid Seat {}".format(letter))
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except:
            raise ValueError("Invalid Seat row {}".format(row))
        
        if row not in row_num:
            raise ValueError("Invalid row num {}".format(row))
        
        return row, letter
        
    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger
        Args:
            seat: Seats like 12A, 22B
            passenger: Passenger to be allocated in that seat
        Raises:
            ValueError if the seat is unavailable
        """
        row, letter =self._parse_seat(seat)
            
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} is already occupied".format(seat))
        
        self._seating[row][letter] = passenger
        
    def relocate_passenger(self, from_seat, to_seat):
        """ Relocates a passenger from one seat to another
        Args:
            from_seat: The passenger's existing seat
            to_seat: The new seat after changing
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))
            
        to_row, to_letter = self._parse_seat(to_seat)    
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("The seat {} is accupied".format(to_seat))
        
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None
        
    def num_seats_available(self):
        return sum(sum(1 for i in row.values() if i is None) for row in self._seating 
                   if row is not None)
     
    def make_boarding_card(self, card_printer):
        for passenger,seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self._number(), self.aircraft_model())
            
    def _passenger_seats(self):
        row_num, seat_letters = self._aircraft.seating_plan()
        for row in row_num:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row,letter))
                    





Flight1 = Flight("BA445", Aircraft("BBAZ990", "Airbus Alta", 10, 3))

pp(Flight1._seating)
Flight1.allocate_seat('3A', 'Patricia')
Flight1.allocate_seat('3B', 'Himadri')
Flight1.allocate_seat('3C', 'Iana')
Flight1.allocate_seat('3B', 'Caitlyn')
Flight1.relocate_passenger('4A', '3A')
Flight1.num_seats_available()
Flight1.make_boarding_card(Aircraft.console_card_printer)






