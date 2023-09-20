class Customer:
    ''' This is a customer class '''
    # class-wide attribute(s) - common to all class-instances '''
    number_of_customers = 0

    def __init__(self, email, employees):
        ''' class instance initialization '''
        # some instance attributes
        self.email = email
        self.employees = employees
        Customer.number_of_customers += 1
        self.id = Customer.number_of_customers

    def getEmployees(self):
        return self.employees


class Retail(Customer):
    __type = 'Retail'
    def __init__(self, name, *args):     # use variadic parameter '*args'
        # call base class constructor
        self.__retailname = name         # 'private' (name-mangled) instance-attribute 
        Customer.__init__(self, *args)

    def __call__(self):
        return self.getName()            # (1) call instance-method
        #return self.__retailname        # (2) access private attribute

    def getName(self):
        return self.__retailname

    def getType(self):
        return self.__type               # access private attribute


class Wholesale(Customer):
    __type = 'Wholesale'
    def __init__(self, name, *args):     # use variadic parameter *args
        # call base class constructor
        self.__wholesalename = name      # 'private' (name-mangled) instance-attribute
        Customer.__init__(self, *args)

    def __call__(self):
        return self.getName()            # (1) call instance-method
        #return self.__wholesalename     # (2) access private attribute

    def getName(self):
        return self.__wholesalename      # access private attribute

    def getType(self):
        return self.__type


def main():
    print(f'Number of customers - on start: {Customer.number_of_customers}')

    # Create customers of different type
    customers = [
        Retail('Peter - Fish & Chips', 'peter@email.com', 4),
        Retail('Bob - Pipe Cleaning', 'bob.@email.com', 13),
        Wholesale('Brown Chemicals', 'brown.chemicals@email.com', 3500),
        Wholesale('Duck Industries','duck.industries@email.com', 1800),
        ]

    print(f'Number of customers - after creation of customers: {Customer.number_of_customers}')

    # output using classic loop
    print('\n>>> 1. Output using classic for loop <<<\n')
    for customer in customers:
        print(f'''
        Customer Name: {customer()}
        Customer Id: {customer.id}
        Customer Type: {customer.getType()}
        Number of Employees: {customer.employees}
        ''')
    
    # output using list comprehension
    print('>>> 2. Output using list comprehension <<<\n')
    [ print(f'''
        Customer Name: {c()}
        Customer Id: {c.id}
        Customer Type: {c.getType()}
        Number of Employees: {c.employees}
    ''') for c in customers]

if __name__ == '__main__':
    main()

