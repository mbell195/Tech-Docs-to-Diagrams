# Order Processing System

**Author:** Marc Bell

## 1. Global Overview (Workflow B)

Our order processing system operates on a global scale, ensuring low-latency transactions regardless of user location.

![Global Network](../assets/diagrams-generated/global-network.png)

**Figure 1:** Conceptual view of our global node distribution.

---

## 2. Checkout Logic (Workflow A)

The engineering team must adhere to the following strict logic for inventory locking. This diagram is auto-generated from our source code.

![Checkout Logic](../assets/diagrams-generated/checkout-logic.svg)

**Figure 2:** The precise inventory validation flow.

---

## 3. Simplified View for Stakeholders (Workflow C)

For non-technical presentations, the logic above can be visualized as a simplified whiteboard sketch to explain the "Lock & Charge" mechanism.

![Checkout Whiteboard](../assets/diagrams-generated/checkout-whiteboard.png)

**Figure 3:** High-level process flow.
