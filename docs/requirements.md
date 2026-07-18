# Functional Requirements — Toolshop (Practice Software Testing)

## Scope
This document describes the functional requirements covered by the automation
suite in this project, for the Toolshop demo application
(https://practicesoftwaretesting.com), covering both its web interface and its
REST API (https://api.practicesoftwaretesting.com).

## Modules covered

### 1. Product catalog (API + UI)
- FR-01: The system must list available products.
- FR-02: The system must allow filtering products by category.
- FR-03: The system must allow searching products by name.
- FR-04: Each product must display name, price, and image.

### 2. Authentication (API + UI)
- FR-05: A registered user must be able to log in with valid credentials.
- FR-06: The system must reject login attempts with invalid credentials.
- FR-07: The system must correctly log the user out on logout.

### 3. Shopping cart (UI)
- FR-08: A user must be able to add one or more products to the cart.
- FR-09: A user must be able to update the quantity of a product in the cart.
- FR-10: A user must be able to remove a product from the cart.
- FR-11: The cart total must be recalculated correctly after any change.

### 4. Checkout (UI)
- FR-12: A user must be able to complete a purchase with valid shipping details.
- FR-13: The system must validate required fields before allowing progress.

## Out of scope
- Real payments (the app is a demo and does not process real payments).
- Load or performance testing.
- Security testing (penetration testing).