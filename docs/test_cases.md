# Test Cases

Format: ID | Requirement | Description | Precondition | Expected result | Type

## API — Product catalog

| ID | Requirement | Description | Expected result | Type |
|---|---|---|---|---|
| TC-API-01 | FR-01 | GET /products returns status code 200 | Status code 200 | Automated |
| TC-API-02 | FR-01 | The response contains a list of products in `data` | `data` is a non-empty list | Automated |
| TC-API-03 | FR-02 | GET /products filtered by category returns only products from that category | All returned products belong to the requested category | Pending |

## UI — Authentication

| ID | Requirement | Description | Precondition | Expected result | Type |
|---|---|---|---|---|---|
| TC-UI-01 | FR-05 | Log in with valid credentials | Registered user exists | Redirects to account page, displays username | Pending |
| TC-UI-02 | FR-06 | Log in with incorrect password | Registered user exists | Displays error message, does not log in | Pending |
| TC-UI-03 | FR-07 | Log out from an active session | User is logged in | Redirects to login page, session ends | Pending |

## UI — Shopping cart

| ID | Requirement | Description | Precondition | Expected result | Type |
|---|---|---|---|---|---|
| TC-UI-04 | FR-08 | Add a product to the cart | None | Cart counter increases by 1 | Pending |
| TC-UI-05 | FR-11 | Updating quantity recalculates the total | At least one product in the cart | Total updates correctly | Pending |