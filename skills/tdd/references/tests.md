# Test examples

Prefer tests that describe observable behavior through a public interface.

```typescript
test("user can checkout with a valid cart", async () => {
  const cart = createCart();
  cart.add(product);
  const result = await checkout(cart, paymentMethod);

  expect(result.status).toBe("confirmed");
});
```

Avoid tests coupled to internal calls:

```typescript
test("checkout calls paymentService.process", async () => {
  const mockPayment = jest.mock(paymentService);
  await checkout(cart, payment);

  expect(mockPayment.process).toHaveBeenCalledWith(cart.total);
});
```

Verify through the interface rather than a side channel. For example, after `createUser`, call `getUser` instead of querying the database directly.

Expected values need an independent source of truth:

```typescript
test("calculateTotal sums line items", () => {
  expect(calculateTotal([{ price: 10 }, { price: 5 }])).toBe(15);
});
```

Do not compute the expected result with the same algorithm as the code under test. A test that copies the implementation can pass by construction.
