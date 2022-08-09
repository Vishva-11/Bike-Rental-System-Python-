import datetime


class BikeRental:

    def __init__(self, stock=0):
        #creating instances of bike rental shop
        self.stock = stock

    def displayStock(self):
        #displaying currently available bikes to rent
        print(f'We currently have {self.stock} bikes available for rent')
        return self.stock

    def BikeOnHourly(self, input):
        #rents bike on hourly basis
        if input < 0:
            print('Number of bikes should be positive!')
            return None

        elif input > self.stock:
            print(f'Sorry we have {self.stock} bikes available right now!')
            return None

        else:
            now = datetime.datetime.now()
            print(f'you have rented {input} bike/bikes on hourly basis today'
                  f'at {now.hour} on {now.date()}')
            print('you will be charged 5$ per bike per hour.')
            print('Have a great and healthy day!')

            self.stock -= input
            return now

    def BikeOnDailyBasis(self, n):

        if n< 0:
            print('Number of bikes should be positive!')
            return None
        elif n >self.stock:
            print(f'Sorry we have {self.stock} bikes available right now!')
        else:
            now = datetime.datetime.now()
            print(f'you have rented {n} bike/bikes on daily basis today'
                  f'at {now.hour} on {now.date()}')
            print('you will be charged 20$ per bike per day.')
            print('Have a great and healthy day!')

            self.stock -= n
            return now

    def BikeOnWeeklyBasis(self,m):

        if m< 0:
            print('Number of bikes should be positive!')
            return None
        elif m >self.stock:
            print(f'Sorry we have {self.stock} bikes available right now!')
        else:
            now = datetime.datetime.now()
            print(f'you have rented {m} bike/bikes on weekly basis today'
                  f'at {now.hour} on {now.date()}')
            print('you will be charged 80$ per bike per day.')
            print('Have a great and healthy day!')

            self.stock -= m
            return now

    def ReturnBike(self, request):

        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            if rentalBasis ==1:
                bill = round(rentalPeriod.seconds/3600) *5*numOfBikes
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) *20* numOfBikes
            elif rentalBasis ==3:
                bill = round(rentalPeriod.days/7) *80* numOfBikes
            else:
                print('Are u sure u rented a bike with us?')
                return None

class Customer:

    def __init__(self):
        print('Enter no.of bikes, whether you want to rent on hourly, daily or weekly'
              'basis by typing 1,2 0r 3 for each respectively. Also enter rental-time in hours')
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):

        bikes = input('How many bikes do u like to rent?')

        try:
            bikes = int(bikes)
        except ValueError:
            print('Please enter a positive number')
            return -1
        except TypeError:
            print('Only enter a number')
            return -1

        if bikes <1:
            print('Invalid Input. number of bikes hould be greater than zero')
        else:
            self.bikes = bikes
        return self.bikes

    def returnBike(self):

        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0,0,0