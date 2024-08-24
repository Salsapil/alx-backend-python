# Difference Between Unit and Integration Tests
## **1- Unit Tests:**   
- **Scope:** Focus on testing individual components or units of code in isolation, typically a single function or method.   
- **Purpose:** Ensure that each unit works correctly on its own.   
- **Dependencies:** External dependencies (like databases, APIs, or other services) are usually mocked or replaced with stubs so that the unit being tested operates in isolation.   
- **Speed:** Because they test small pieces of code without external dependencies, unit tests are usually fast to run.   
- **Examples:** Testing a mathematical function, like ensuring a sum() function correctly adds two numbers.   

## **2- Integration Tests:**   
- **Scope:** Evaluate how different units of code work together as a whole. They test the interactions between components, such as how functions or modules collaborate to achieve a task.   
- **Purpose:** Identify issues that arise when different units or modules are integrated. Integration tests check that these units work together as intended.   
- **Dependencies:** Involve actual dependencies like databases, file systems, or external APIs to ensure that all parts work correctly in a real-world environment.   
- **Speed:** Since they test multiple components together and often involve real dependencies, integration tests tend to be slower than unit tests.   
- **Examples:** Testing a full feature of an application, like verifying that user authentication works correctly, which might involve the UI, backend, and database.   

# Common Testing Patterns
## **1- Mocking:**
- **Definition:** Mocking is the process of creating fake versions of objects, functions, or services that mimic the behavior of real ones. This allows you to isolate the code under test from its dependencies.   
- **Purpose:** Mocking is used to simulate and control the behavior of complex or external dependencies, making it easier to test the code in isolation. It also allows you to simulate different scenarios, such as errors or specific responses from external services.   
- **Example:** If your function sends a request to an external API, you can mock the API call to return a predefined response instead of actually hitting the API.   

## **2- Parametrization:**
- **Definition:** Parametrization is the process of running a test case multiple times with different input values. It helps ensure that your code works correctly for a range of inputs.   
- **Purpose:** It allows you to test a function or method with multiple sets of data without writing separate test cases for each set.   
- **Example:** If you have a function that calculates the square of a number, you can parametrize the test to run with various numbers.    

## **3- Fixtures:**
- **Definition:** Fixtures are a way to set up a consistent and repeatable test environment before each test case runs. They can involve setting up databases, initializing variables, or configuring services.
- **Purpose:** Fixtures ensure that your tests run in a predictable environment, making them more reliable and easier to debug.
- **Example:** If your test relies on a database, a fixture might set up the database with known data before the test starts and clean it up afterward.
