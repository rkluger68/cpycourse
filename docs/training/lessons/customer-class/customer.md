!!! question "Lesson: Customer Class"
    
    === "Task"

        1. Create the following class-hierarchy:
        
            1. ***Class Customer***

                - class-attribute: `number_of_customers` (which should increment with every new class-instance)
                - class constructor with parameter: `email`, `employees`
                - instance-attribute: `id` (current value of `number_of_customers`)
                - instance-attribute: `email`
                - instance-attribute: `employees` (number of employees)
                - instance-method: `getEmployees` (returning `employees`)

            1. ***Class Retail(Customer)***

                - private class attribute: `__type` initialized to 'Retail'
                - class constructor with parameters: `name`, `email`, `employees`
                - private instance-attribute: `__retailname` (initialized with `name`-parameter)
                - instance-method: `getName` (returning private instance-attribute `__retailname`)
                - instance-method: `getType` (returning private class-attribute `__type`)

            2. ***Class Wholesale(Customer)***

                - private class attribute: `__type` initialized to 'Wholesale'
                - class constructor with parameters: `name`, `email`, `employee`
                - private instance-attribute: `__wholesalename` (initialized with `name`-parameter)
                - instance-method: `getName` (returning private instance-attribute `__wholesalename`)
                - instance-method: `getType` (returning private class-attribute `__type`)
        
        2. Create a `list` of Customers of different customer-types ('Retail'- and 'Wholesale'-customers)
            
        3. Output the attributes `name`, `type`, `id`, `employees` for all customers (use classic-loop or list-comprehension)    
      
    === "Hints" 

        - provide a callable interface `__call__()` for the derived classes returning the customer's name

    === "Solution" 

        ??? pied-piper "Example Customer-Class Implementation"

            ``` python title="customer.py"
            --8<-- "training/lessons/customer-class/customer.py"
            ```

            [:material-file-download:](customer.py)
