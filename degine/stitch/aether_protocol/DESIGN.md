# Design System Strategy: The Cyber-Editorial Framework

## 1. Overview & Creative North Star: "The Neon Scriptorium"
This design system rejects the clichéd, "boxy" look of traditional SaaS dashboards. Our Creative North Star is **The Neon Scriptorium**—a marriage of high-tech precision and elite editorial layout. We treat data as a sacred, high-stakes asset. 

To break the "template" look, we employ **intentional asymmetry**. Instead of centered, rigid grids, we use heavy left-weighted typography contrasted against expansive, breathing negative space. Elements overlap slightly—a header might bleed into a glass card—to create a sense of architectural depth and bespoke craftsmanship.

---

## 2. Colors: Tonal Depth & The "No-Line" Mandate
We do not build with lines; we build with light and atmosphere.

### The Palette
- **Core Neutral:** `surface` (#0b0e14) serves as our void.
- **Vibrant Accents:** `primary` (#81ecff) for "Actionable Intel" and `secondary` (#9f8eff) for "System Status."
- **Alerts:** `tertiary` (#ff6e84) for high-voltage warnings.

### The "No-Line" Rule
**1px solid borders are strictly prohibited for sectioning.** To define a workspace, use background shifts. 
*   **Implementation:** Place a `surface-container-high` (#1c2028) module directly onto the `surface` (#0b0e14) background. The 4% shift in luminance is sufficient for the human eye to perceive a boundary without the "clutter" of a stroke.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of semi-translucent plates:
1.  **Base:** `surface` (The floor)
2.  **Sectioning:** `surface-container-low` (The desk)
3.  **Interactive Modules:** `surface-container-high` (The paper)
4.  **Pop-overs/Modals:** `surface-bright` (The floating HUD)

### The "Glass & Gradient" Signature
To achieve "full attractiveness," use **Glassmorphism**. For floating timers or security widgets, use `surface-variant` at 60% opacity with a `20px` backdrop-blur. 
*   **Signature Glow:** Apply a linear gradient to `primary` CTAs: `primary` (#81ecff) to `primary-dim` (#00d4ec) at a 135-degree angle. This prevents the "flat" look and simulates a light-emitting diode.

---

## 3. Typography: Technical Authority
We pair the geometric precision of **Space Grotesk** with the utilitarian clarity of **Inter**.

*   **Display & Headlines (`Space Grotesk`):** These are our "anchors." Use `display-lg` (3.5rem) with tight letter-spacing (-0.02em) for account balances or high-level metrics. The slight quirkiness of Space Grotesk adds a "high-tech boutique" feel.
*   **Body & Labels (`Inter`):** All functional data uses Inter. It is the "workhorse" that ensures security logs and account settings are legible at a glance.
*   **The Data Narrative:** Use `label-md` for all metadata. In this system, metadata isn't just "small text"—it’s the technical substantiation of the UI.

---

## 4. Elevation & Depth: The Layering Principle
Shadows in this system are not black; they are "ambient occlusions."

*   **Ambient Shadows:** For floating elements, use a shadow color derived from `surface-container-highest` (#22262f) with a blur of `32px` and an opacity of 6%. It should feel like a soft hum, not a hard drop.
*   **The Ghost Border Fallback:** If accessibility requirements demand a border (e.g., in high-contrast modes), use `outline-variant` (#45484f) at **15% opacity**. It should be felt, not seen.
*   **Depth through Glow:** Interactive elements in a "hover" state should emit a `primary` glow. Use an `0px 0px 15px` outer glow with `surface-tint` (#81ecff) at 30% opacity to simulate a screen glowing in a dark room.

---

## 5. Components: Precision Engineered

### Buttons
*   **Primary:** Gradient fill (`primary` to `primary-dim`), `rounded-md`, no border.
*   **Secondary:** Ghost style. No fill, `ghost-border` (15% opacity), text in `primary`.
*   **Tertiary:** Text-only, `label-md` uppercase with 0.1rem letter spacing.

### Input Fields
Forbid the "four-sided box." Use a `surface-container-highest` background with a `2px` bottom-weighted accent in `outline` (#73757d). On focus, the bottom accent transitions to `primary` (#81ecff) with a soft 4px glow.

### Cards & Lists
*   **The Divider Rule:** Never use `<hr>` or border-bottom. Separate list items using `spacing-4` (0.9rem) of vertical white space or by alternating background shades between `surface-container` and `surface-container-low`.
*   **The "Security Pulse":** For active timers or live sessions, use a small `8px` circle with a CSS pulse animation using the `secondary` (#9f8eff) color.

### Additional Component: The "Glass Ledger"
A specialized dashboard widget for transaction history. Use a full-width `surface-container-low` container with `backdrop-blur`. Content inside is organized via **asymmetric columns**—large amounts on the left, tiny technical timestamps on the far right.

---

## 6. Do’s and Don’ts

### Do:
*   **Do** use `spacing-10` and `spacing-16` to create dramatic gaps between major sections.
*   **Do** use `primary-fixed-dim` for icons to ensure they feel "lit" against the dark background.
*   **Do** align text to a strict baseline, but allow decorative elements (like background gradients) to be organic and off-center.

### Don’t:
*   **Don't** use pure white (#FFFFFF). Always use `on-surface` (#ecedf6) to reduce eye strain in the dark theme.
*   **Don't** use `rounded-full` for functional buttons; keep them `rounded-md` (0.375rem) to maintain a "high-tech" architectural feel. Save `full` for status pips and chips.
*   **Don't** use standard "Folder" icons. Use abstract, thin-stroke geometric shapes to represent categories.

---

## 7. Spacing Scale: The Rhythm of Data
Our spacing is intentionally airy to counteract the density of technical data.
*   **Micro-interactions:** Use `spacing-1` to `spacing-2`.
*   **Component Internal Padding:** Use `spacing-4` (0.9rem).
*   **Section Gaps:** Use `spacing-12` (2.75rem) to create the "Editorial" feel. Space is luxury.