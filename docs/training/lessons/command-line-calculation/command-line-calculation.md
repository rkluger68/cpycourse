!!! question "Lesson: Command Line Calculation"
    
    === "Task"
    
        Use Python as a "command line calculator" to calculate repayment plus
        compound interest for 

        - a yearly interest of 3%,
        - a duration of 3 years and
        - an investment of 91514.17 €.

    === "Hints"

        Perform the task in an interative Python session (the "REPL"), on the
        command line or e.g. in Jupyter.

    === "Solution"

        ??? example

            ```
            >>> 91514.17 * 1.03**3
            100000.00444159
            ```

            Explanation:
            
            ```
            >>> principal = 91514.17
            >>> interest_rate = 0.03 
            >>> q = 1 + interest_rate  # factor
            >>> t = 3  # time interval in years
            >>> accumulated_value = principal * q**t
            >>> accumulated_value
            100000.00444159
            ```


