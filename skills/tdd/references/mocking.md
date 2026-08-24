# Mocking guidance

Mock system boundaries only:

- External APIs
- Time or randomness
- File systems when a real temporary file is impractical
- Databases when a test database is impractical

Do not mock your own classes, modules, or internal collaborators.

Pass external dependencies into the code instead of constructing them inside the behavior under test:

```typescript
function processPayment(order, paymentClient) {
  return paymentClient.charge(order.total);
}
```

Prefer a small typed operation for each external call over one generic fetcher with branching mock logic:

```typescript
const api = {
  getUser: (id) => fetch(`/users/${id}`),
  getOrders: (userId) => fetch(`/users/${userId}/orders`),
  createOrder: (data) => fetch("/orders", { method: "POST", body: data }),
};
```

Each boundary mock should return one specific shape and make the external operation under test obvious.
