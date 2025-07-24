## Overview

This document summarizes the key issues found in the original codebase, the changes made during refactoring, assumptions made, and potential improvements if given more time.

------------------------------------------------------------------------------------------------------------------------------------------

1# Major Issues Identified:-

  - The codebase was monolithic and lacked structure making less readable ,modular and less maintainable.

  - Business logic and data access code were tightly coupled inside route handlers.
  
  - No data validation making less secure causing easy injection.

  - SQL queries were manually concatenated with user inputs, creating a serious SQL injection risk.

  - Error handling was inconsistent and often vague, making debugging harder.

  - Tests were not modular and had limited coverage.

------------------------------------------------------------------------------------------------------------------------------------------

2# Changes Made and Why?

  - Modularized Codebase: Used Cleaner Architecture.

      - Split the code into separate layers: controllers, services, DB Layer(DAO), Helpers , Exceptions.

      - Used controller for APIs (main entry point of request), used services for business logic , Dao for DB access  ,Helpers method for Common response and Error Code.

      - This improves maintainability, testability, and readability.

  - Input Validation Layer Added:

      - Checked for mandatory fields and raised validation errors in service layer.
    
      - To prevent invalid data or incomplete data to enter in system.

  - Custom Exception:

      - Created meaningful exceptions to show different messages into meaningful responses including Status codes.
      
      - Promotes reuse and consistent error messages throughout the codebase.

  - Centralized Error Handling: 

      - Added a centralized error handler that catches custom and built-in exceptions.

      - Ensures every error response follows a consistent meaningful structure.

  - Parameterized SQL Queries

      - Replaced raw SQL concatenation with parameterized queries to avoid SQL injection.

      - Increases safety and readability of database operations.

  - Common Responses and Error codes:

      - Introduced a Helpers file to store reusable error messages and status codes.

      - Makes it easier to manage and update messages globally.

  - Refactored Tests

      - Updated tests to follow the new layered structure and mock dependencies correctly.

      - Added edge case and failure scenario tests to increase coverage.

------------------------------------------------------------------------------------------------------------------------------------------

3# Justification for Architectural Decisions:

  - The layered architecture supports the Separation of Concerns principle, keeping code clean and organized making more readable and maintainable.

  - Custom exceptions improve error reporting and are easier to debug and trace the errors.

  - Parameterized queries protect the application from SQL injection.

  - Centralized error handling ensures consistency and simplifies error management.

  - Using constants reduces hardcoding and makes localization or updates more manageable.

------------------------------------------------------------------------------------------------------------------------------------------

4# Trade-offs Made:

  - The new structure introduces extra files and complexity for small apps.

  - Input validation was done manually and could benefit from specialized libraries.

  - Error messages and codes are manually written instead of being dynamic or from external sources.

------------------------------------------------------------------------------------------------------------------------------------------

5# What I Would Do with More Time:

  - Add database migration tools and seed data scripts for better setup.

  - Integrate an ORM like SQLAlchemy for cleaner and more scalable data access.

  - Implement role-based authentication and token expiration for better security.

  - Introduce data validation libraries like marshmallow or pydantic.

  - Add logging with Python's logging or loguru for traceability and debugging.

  - Document all APIs with Swagger/OpenAPI for better developer usability and testing APIs.
