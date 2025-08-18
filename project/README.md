### Problem Statement
- A grocery chain struggles with frequent stockouts and overstocking of perishable goods, leading to lost sales and waste. Current ordering relies heavily on manager intuition. Accurate demand forecasts for key SKUs could reduce waste and improve availability.

### Stakeholder & User
- Decision-makers: Supply Chain Director, Category Managers
- Primary users: Store managers, replenishment planners
- Workflow context: Forecasts generated overnight and integrated into the store ordering system by 6 AM daily. Forecast horizon: 1–14 days.

### Useful Answer
- Time-series forecast for daily demand per SKU/store. Decision: quantity to order. Metric: forecast MAPE, waste reduction %, sales uplift.

### Assumptions & Constraints
- Historical sales, promotions, and weather data available
- Latency: overnight batch acceptable
- Perishability means forecast horizon <14 days

### Known Unknowns / Risks
- Unpredictable spikes from local events
- Supplier delivery constraints
- New product introductions with no sales history

### Lifecycle Mapping
- Goal A: Reduce waste & stockouts → Problem Framing & Scoping (Stage 01) → Problem definition document (this)
- Goal B: Build forecasting prototype → Data Exploration & Model Development (Stage 02) → MVP forecast model tested on historical data
- Goal C: Integrate into ordering workflow → Deployment & Monitoring (Stage 03) → Productionized forecasting pipeline with dashboard monitoring